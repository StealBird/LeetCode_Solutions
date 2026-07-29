class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def genrateRows(numRows):
            triangle = []

            for i in range(0,numRows):
                triangle.append(getRow(i))
            return triangle
        def getRow(rowIndex):
            ans = 1
            result = [ans]

            for i in range(1,rowIndex+1):
                ans = ans*(rowIndex+1-i)//i
                result.append(ans)
            return result
        return genrateRows(numRows)

        