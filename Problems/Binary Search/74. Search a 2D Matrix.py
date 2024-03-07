class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        # matrix.sort(key = lambda x: x[0])
        emp = []
        for e in matrix:
            emp = emp + e
        print(emp)
        return self.binarySearch(emp, target)

    def binarySearch(self, arr: List[int], target: int) -> bool:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True
        return False
            