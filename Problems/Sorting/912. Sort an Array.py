class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # if len(nums) <= 1:
        #     return nums

        # # insertion sort
        # for i in range(1, len(nums)):
        #     for j in range(i-1, -1, -1):
        #         x = j+1
        #         if nums[j] > nums[x]:
        #             # swap
        #             hold = nums[j]
        #             nums[j] = nums[x]
        #             nums[x] = hold
        # return nums

        # merge sort
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums) // 2
            x = nums[0:mid]
            y = nums[mid:len(nums)]
            x = self.sortArray(x) 
            y = self.sortArray(y)
            arr = self.merge(x, y)
            return arr

    def merge(self, x: List[int], y: List[int]) -> List[int]:
        i = j = 0
        arr = []
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                arr.append(x[i])
                i += 1
            else:
                arr.append(y[j])
                j += 1
        if i < len(x):
            arr += x[i:len(x)]
        if j < len(y):
            arr += y[j:len(y)]
        return arr