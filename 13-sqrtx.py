'''
******************************************************************************************
13. Sqrt(x)
******************************************************************************************
Easy: Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        n=math.sqrt(x)
        n=int(n)
        return n