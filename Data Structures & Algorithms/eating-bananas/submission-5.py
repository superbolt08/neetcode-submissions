class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2      
            hoursNeeded = 0

            for pile in piles:
                hoursNeeded = hoursNeeded + math.ceil(pile / mid)   

            if hoursNeeded <= h:
                hi = mid          
            else:
                lo = mid + 1     

        return lo

