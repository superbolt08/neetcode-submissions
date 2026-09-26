class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                # target is in the LEFT half — move right boundary
                right = mid - 1 
            else:
                # target is in the RIGHT half — move left boundary
                left = mid + 1
        return -1