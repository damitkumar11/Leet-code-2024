class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle negative sign
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        # Reverse the digits
        reversed_x = int(str(x)[::-1]) * sign

        # Check for overflow
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0

        return reversed_x