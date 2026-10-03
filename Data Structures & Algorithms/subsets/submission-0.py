class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        hashmap = set()
        def backtrack(seq):

            key = tuple(sorted(seq))

            if key in hashmap:
                return

            hashmap.add(key)
            out.append(seq[:])
            for num in nums:
                if num in seq:
                    continue

                seq.append(num)
                backtrack(seq)
                seq.pop()

        backtrack([])
        return out
           