class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = [*nums, *nums]  # solved with unpacking operator
        # return ans

        # return nums + nums
        # return nums*2

        n = 2*len(nums)
        ans = [0]*n
        i = 0
        while i < len(nums):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]    
            i += 1
        return ans       

# Learned that in python after we declare an empty array
# arr = []
    
# We can't do like 
# arr[0] = 1
    
# So while Python does support dynamic list creation, 
# the syntax for adding elements to the list differs from JavaScript.                
