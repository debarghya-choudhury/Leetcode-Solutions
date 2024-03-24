class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hSet = set()
        for i in nums:
            if i in hSet:
                return i
            else:
                hSet.add(i)