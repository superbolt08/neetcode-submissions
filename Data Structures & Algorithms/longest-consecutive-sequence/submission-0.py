class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons = set(nums)
        max_count = 0
        count = 0
        for num in nums:
            if((num -1) not in cons):
                count = 0
                i = num
                while(True):
                    if(i in cons):
                        count = count + 1
                        i = i + 1
                    else:
                        if count > max_count:
                            max_count = count
                        break
                
        return max_count

