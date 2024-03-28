class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # basically if a subarray multiplication is < k then all of its internal subarray multiplications also will be < k
        res = 0 
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            res += (r - l + 1)
        return res
            