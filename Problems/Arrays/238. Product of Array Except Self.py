class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # resArr = []                          #  O(n^2)
        # for i in range(len(nums)):
        #     mul = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             mul *= nums[j]
        #     resArr.append(mul)
        # return resArr

        resArr = []

        mul = 1
        for i in range(len(nums)):
            if mul == 0:
                break
            mul *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] != 0:
                x = mul // nums[i]
                resArr.append(x)
            else:
                multi = 1
                for j in range(len(nums)):
                    if multi == 0:
                        break
                    if i != j:
                        multi *= nums[j]
                resArr.append(multi)
        
        return resArr
