class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s): return ""

        count_t = Counter(t)
        required = len(count_t)

        window = {}
        seen = 0

        left = 0
        ans = (float("inf"),0,0)

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                seen += 1
            
            while left <= right and seen == required:
                char_left = s[left]

                if(right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window[char_left] -= 1
                if char_left in count_t and window[char_left] < count_t[char_left]:
                    seen -= 1
                
                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


