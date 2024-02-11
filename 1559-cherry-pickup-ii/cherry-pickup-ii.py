import functools
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(row: int, col1: int, col2: int) -> int:
            if row == m: return 0
            curr = grid[row][col1]
            if col1 != col2: curr += grid[row][col2]
            result = 0
            for c1 in range(col1 - 1, col1 + 2):
                for c2 in range(col2 - 1, col2 + 2):
                    if 0 <= c1 < n and 0 <= c2 < n:
                        result = max(result, dfs(row + 1, c1, c2))
            return result + curr

        m, n = map(len, (grid, grid[0]))
        return dfs(0, 0, n - 1)
        