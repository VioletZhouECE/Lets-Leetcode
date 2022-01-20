"""
Ugh I hate this one :(

https://leetcode.com/problems/exclusive-time-of-functions/

Keys:
1. we need to use a stack to keep track of the current function which is being executed.
2. we need to store the previous timestamp - this information allows us to compute the time elapsed.
The big idea is to add each time interval(timestamp-prev) to the "correct" function id:
    start - add it to the "previous" function (aka the function that comes before start)
    end - add it to the current function
we need these information from the stack.
    
There are some tricky +1/-1 in this question. Make sure you test it on an example.

Time complexity: O(n). Space complexity: O(n)
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0]*n
        stack = []
        prev = 0
        
        for log in logs:
            logData = log.split(":")
            funcID, flag, timestamp = int(logData[0]), logData[1], int(logData[2])
            if flag == "start":
                #notice that this is not timestamp-prev+1
                if stack: result[stack[-1]] += timestamp-prev
                prev = timestamp
                stack.append(funcID)
            else:
                result[stack[-1]] += timestamp-prev+1
                #notice that this is timestamp+1
                prev = timestamp+1
                stack.pop()
        
        return result