class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check for negative numbers and numbers ending with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_num = x

        # Reverse the second half of the number
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # Check for even and odd length palindromes
        return x == reversed_num or x == reversed_num // 10