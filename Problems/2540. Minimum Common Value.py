class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        mnm = -1
        flag = False
        st = set(nums1)
        for i in nums2:
            if i in st:
                mnm = min(mnm, i) if flag == True else i
                flag = True
        return mnm