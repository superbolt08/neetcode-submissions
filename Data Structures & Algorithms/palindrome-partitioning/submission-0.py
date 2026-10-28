class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        out = []

        def isPalindrome(string):
            if string == string[::-1]:
                return True
            return False

        def backtrack(start):
            if start == len(s):
                out.append(curr[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if isPalindrome(substring):
                    # 1. Add substring to curr
                    curr.append(substring)
                    # 2. Backtrack from end
                    backtrack(end)
                    # 3. Undo your choice
                    curr.pop()
        
        backtrack(0)
        return out
