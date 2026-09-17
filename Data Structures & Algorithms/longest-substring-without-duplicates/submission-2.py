class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        string = ''

        for char in s:
            if char not in string:
                string += char
                count = max(count, len(string))
            else:
                string = string[string.index(char) + 1:] + char
        return count