class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #legend for all roman values

        integer = 0 #int for total sum
        s.upper() #convert to fit legend
        for i in range(len(s)):
            current = roman_map[s[i]]

            if i + 1 < len(s) and current < roman_map[s[i+1]]:
                integer -= current
            else:
                integer += current
        return integer



    