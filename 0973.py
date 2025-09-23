class Solution(object):
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda coor : coor[0]**2 + coor[1]**2)
        return points[:k]