"""
https://leetcode.com/problems/group-shifted-strings/

Keys: 
1. "Grouping things together" should remind you of hashMap lmao.
2. Same shifting sequence -> (ascii code differences) are the same.

hashMap: {(ascii code differences): [strings]}
example: {():["a","z"], (1,1): ["abc","bcd","xyz"], ...}

Time complexity: O(k) where k is the total number of characters
Space complexity: O(n)
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for str in strings:
            diffList = []
            for index in range(1,len(str)):
                diff = ord(str[index])-ord(str[index-1])
                diff = diff+26 if diff < 0 else diff
                diffList.append(diff)
            dict[tuple(diffList)].append(str)
            
        result = [tuple[1] for tuple in dict.items()]
        
        return result