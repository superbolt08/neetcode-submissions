class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        preprod = 1
        postprod = 1
        for i, num in enumerate(nums):
            prefix[i] = preprod
            preprod *= num
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postprod
            postprod *= nums[i]
        return [prefix[i] * postfix[i] for i in range(len(nums))]

         
        