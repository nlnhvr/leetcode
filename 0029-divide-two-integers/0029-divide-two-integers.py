class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1
        if divisor == 1:
            return dividend
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = 0 if (dividend < 0) ^ (divisor < 0) else 1
        divid = abs(dividend)
        divis = abs(divisor)
        ans = 0
        while divid >= divis:
            exp = 0
            while divid >= (divis << exp):
                exp += 1
            exp -= 1
            ans += (1<<exp)
            divid -= (divis << exp)
        if sign:
            return ans
        else:
            return -ans
