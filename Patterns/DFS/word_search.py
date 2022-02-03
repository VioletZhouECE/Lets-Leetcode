"""
https://leetcode.com/problems/word-search/

Classic DFS - "exploring all the options"
In every recursive call, we check one letter

We need to mark a cell as visited:
1. Use a set (slower).
2. Mark the cell as visited and unmark it before returning from the recursive call (faster).

It's common to modify something to pass some information to the child recursive call and undo it before the function returns (so that it does not effect the other child recursive calls).

Time complexity: O(m*n*4^s)
We invoke searchWord() m*n times. Each recursive call does a constant amount of work, and we call 4 other recursive calls until we reach a depth of s (length of the word). So the total runtime is O(m*n*4^s).
Space complexity: O(s)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rInd in range(len(board)):
            for cInd in range(len(board[0])):
                if self.searchWord(word, 0, board, rInd, cInd):
                    return True
        return False
        
    def searchWord(self, word, start, board, row, col):
        #base case
        if start == len(word):
            return True
        #invalid row, col
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
            return False
        if word[start] != board[row][col]:
            return False
        board[row][col] = "#"
        #look in the 4 directions
        found = self.searchWord(word, start+1, board, row-1, col) \
                or self.searchWord(word, start+1, board, row, col-1) \
                or self.searchWord(word, start+1, board, row+1, col) \
                or self.searchWord(word, start+1, board, row, col+1)
        board[row][col] = word[start]
        return found
