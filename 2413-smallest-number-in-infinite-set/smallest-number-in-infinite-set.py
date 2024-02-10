class SmallestInfiniteSet:
    def __init__(self):
        self.black = set()

    def popSmallest(self) -> int:
        i = 1
        while i in self.black:
            i += 1
        self.black.add(i)
        return i

    def addBack(self, num: int) -> None:
        self.black.discard(num)

class SmallestInfiniteSet:

    def __init__(self):
        self.A = [True] * (1001)
        self.index = 1

    def popSmallest(self) -> int:
        res = 0
        
        for i in range(1, len(self.A)):
            if self.A[i]:
                res = i
                self.A[i] = False
                break
        
        return res

    def addBack(self, num: int) -> None:
        self.A[num] = True
