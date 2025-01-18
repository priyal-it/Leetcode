'''
******************************************************************************************
3. Longest Common Prefix
******************************************************************************************
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n=len(strs)
        prefix=strs[0]
        for i in range (1,n):
            while not strs[i].startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix