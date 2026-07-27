class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m , n = len(matrix) , len(matrix[0])

        #check if 0 is there in the 0th col and row
        first_row_zero = False
        first_col_zero = False

        #check for rows
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        #check for colums
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        #using first col and row for marking which needs to be zero
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        #now just zero the marked column and rows
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        #now we zero first row 
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        
        #now similar thing for first column also
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0





       
        