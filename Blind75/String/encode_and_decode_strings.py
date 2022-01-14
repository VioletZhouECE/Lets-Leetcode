"""
https://leetcode.com/problems/encode-and-decode-strings/

Run length encoding:
length (chr(len(s)) always occupy 1 char) + the original string
Notice that you can't just choose a random delimiter (what if that delimiter appears in some strings?)

Time complexity: O(k). Space complexity: O(1)
"""
    
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""
        for s in strs:
            encoded += chr(len(s))
            encoded += s
        return encoded
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            #read the length of the next string
            length = ord(s[i])
            i += 1
            strs.append(s[i:i+length])
            i += length
        return strs
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))