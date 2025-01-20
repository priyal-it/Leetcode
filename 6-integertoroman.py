'''
******************************************************************************************
6. Integer to Roman
******************************************************************************************
Given an integer, convert it to a Roman numeral.

'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_map={1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman=""
        for key in sorted(roman_map.keys(), reverse=True):
            while num>=key:
                roman+=roman_map[key]
                num-=key
        return roman