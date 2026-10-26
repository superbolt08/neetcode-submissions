class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ins = sorted(nums)
        out = []
        curr = []
        def backtrack(i):
            if curr not in out:
                out.append(curr[:])
            for j in range(i, len(nums)):
                    # 3. Pruning: Check if the choice is valid under the problem's constraints
                if j > i and ins[j] == ins[j - 1]:
                    continue

                curr.append(ins[j])
                backtrack(j+1)
                curr.pop()
        backtrack(0)
        return out