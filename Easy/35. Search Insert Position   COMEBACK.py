class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(0, len(nums)):     #   O(n) 
            if nums[i] == target:
                result = i
            elif target > nums[i]:
                result = i+1
        return result        
    
# Need one more solution with binary sort in O(log n)    