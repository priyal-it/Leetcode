'''
******************************************************************************************
12. Plus One
******************************************************************************************
Easy: You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
class Solution(object):
    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k=len(digits)
        num=0
        new_arr=[]
        for digit in digits:
            num+=digit*(10**(k-1))
            k-=1
        num+=1
        a=str(num)
        for d in a:
            new_arr.append(int(d))
        return new_arr