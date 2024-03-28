class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = r = 0
        hMap = {}
        ans = 0
        for r in range(len(nums)):
            if nums[r] in hMap:
                hMap[nums[r]] += 1
                while hMap[nums[r]] > k and l <= r:
                    # print("l", l, "r", r)
                    hMap[nums[l]] -= 1
                    l += 1
            else:
                hMap[nums[r]] = 1
            # print("l", l, "r", r)
            # print(hMap)
            ans = max(ans, (r - l + 1))
            # print("ans", ans)
        # print(hMap)
        # print("l", l)
        # print("r", r)
        return ans