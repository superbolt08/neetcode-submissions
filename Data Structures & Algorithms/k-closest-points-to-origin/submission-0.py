class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}

        for i, point in enumerate(points):
            distances[i] = point[0] ** 2 + point[1] ** 2

        closest_indices = sorted(distances, key=distances.get)[:k]
        return [points[i] for i in closest_indices]