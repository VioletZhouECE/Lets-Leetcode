"""
https://leetcode.com/problems/partition-labels/

Okay this is the Bloomberg interview question I bombed...get it on my birthday :)

We need to do this in 2 passes:
It's important to realize that we need to store {char: the index it is last seen}
In my interview I was thinking of doing everything in one pass and that didn't work out :(
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for i, c in enumerate(s):
            lastSeen[c] = i
        curr, start, end = 0, 0, 0
        res = []
        while curr < len(s):
            end = max(end, lastSeen[s[curr]])
            if curr == end:
                res.append(end-start+1)
                end += 1
                start = end
            curr += 1
        return res