"""
https://leetcode.com/problems/group-anagrams/

Keys:
1. Sorted anagrams are the same: this gives us a convenient way to compare them.
2. No need to "arrange and collect" the anagarams, use a hash table lol.

k characters
Time complexity: O(klogk), Space complexity: O(k)
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()