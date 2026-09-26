class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # frequency of each character in current window
        maxfreq = 0          # count of the most frequent char in window so far
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])

            window_size = right - left + 1
            if window_size - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
