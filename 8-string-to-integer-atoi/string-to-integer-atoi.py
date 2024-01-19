class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Ignore leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for '+' or '-'
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Read in digits until a non-digit character is encountered
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1

        return result * sign