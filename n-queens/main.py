class Solution(object):
    def __init__(self):
        # from left x, 360 degree, by clockwise
        self.direction=[[-1, 0], [-1, -1], [0, -1], [1, -1], 
                    [1, 0], [1, 1], [0, 1], [-1, 1]]


    def checkAvailLine(self, ni, nj, di, dj, board):
        row = len(board)
        col = len(board[0])

        if board[ni][nj] == 1:
            return False

        # i in row dimension and j in col dimension
        next_i = ni+di
        next_j = nj+dj

        if next_i < 0 or next_i >= row:
            return True
        
        if next_j < 0 or next_j >= col:
            return True
        
        return self.checkAvailLine(next_i, next_j, di, dj, board)

        
    def canSet(self, ni, nj, board):
        row = len(board)
        col = len(board[0])

        for idx, dir in enumerate(self.direction):
            # ni current pos in row direction
            # nj current pos in col direction

            di = dir[1]
            dj = dir[0]

            next_i = ni+di
            next_j = nj+dj

           
            if next_i < 0 or next_i >= row:
                continue

            if next_j < 0 or next_j >= col:
                continue

            # if nj == 2:
            #     print(ni, nj, idx, next_i, next_j)

            # i in row dimension and j in col dimension
            if not self.checkAvailLine(next_i, next_j, di, dj, board):
                # print("False", ni, nj, idx, next_i, next_j)
                return False

        return True

    # DP vertically
    def solveNQueensSingle(self, board, ori_i, set_j, outs):
        row = len(board)
        col = len(board[0])
        checkPlaced = False  # t

        if ori_i >= row:
            # if board[0][1] == 1 and board[1][4] == 1:
            #     print("yeay canSet", ori_i, board)
            outs.append(self.fromBoardToString(board))
            return True

        for j in range(0, col): # only iterate horizontally
            # if board[0][1] == 1 and board[1][4] == 1:
            #     print("canSet why", ori_i, j, board)

            if j in set_j:
                continue

            
            
            if self.canSet(ori_i, j, board):
                # if board[0][1] == 1 and board[1][4] == 1:
                #     print("canSet", ori_i, j, "True", board)
                checkPlaced = True
                board[ori_i][j] = 1
                set_j.add(j)
                if not self.solveNQueensSingle(board, ori_i + 1, set_j, outs):
                    board[ori_i][j] = 0
                    set_j.remove(j)
                    continue
                board[ori_i][j] = 0
                set_j.remove(j)
            # else:
            #     if board[0][1] == 1 and board[1][4] == 1:
            #         print("canSet", ori_i, j,"False", board)

        return checkPlaced



    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        outs = []

        for j in range(0, n):
            board = [[0] * n for _ in range(n)]
            board[0][j] = 1

            # print("--------------------------------")
            # print("solve", 0, j, board)
            # print("--------------------------------")

            self.solveNQueensSingle(board, 1, set([j]), outs)


        return outs


    def fromBoardToString(self, board):
        row = len(board)
        col = len(board[0])
        out = [''] * row

        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 1:
                    out[i] += 'Q'
                else:
                    out[i] += '.'
        return out


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(5))