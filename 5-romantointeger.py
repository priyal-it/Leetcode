'''
******************************************************************************************
5. Roman to Integer
******************************************************************************************
Given a roman numeral, convert it to an integer.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev=0
        total=0
        roman_map={"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for char in reversed(s):
            current=roman_map[char]
            if prev>current:
                total-=current
            else:
                total+=current
            prev=current
        return total
