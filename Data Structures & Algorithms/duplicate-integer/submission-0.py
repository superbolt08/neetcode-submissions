class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for value in nums:
            if not map.get(value):
                map[value] = 1
            else:
                return True
        return False
