class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        nums = [x for x in nums if x <= target]
        curr = []
        result = []
        def backtrack(i, curr):
            if sum(curr) == target:
                result.append(curr)  
                return
            

            # 2. Iterate through all available choices at the current step
            for j in range(i, len(nums)):
                    # 3. Pruning: Check if the choice is valid under the problem's constraints
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if sum(curr) + nums[j] > target:
                    break
                        
                # CHOOSE: Add the choice to the current state
                curr.append(nums[j])
                        
                # EXPLORE: Recurse deeper into the decision tree
                backtrack(j+1, curr[:])
                        
                # UNCHOOSE: Undo the choice (backtrack) to try the next alternative
                curr.pop() 
        backtrack(0,[])
        return result

