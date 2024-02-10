class Solution:
    def is_safe(self, row, col, grid):
        return(0<= row< len(grid) and
               0<= col< len(grid[0]) and
               grid[row][col] == 1)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_set = set()
        rotten = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotten.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_set.add((row, col))
        if rotten == [] and not fresh_set:
            return 0
        elif rotten == []:
            return -1
            
        valid_row = [-1, 0, 0, 1]
        valid_col = [0, -1, 1, 0]
        while(rotten):
            row, col, time = rotten.pop(0)
            for neigh in range(len(valid_row)):
                new_row = row+valid_row[neigh]
                new_col = col+valid_col[neigh]
                if(self.is_safe(new_row, new_col, grid)):
                    grid[new_row][new_col] = 2
                    rotten.append((new_row, new_col, time+1))
                    fresh_set.remove((new_row, new_col))
        return -1 if fresh_set else time
        