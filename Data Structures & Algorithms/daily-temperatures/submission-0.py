class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                popped_index = stack.pop()
                result[popped_index] = index - popped_index
            stack.append(index)
        return result
