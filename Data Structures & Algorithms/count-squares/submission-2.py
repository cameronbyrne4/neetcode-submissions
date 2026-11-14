class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)      # tuple coords --> count

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.points[(x,y)] += 1
        return None

    def count(self, point: List[int]) -> int:
        # CHECK FOR DIAGONALS
        count = 0
        a,b = point[0], point[1]
        for (x,y), c in self.points.items():
            # check if a,b are diagonals... if yes look for the other 2
            cnt = 0
            if (x,y) != (a,b) and abs(x-a) == abs(y-b):
                # check if both diags exist and multiply the count above 1 for all 4
                if (x,b) in self.points and (a,y) in self.points:
                    cnt = 1 # one square exists
                    cnt *= self.points[(x,b)]
                    cnt *= self.points[(a,y)]
                    cnt *= self.points[(x,y)]
            count += cnt

        return count
