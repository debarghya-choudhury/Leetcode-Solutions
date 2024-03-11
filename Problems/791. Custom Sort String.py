class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = {}
        count = 1
        for i in order:
            orderMap[i] = count
            count += 1
        # print(orderMap)

        arr = []
        for i in s:
            arr.append(i)
            if i not in orderMap:
                orderMap[i] = 0

        arr.sort(key=lambda x: orderMap[x])
        ans = ("").join(arr)
        # print(arr)
        return ans