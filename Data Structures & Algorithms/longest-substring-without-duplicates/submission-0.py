class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        max_count = 0
        left = 0
        right = 0
        while(right < len(s)): 
            if table.get(s[right]) is not None and table[s[right]] >= left:
                left = table[s[right]] + 1 
            table[s[right]] = right
            max_count = max(max_count, right - left + 1)
            right = right + 1
        return max_count