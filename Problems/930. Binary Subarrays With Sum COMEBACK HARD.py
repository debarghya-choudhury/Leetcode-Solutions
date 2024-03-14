class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # if len(nums) < goal:
        #     return 0

        # count = 0                                        # O(n^2) because im dumb
        # for i in range(0, len(nums)): 
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total == goal:
        #             count += 1
        #         elif total > goal:
        #             break
        # return count

        def helper(x):                                # O(n) thx neetcode
            if x < 0: return 0

            count = 0
            currSum = 0
            L = R = 0
            while R < len(nums):
                currSum += nums[R]
                while currSum > x:
                    currSum -= nums[L]
                    L += 1
                count += R - L + 1
                R += 1
            return count

        return helper(goal) - helper(goal - 1)

