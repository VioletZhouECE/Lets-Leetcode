"""
https://leetcode.com/problems/word-search-ii/

1. For each word, do a DFS search on the board.
2. Do DFS search on the board and see which words the current search could match. Stop if there is no possible match.
Note: we need to use a set to eliminate duplicates (a word could be constructed in more than one way).

How to quickly identify which words the current search could match? A trie!
Time complexity: O(m*n*4^s). Essentially the same as Word Search. 
Trie insertion: O(s) where s is the total number of characters in all the words.

This is the correct algo but it gets TLE :(

Trie implementation:
Children is a set of dictionary of {char: charNode}
"""
class TrieNode:
    def __init__(self):
        #children is a set of dictionary of {char: charNode}
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        if node.endOfWord:
            return True
        return False
                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)
        result = set()
        for rInd in range(len(board)):
            for cInd in range(len(board[0])):
                self.dfs(board, root, rInd, cInd, result, "")
        return list(result)
    
    def dfs(self, board, node, row, col, result, word):
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
            return
        if board[row][col] not in node.children:
            return
        currChar = board[row][col]
        childNode = node.children[currChar]
        if childNode.endOfWord:
            result.add(word+currChar)
        board[row][col] = "#"
        self.dfs(board, childNode, row+1, col, result, word+currChar)
        self.dfs(board, childNode, row, col+1, result, word+currChar)
        self.dfs(board, childNode, row-1, col, result, word+currChar)
        self.dfs(board, childNode, row, col-1, result, word+currChar)
        board[row][col] = currChar