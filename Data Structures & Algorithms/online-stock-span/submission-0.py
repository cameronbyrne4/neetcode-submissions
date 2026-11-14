class StockSpanner:
    '''
    I'm not tryna use a stack??
    Can we just use an array
    '''
    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        '''
        returns the span
        '''
        self.arr.append(price)
        s = 1
        n = len(self.arr) # will be at least one
        i = n-2
        while i > -1 and self.arr[i] <= price:
            s += 1
            i -=1


        return s


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)