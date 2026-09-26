class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        cars = sorted(zip(position, speed), reverse=True)
        for position, speed in cars:
            time = (target-position) / speed
            if not times or time > times[-1]:
                times.append(time)
        return len(times)
