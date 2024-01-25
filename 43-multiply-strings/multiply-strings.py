class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        ans = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])
        for i in range(len(ans) - 1):
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        return "".join(str(i) for i in ans[::-1]).lstrip('0')
        