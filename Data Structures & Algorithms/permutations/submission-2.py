class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        def backtrack(value, curr):
            if not nums :
                    res.append(curr)
                    return
            for j in range(len(nums)):    
                curr.append(nums[j])
                value = nums.pop(j)
                backtrack(value, curr[:])
                curr.pop()
                nums.insert(j, value)
        backtrack(0, curr)
        return res
