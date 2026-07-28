class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #make transposed matrix
        for i in range(0, n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        #now we reverse the transposed matrix
        for i in range(n):
            left , right = 0 ,n-1

            while left<right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1