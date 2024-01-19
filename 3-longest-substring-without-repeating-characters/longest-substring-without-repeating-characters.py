class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a dictionary to store the last index of each character
        char_index = {}
        # Initialize pointers for the sliding window
        left = 0
        right = 0
        # Initialize the maximum length of the substring
        max_length = 0

        # Iterate through the string with the sliding window
        while right < len(s):
            # If the character at the right pointer is not in the current substring
            if s[right] not in char_index or char_index[s[right]] < left:
                # Update the last index of the character
                char_index[s[right]] = right
                # Update the maximum length of the substring
                max_length = max(max_length, right - left + 1)
                # Move the right pointer to the next character
                right += 1
            else:
                # Move the left pointer to the right of the last occurrence of the character
                left = char_index[s[right]] + 1

        # Return the maximum length of the substring
        return max_length
