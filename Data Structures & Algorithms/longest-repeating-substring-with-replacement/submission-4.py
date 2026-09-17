class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        left = 0
        max_count = 0
        max_length = 0
        
        for right in range(len(s)):
            right_char = s[right]
            
            char_counts[right_char] = char_counts.get(right_char, 0) + 1
            
            max_count = max(max_count, char_counts[right_char])
            
            window_len = right - left + 1
            
            if window_len - max_count > k:
                left_char = s[left]
                char_counts[left_char] -= 1
                left += 1 
            max_length = max(max_length, right - left + 1)
            
        return max_length