from typing import List


class Solution:
    # rules:
    # 1-9 once in each row
    # 1-9 once in each col
    # 1-9 once in each grid square

    # pos in format (y, x) or (row, col)

    def checkAvailHorizontal(self, inp_num, pos, board):
        i_row = pos[0]
        i_col = pos[1]

        if inp_num in board[i_row]:
            return False
        
        return True
        

    def checkAvailVertical(self, inp_num, pos, board):
        i_row = pos[0]
        i_col = pos[1]
        row = len(board)
        col = len(board[0])

        tmp_list = [board[i][i_col] for i in range(row)]

        if inp_num in tmp_list:
            return False

        return True


    def checkAvailSubBoxes(self, inp_num, pos, board):
        i_row = pos[0]
        i_col = pos[1]
        row = len(board)
        col = len(board[0])

        min_i_row = i_row // 3
        min_i_col = i_col // 3

        tmp_list = [board[i][j] for i in range(min_i_row, min_i_row+3) \
                    for j in range(min_i_col, min_i_col+3)]

        if inp_num in tmp_list:
            return False

        return True
    
    def removeNegatives(self, nums: List[int]) -> List[int]:
        return list(filter((-1).__ne__, nums))

    def getNumsHorizontal(self, pos, board: List[List[int]]) -> List[int]:
        return self.removeNegatives(board[pos[0]])
    
    def getNumsVertical(self, pos, board: List[List[int]]) -> List[int]:
        return self.removeNegatives([board[i][pos[1]] for i in range(len(board))])
    
    def getNumsSubBoxes(self, pos, board: List[List[int]]) -> List[int]:
        return self.removeNegatives(
            [board[i][j] for i in range(pos[0]//3 * 3, pos[0]//3 * 3 + 3) 
             for j in range(pos[1]//3 * 3, pos[1]//3 * 3 + 3)])
    
    def getAvailNums(self, nums_occ: List[int]) -> List[int]:
        avail_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return list(set(avail_nums) - set(nums_occ))
    

    def findBestPos(self, board: List[List[str]]):
        # Greedy approach: find the pos with the least number of avail nums and the highest similarity

        threshold = 3

        # horizontal
        total_nums_avails_horizontal = [self.getAvailNums(self.getNumsHorizontal((i, 0), board)) for i in range(len(board))]
        total_nums_avails_vertical = [self.getAvailNums(self.getNumsVertical((0, i), board)) for i in range(len(board[0]))]
        total_nums_avails_sub_boxes = [
            self.getAvailNums(self.getNumsSubBoxes((i, j), board)) 
            for i in range(0,len(board), 3) for j in range(0,len(board[0]), 3)]


        n_total_nums_avails = [len(nums_avail) for nums_avail in total_nums_avails_horizontal]
        if sum(n_total_nums_avails) == 0:
            return (-1, -1), [], True
        
        out_pos = (-1, -1)
        out_avail_nums = range(10)
        for i in range(len(board) * len(board[0])):
            idx_hor = i // len(board)
            idx_vert = i % len(board[0])

            if board[idx_hor][idx_vert] != -1:
                continue

            idx_sub_box = (idx_hor // 3) * 3 + (idx_vert // 3)

            def empty_then_all(nums: List[int]):
                return range(9) if len(nums) == 0 else nums

            common_set = set(empty_then_all(total_nums_avails_horizontal[idx_hor])).intersection(
                    set(empty_then_all(total_nums_avails_vertical[idx_vert])).intersection(
                    set(empty_then_all(total_nums_avails_sub_boxes[idx_sub_box]))))
            common_set = list(common_set)

            if len(common_set) < len(out_avail_nums):
                out_pos = (idx_hor, idx_vert)
                out_avail_nums = common_set

            if len(common_set) <= 2:
                break

        return out_pos, out_avail_nums, False

    
    def solveSudokuSingle(self, board: List[List[str]]):
        pos, avail_nums,is_done = self.findBestPos(board)

        if is_done:
            return True
        
        # avail_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # nums_horizontal = self.getNumsHorizontal(pos, board)
        # nums_vertical = self.getNumsVertical(pos, board)
        # nums_sub_boxes = self.getNumsSubBoxes(pos, board)
        # avail_nums = list(set(avail_nums) - set(nums_horizontal) - set(nums_vertical) - set(nums_sub_boxes))

        # if len(avail_nums) == 0:
        #     return False

        # Assume that the first step of there must be a solution of avail_num
        for avail_num in avail_nums:
            board[pos[0]][pos[1]] = avail_num

            if not self.solveSudokuSingle(board):
                board[pos[0]][pos[1]] = -1
            else:
                return True
    
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.formatBoardToNumBoard(board)
        self.solveSudokuSingle(board)
        self.formatNumBoardToBoard(board)

    def formatBoardToNumBoard(self, board: List[List[str]]) -> List[List[int]]:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    board[i][j] = -1
                else:
                    board[i][j] = int(board[i][j])
    
    def formatNumBoardToBoard(self, board: List[List[int]]) -> List[List[str]]:
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = str(board[i][j])


if __name__ == "__main__":
    sol = Solution()
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # sol.solveSudoku(board)
    # print(board)

    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    sol.solveSudoku(board)
    print(board)