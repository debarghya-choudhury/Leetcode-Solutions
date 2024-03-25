class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hSet = set()
        res = []
        for i in nums:
            if i in hSet:
                res.append(i)
            else:
                hSet.add(i)
        return res