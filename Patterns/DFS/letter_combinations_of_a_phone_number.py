class Solution:
    def __init__(self):
        self.mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        result = []
        self.letterCombinationsHelper(digits, 0, [], result)
        return result
        
    def letterCombinationsHelper(self, digits, start, temp, result):
        if start == len(digits):
            result.append("".join(temp))
            return
        for c in self.mapping[int(digits[start])-2]:
            temp.append(c)
            self.letterCombinationsHelper(digits, start+1, temp, result)
            temp.pop()