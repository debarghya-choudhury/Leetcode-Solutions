class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # ans = 0                                      # O(n^2) Brute Force Approach

        # for i in range(0, len(nums)):
        #     counts = {
        #         0: 0,
        #         1: 0
        #     }
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             counts[0] += 1
        #         else:
        #             counts[1] += 1
                
        #         if counts[0] == counts[1]:
        #             counts[0] = 0
        #             counts[1] = 0
        #             ans = max(j-i+1, ans)
        
        # return ans

        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len



