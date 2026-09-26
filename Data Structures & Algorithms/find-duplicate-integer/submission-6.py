class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        slow2 = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                while slow2 != slow:
                    slow2 = nums[slow2]
                    slow = nums[slow]
                return slow2