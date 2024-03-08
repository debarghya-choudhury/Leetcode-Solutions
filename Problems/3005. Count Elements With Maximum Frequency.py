class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        mxm = 0
        dct = {}
        for i in range(0, len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = 1
                mxm = max(mxm, dct[nums[i]])
            else:
                dct[nums[i]] += 1
                mxm = max(mxm, dct[nums[i]])
        
        for i in dct:
            if dct[i] == mxm:
                ans += dct[i]
        
        return ans