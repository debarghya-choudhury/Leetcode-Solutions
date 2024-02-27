class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []          # Without using any array methods like append() or pop()
        sum = 0
        for i in range(0, len(ops)):
            if ops[i] == "+":
                records = records + [int(records[len(records) - 1]) + int(records[len(records) - 2])]
            elif ops[i] == "D":
                records = records + [int(records[len(records)- 1])*2]
            elif ops[i] == "C":
                records = records[0:-1]
            else:
                records = records + [int(ops[i])]   
        print(records)
        for i in range(0, len(records)):
            sum += records[i]

        return sum    
