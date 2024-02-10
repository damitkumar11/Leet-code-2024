class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Define the mapping of digits to letters
        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Helper function to generate combinations
        def backtrack(index, path):
            # If the path is of the same length as digits, add it to the result
            if index == len(digits):
                result.append(''.join(path))
                return

            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = digit_mapping[current_digit]

            # Iterate through the letters and recurse
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result
        
        