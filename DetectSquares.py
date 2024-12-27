class DetectSquares:
    def __init__(self):
        self.cord_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.cord_count[tuple(point)] +=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.pts:
            if (abs(qx - x) != abs(qy - y)) or qx == x or qy == y :
                continue
            res += self.cord_count[(qx, y)] * self.cord_count[(x, qy)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)