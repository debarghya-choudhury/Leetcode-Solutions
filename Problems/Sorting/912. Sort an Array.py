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
        # if len(nums) == 1:
        #     return nums
        # else:
        #     mid = len(nums) // 2
        #     x = nums[0:mid]
        #     y = nums[mid:len(nums)]
        #     x = self.sortArray(x) 
        #     y = self.sortArray(y)
        #     arr = self.merge(x, y)
        #     return arr

        # quick sort
        if len(nums) <= 1:
            return nums
        pivot = len(nums) - 1
        p1 = p2 = 0

        for i in range(0, len(nums) - 1):
            if nums[p2] <= nums[pivot]:
                hold = nums[p2]
                nums[p2] = nums[p1]
                nums[p1] = hold
                p1 += 1
            p2 += 1
        hold = nums[p1]
        nums[p1] = nums[pivot]
        nums[pivot] = hold
        print(nums)
        nums[:p1] = self.sortArray(nums[0:p1])
        nums[p1+1:] = self.sortArray(nums[p1+1:pivot+1])
        return nums
        
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