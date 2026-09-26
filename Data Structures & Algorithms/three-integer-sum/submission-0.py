class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 1
        right = len(nums) -1
        answers = []
        nums.sort()
        for index, num  in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current_sum = num + nums[left] + nums[right]
                if current_sum == 0:
                    answers.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1  # Sum is too small, move right to get a larger number
                else:
                    right -= 1 # Sum is too large, move left to get a smaller number
                    
        return answers