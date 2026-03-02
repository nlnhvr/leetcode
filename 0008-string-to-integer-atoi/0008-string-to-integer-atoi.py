class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        max = 2**31 - 1
        min = -2**31
        n = len(s)
        sign = 1

        if not s:
            return 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            
            if sign * num <= min:
                return min
            if sign * num >= max:
                return max
            
            i += 1
  
        return num * sign