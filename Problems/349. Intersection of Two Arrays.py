class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set1 = set(nums1)
        # set2 = set(nums2)
        # res = set([])
        # for i in set1:
        #     if i in set2:
        #         res.add(i)
        # return list(res)

        # alternative method
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        return list(intersection)
