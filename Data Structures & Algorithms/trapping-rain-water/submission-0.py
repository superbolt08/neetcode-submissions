class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        prefix, suffix, water = [], [], []
        max_height = 0
        for num in height:
            max_height = max(max_height, num)
            prefix.append(max_height)
        
        max_height = 0
        for num in reversed(height):
            max_height = max(max_height, num)
            suffix.append(max_height)
        suffix.reverse()

        return sum(min(prefix[i], suffix[i]) - height[i] for i in range(len(height)))

