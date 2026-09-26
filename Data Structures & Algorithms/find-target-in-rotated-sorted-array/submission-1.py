class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Step 1: figure out which half is normally sorted
            if nums[l] <= nums[mid]:
                # left half [l, mid] is sorted
                
                # Step 2: is target inside that sorted range?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right half [mid, r] must be sorted instead
                
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1