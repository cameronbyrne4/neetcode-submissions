class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        # adds to arr in order ex. 1,2,4,5 adding 3
        i = 0
        if len(self.arr) > 0:
            while i < len(self.arr) and num > self.arr[i]:
                i += 1
        self.arr.insert(i, num)

    def findMedian(self) -> float:
        '''
        l = 0
        r = len(self.arr)-1

        while l < r:
            l += 1
            r -= 1 
            # either end up switched or end up on the same one
            # same one:
        if l==r:
            return float(self.arr[l])
        # switched:
        return (float(self.arr[l]) + float(self.arr[r]))/2
        '''
        n = len(self.arr)
        if n % 2 == 1:
            return float(self.arr[n // 2])
        else:
            return (self.arr[n//2 - 1] + self.arr[n//2]) / 2
        