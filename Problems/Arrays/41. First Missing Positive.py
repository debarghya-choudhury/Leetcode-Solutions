class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] > 1:
            return 1
        i = 0 
        flag = False
        while i < len(nums):
            if nums[i] < 0:
                flag = True
                if i == len(nums) - 1:
                    return 1
                i += 1
            elif nums[i] == 0:
                flag = False
                i += 1
            else:
                if nums[i] == 1:
                    i += 1
                elif nums[i] > 1 and flag == True:
                    print("here", nums[i])
                    return 1
                elif i < len(nums):
                    if nums[i] - nums[i - 1] > 1:
                        return nums[i - 1] + 1
                    else:
                        i += 1
                else:
                    i += 1
                flag = False
        return nums[-1] + 1

