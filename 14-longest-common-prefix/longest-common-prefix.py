class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Sort the strings to find the common prefix
        strs.sort()

        # Consider the first and last strings after sorting
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = []
        
        # Iterate through the characters of the first string
        for i in range(len(first_str)):
            # If the character is the same in the last string, add it to the common prefix
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                # If characters are different, break the loop
                break

        return "".join(common_prefix)
        