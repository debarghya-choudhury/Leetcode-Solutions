class Solution:
    def reformatDate(self, date: str) -> str:
        monArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monMap = {monArr[i]: str(i+1) for i in range(len(monArr))}

        modDate = date.split(" ")

        day = modDate[0][:2] if len(modDate[0]) == 4 else "0" + modDate[0][:1]
        mon = monMap[modDate[1]] if len(monMap[modDate[1]]) == 2 else "0" + monMap[modDate[1]]
        year = modDate[2]

        return year + "-" + mon + "-" + day