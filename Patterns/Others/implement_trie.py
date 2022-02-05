"""
https://leetcode.com/problems/implement-trie-prefix-tree/

Applications: 
1. prefix search (autocomplete/spellcheck).
2. search for all the matching words simultaneously (word search II).
3. string matching (reuse src text).
   Trie construction takes O(m^2) - a string of length m has m prefixes and m^2 chars in total.
   
Runtime:
Trie construction - O(m) where m is the number of chars in the src text.
Usually trie construction is the most expensive operation.
Insert, search - O(s) where s is the number of chars in the target text.

TL'DR: Trie provides an efficient way to search in a set of words, but the construction might be slow & has space overhead. 
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)