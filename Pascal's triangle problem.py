class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            result=[[1],[1,1]]
            for i in range(2, numRows):
                prev = result[-1]
                row = [1]
                for j in range(1, len(prev)):
                    row.append(prev[j] + prev[j - 1])
                row.append(1)
                result.append(row)
        return result
