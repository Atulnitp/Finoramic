class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        n = len(A)
        valid = 1
        for i in range(n):
            countCol = 0
            countRow = 0
            Rowset =set()
            Colset = set()
            for j in range(n):
                if A[j][i] != '.':
                    countCol += 1
                    Colset.add(A[j][i])
                if A[i][j] != '.':
                    countRow += 1
                    Rowset.add(A[i][j])
            if len(Rowset)!= countRow or len(Colset) != countCol:
                valid = 0
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                count = 0
                numset = set()
                for i in range(3):
                    for j in range(3):
                        if A[m+i][n+j] != '.':
                            count += 1
                            numset.add(A[m+i][n+j])
                if len(numset) != count:
                    valid = 0
        return valid
