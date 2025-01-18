'''
******************************************************************************************
4. Length of Last Word
******************************************************************************************
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        i=n-1
        length=0
        while i>=0 and s[i]==" ":
                i-=1
        while i>=0 and s[i]!=" ":
                i-=1
                length+=1
        return length