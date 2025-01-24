'''
******************************************************************************************
11. Find the Index of the First Occurence in a String
******************************************************************************************
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return -1
        
        for i in range (len(haystack)):
            if haystack.startswith(needle):
                return i
            else:
                haystack=haystack[1:]
        return -1
       