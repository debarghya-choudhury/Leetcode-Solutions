exports.confirmMonthlyContractPaymentUsingSTCPayAndWallet = (req, res) => {
	const userID = req.body.userID || req.query.userID || req.params.userID;
	const contractID = req.body.contractID || req.query.contractID || req.params.contractID;
	const timestamp = req.body.timestamp || req.query.timestamp || req.params.timestamp;

	const otpReference = req.body.otpReference || req.query.otpReference || req.params.otpReference;
	const stcPayPmtReference = req.body.stcPayPmtReference || req.query.stcPayPmtReference || req.params.stcPayPmtReference;
	const otp = req.body.otp || req.query.otp || req.params.otp;

	const amount = req.body.amount || req.query.amount || req.params.amount;
	const walletAmount = req.body.walletAmount || req.query.walletAmount || req.params.walletAmount;
	let priceToken = req.body.priceToken || req.query.priceToken || req.params.priceToken;
	if (!priceToken) {
		priceToken = ""
	}


	confirmPaymentUsingSTCPayAndWallet(userID, contractID, amount, walletAmount, timestamp, otpReference, stcPayPmtReference, otp, priceToken).then(response => {
		res.send(response);
	});
};

async function confirmPaymentUsingSTCPayAndWallet(userID, contractID, amount, walletAmount, timestamp, otpReference, stcPayPmtReference, otp, priceToken) {

	let currentAmountInWallet = 0;
	let walletUserID = userID;

	let userRecord = await config.database.collection("users").find({
		userID: userID
	}).toArray();
	if (userRecord.length > 0) {
		let typeOfUser = userRecord[0]["registeredAs"];
		if (typeOfUser == "company") {
			if (userRecord[0]["roleInCompany"] != "superAdmin") {
				walletUserID = userRecord[0]["companyID"];
			}
		}
	}

	let walletRecord = await config.database.collection("wallets").find({
		userID: walletUserID
	}).toArray();
	if (walletRecord.length > 0) {
		currentAmountInWallet = walletRecord[0]["amount"];
	}

	if (currentAmountInWallet < walletAmount) {
		return {
			"error": "Not able to place contract due to change in wallet balance"
		};
	} else {
		let netWalletAmount = currentAmountInWallet - walletAmount;
		netWalletAmount = netWalletAmount.round(2);
		let updateWalletRecord = await config.database.collection("wallets").findOneAndUpdate({
			"userID": walletUserID
		}, {
			"$set": {
				"amount": netWalletAmount
			}
		});

		let checkPaymentStatus = await config.database.collection("payments").find({
			"userID": userID,
			"contractID": contractID,
			"transactionID": timestamp
		}).toArray()

		let walletPayments = {
			type: "wallet",
			date: checkPaymentStatus[0].date,
			amount: walletAmount
		}
		let updateContractWalletPayment = await config.database.collection("monthlyContracts").updateOne({
			"userID": userID,
			"contractID": contractID,
			"timestamp": timestamp
		}, {
			"$push": {
				"payments": walletPayments
			}
		});

		let confirmStcPayResponse = await createSTCPayDirectPaymentConfirm(otpReference, stcPayPmtReference, otp);
		console.log("STC Payment Confirmation Status:", confirmStcPayResponse);
		if (confirmStcPayResponse.hasOwnProperty("DirectPaymentConfirmV4ResponseMessage")) {
			let paymentStatus = confirmStcPayResponse["DirectPaymentConfirmV4ResponseMessage"]["PaymentStatus"];
			let paymentStatusDesc = confirmStcPayResponse["DirectPaymentConfirmV4ResponseMessage"]["PaymentStatusDesc"];

			if (paymentStatus == 2 && paymentStatusDesc == "Paid") {
				let updatePaymentStatus = await config.database.collection("payments").updateOne({
					"userID": userID,
					"contractID": contractID,
					"transactionID": timestamp
				}, {
					"$set": {
						"paymentStatus": "SUCCESS"
					}
				});
				
				let payments = {
					"type": "online",
					"date": checkPaymentStatus[0].date,
					"amount": checkPaymentStatus[0].amount,
					"transactionID": timestamp,
					"gateway": "STC",
					"stcPayPmtReference": stcPayPmtReference,
					"stcPayMobileNumber": checkPaymentStatus[0].stcPayMobileNumber
				}
				let updateContractStatus = await config.database.collection("monthlyContracts").updateOne({
					"userID": userID,
					"contractID": contractID,
					"timestamp": timestamp
				}, {
					"$set": {
						"paymentStatus": "SUCCESS",
						"status": "active"
					},
					"$push": {
						payments: payments
					}
				});

				if(priceToken) {
					// Update getPriceHistory to mark order placed after hitting get price
					let updateGetPriceHistoryStatus = await config.database.collection("getMonthlyContractsPriceHistory").updateOne({priceToken}, {$set:{"status":"placed"}});
					if (updateGetPriceHistoryStatus.modifiedCount > 0) {
						logger.info(`Status of price history token ${priceToken} is updated successfully to placed state.`);
					} else {
						logger.error(`Updating status of price history token ${priceToken} to placed state is failed.`);
					}
				}
				// Send monthly contract info to zoho
				await callZohoAPIs.callInsertMonthlyContractZohoAPI(contractID);
				return {
					//"success": "Contract placed successfully and your contract id is " + contractID
					"success": "Contract placed successfully and your transaction id is " + timestamp
				};
			} else {
				// Refund deducted wallet amount
				let currentAmountInWallet = 0;
				let walletRecord = await config.database.collection("wallets").find({
					userID: walletUserID
				}).toArray();
				if (walletRecord.length > 0) {
					currentAmountInWallet = walletRecord[0]["amount"];
				}
				let netWalletAmount = currentAmountInWallet + walletAmount;
				netWalletAmount = netWalletAmount.round(2);
				let updateWalletRecord = await config.database.collection("wallets").findOneAndUpdate({
					"userID": walletUserID
				}, {
					"$set": {
						"amount": netWalletAmount
					}
				});

				let updatePaymentStatus = await config.database.collection("payments").updateOne({
					"userID": userID,
					"contractID": contractID,
					"transactionID": timestamp
				}, {
					"$set": {
						"paymentStatus": "paymentStatusDesc"
					}
				});
				let updateContractStatus = await config.database.collection("monthlyContracts").updateOne({
					"userID": userID,
					"contractID": contractID,
					"timestamp": timestamp
				}, {
					"$set": {
						"paymentStatus": "paymentStatusDesc",
						"status": "IN-PROGRESS"
					}
				});
				return {
					"error": "Payment Failed"
				};
			}
		} else {
			// Refund deducted wallet amount
			let currentAmountInWallet = 0;
			let walletRecord = await config.database.collection("wallets").find({
				userID: walletUserID
			}).toArray();
			if (walletRecord.length > 0) {
				currentAmountInWallet = walletRecord[0]["amount"];
			}
			let netWalletAmount = currentAmountInWallet + walletAmount;
			netWalletAmount = netWalletAmount.round(2);
			let updateWalletRecord = await config.database.collection("wallets").findOneAndUpdate({
				"userID": walletUserID
			}, {
				"$set": {
					"amount": netWalletAmount
				}
			});

			let updatePaymentStatus = await config.database.collection("payments").updateOne({
				"userID": userID,
				"contractID": contractID,
				"transactionID": timestamp
			}, {
				"$set": {
					"paymentStatus": "FAILED"
				}
			});
			let updateContractStatus = await config.database.collection("monthlyContracts").updateOne({
				"userID": userID,
				"contractID": contractID,
				"timestamp": timestamp
			}, {
				"$set": {
					"paymentStatus": "FAILED",
					"status": "deleted"
				}
			});
			return {
				"error": "Payment Failed"
			};
		}
	}
}

async function createSTCPayDirectPaymentConfirm(OtpReference, STCPayPmtReference, OtpValue) {
	let inputJSON = {
		"DirectPaymentConfirmV4RequestMessage": {
			"OtpReference": OtpReference,
			"STCPayPmtReference": STCPayPmtReference,
			"OtpValue": OtpValue,
			"OtpValue": OtpValue,
			"TokenReference": "string",
			"TokenizeYn": true
		}
	};
	console.log("config.stcPayOnlineMerchantID::", config.stcPayOnlineMerchantID);
	console.log("config.stcPayHostname::", config.stcPayHostname);
	console.log("config.stcPayBaseURL::", config.stcPayBaseURL);
	console.log(path.resolve(__dirname, "../security/final.crt"));
	console.log(path.resolve(__dirname, "../security/private.key"));
	const options = {
		hostname: config.stcPayHostname,
		path: '/B2B.DirectPayment.WebApi/DirectPayment/V4/DirectPaymentConfirm',
		url: config.stcPayBaseURL + 'B2B.DirectPayment.WebApi/DirectPayment/V4/DirectPaymentConfirm',
		cert: fs.readFileSync(path.resolve(__dirname, "../security/final.crt")),
		key: fs.readFileSync(path.resolve(__dirname, "../security/private.key")),
		method: 'POST',
		json: inputJSON,
		headers: {
			'Content-Type': 'application/json',
			'X-ClientCode': config.stcPayOnlineMerchantID
		}
	};

	console.log("BEFORE PROMISE");

	let responseJSON = await waitForResults(options);
	console.log("AFTER PROMISE:", responseJSON);

	return responseJSON;
}