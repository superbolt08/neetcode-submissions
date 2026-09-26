class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            complement = target - v
            if complement in nums:
                j = nums.index(complement)
                if i != j:
                    return sorted([i, j])