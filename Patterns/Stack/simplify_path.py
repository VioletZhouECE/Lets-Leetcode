"""
https://leetcode.com/problems/simplify-path/

I think the important thing is to realize that you can split the array by / so you can focus on the components within /
Use a stack becuase we wanna pop from stack when we see ..

Time complexity: O(n). Space complexity: O(n)
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        
        for p in paths:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)