class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mapObj = map(lambda x: x**2, nums) # map() returns iterable map object -->  <map object at 0x7bcdb0233580>
        nums = list(mapObj)  # creates list from iterable object

         # I only know manual bubble sort which is O(n**2) so sorry
        nums.sort()   # sort in python changes original array and returns none if saved to a variable
        # or
        nums2 = sorted(nums)
        return nums2