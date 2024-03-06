class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Using Bucket Sort (Good when we know what elements are present in the array)
        
        bucket = [0, 0, 0]   # bucket containing number of [red, white, blue]
        for i in nums:
            if i == 0:
                bucket[0] += 1
            elif i == 1:
                bucket[1] += 1
            else:
                bucket[2] += 1
        for i in range(0, len(nums)):
            if i < bucket[0]:
                nums[i] = 0
            elif i >= bucket[0] and i < bucket[0] + bucket[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        