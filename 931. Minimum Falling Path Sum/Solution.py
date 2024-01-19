class Solution:
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)

        # Iterate through the matrix starting from the second row
        for i in range(1, n):
            for j in range(n):
                # Update the current element by adding the minimum of the three choices
                matrix[i][j] += min(
                    matrix[i - 1][j],
                    matrix[i - 1][max(0, j - 1)],
                    matrix[i - 1][min(n - 1, j + 1)]
                )

        # Return the minimum value in the last row
        return min(matrix[-1])
