class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: binary search first column to find candidate row
        lo, hi = 0, m - 1
        row = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target:
                row = mid          # this row is a valid candidate
                lo = mid + 1       # keep looking further down for a better one
            else:
                hi = mid - 1       # first value too big, go up
        
        if row == -1:
            return False  # target is smaller than every row's first value
        
        # Step 2: binary search within that row
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False