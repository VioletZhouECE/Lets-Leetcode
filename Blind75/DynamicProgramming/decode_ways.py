"""
https://leetcode.com/problems/decode-ways/

Recurrence relation:
    numDecodingHelper(s, start, end) = numDecodingHelper(s, start, end-1) + numDecodingHelper(s, start, end-2)
    
DP:
Just one small thing:
Technically we should initialize both dp[0] and dp[1], but initializing dp[1] involves a bit of logic (and duplicate logic), so we do the work in the for loop (main logic). The caveat is that now we have to add if i<2: dp[i] += 1 to avoid index out of bound error.
Alternatively, we can make dp[i+1] = dp[i] so we don't need to avoid index out of bound, but that makes the code less intuitive imo.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        dp[0] = 1 if s[0] != "0" else 0
         
        for i in range(1,len(s)):
            if s[i] != "0":
                dp[i] += dp[i-1]
            if s[i-1] != "0" and 1 <= int(s[i-1:i+1]) <= 26:
                if i<2:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
            
        return dp[-1]