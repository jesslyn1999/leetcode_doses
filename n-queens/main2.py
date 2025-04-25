from typing import List
from itertools import permutations

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
         return [
            ["." * i + "Q" + "." * (n - i - 1) for i in p]
            for p in permutations(range(n))
            if len(set(i - j for i, j in enumerate(p))) == 
               len(set(i + j for i, j in enumerate(p))) == n
        ]
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))