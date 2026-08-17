class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        row = [1]
        val = 1
        for c in range(1,rowIndex+1):
            val = val*(rowIndex-c+1) // c
            row.append(val)
        return row
        