from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        referred =  grid[row][col]
        visited_grid = [[False for _ in grid[0]] for _ in grid]

        def backtrack(pos):
            if pos[0] < 0 or  pos[0] >= len(grid) or \
                pos[1] < 0 or pos[1] >= len(grid[0]):
                return True
            
            if visited_grid[pos[0]][pos[1]]:
                return False  # False: means flooded area
                
            if grid[pos[0]][pos[1]] != referred:
                return True  # True: means reach the border
            
            # grid[pos[0]][pos[1]] = visited
            visited_grid[pos[0]][pos[1]] = True

            anyBorder = [
                backtrack((pos[0], pos[1] - 1)),
                backtrack((pos[0] - 1, pos[1])),
                backtrack((pos[0], pos[1] + 1)),
                backtrack((pos[0] + 1, pos[1]))
            ]
            if any(anyBorder):
                grid[pos[0]][pos[1]] = color
            
            return False

        backtrack((row, col))
        return grid



if __name__ == "__main__":
    sol = Solution()
    # grid= [[1,1],[1,2]]
    # row = 0
    # col = 0
    # color = 3
    # grid = sol.colorBorder(grid, row, col, color)
    # print(grid)
    # print()

    # grid= [[1,2,2],[2,3,2]]
    # row = 0
    # col = 1
    # color = 3
    # grid = sol.colorBorder(grid, row, col, color)
    # print(grid)
    # print()

    grid= [[1,1,1],[1,1,1],[1,1,1]]
    row = 1
    col = 1
    color = 2
    grid = sol.colorBorder(grid, row, col, color)
    print(grid)
    print()

    grid= [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]]
    row = 1
    col = 3
    color = 1
    grid = sol.colorBorder(grid, row, col, color)
    print(grid)
    print()