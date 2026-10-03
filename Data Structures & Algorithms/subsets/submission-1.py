class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(i, seq):
            if i == len(nums):
                out.append(seq[:])
                return

            # don't include nums[i]
            backtrack(i + 1, seq)

            # include nums[i]
            seq.append(nums[i])
            backtrack(i + 1, seq)
            seq.pop()

        backtrack(0, [])
        return out
           