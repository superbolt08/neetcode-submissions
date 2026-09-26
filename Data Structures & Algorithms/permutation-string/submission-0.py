class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        window = [0] * 26
        for ch in s2[0:len(s1)]:
            window[ord(ch) - ord('a')] += 1

        if window == need:
            return True
        for start in range(1, len(s2) - len(s1) + 1):
            end = start + len(s1) - 1
            outgoing_char = s2[start - 1]
            incoming_char = s2[end]
            window[ord(outgoing_char) - ord('a')] -= 1
            window[ord(incoming_char) - ord('a')] += 1

            if window == need:
                return True
        return False

# declare hash table pointers, array of all characters
# return false if s1 > s2
# count charaters 
