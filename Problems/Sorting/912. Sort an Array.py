class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        # insertion sort
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                x = j+1
                if nums[j] > nums[x]:
                    # swap
                    hold = nums[j]
                    nums[j] = nums[x]
                    nums[x] = hold
        return nums

        # merge sort
                        
                



        