'''
******************************************************************************************
2. Palindrome Number
******************************************************************************************
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_list=[]
        if(abs(x))==x:
            for j in range (len(str(abs(x)))):
                num_list.append(str(x)[j])
            for i in range(len(num_list)):
                if num_list[i]!=num_list[len(num_list)-1-i]:
                    return False
        else:
            return False
        return True