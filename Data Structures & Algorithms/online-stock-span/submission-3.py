class StockSpanner:
    '''
    - Add new element with each next call.
    - order matters (no heap)

    Data Structure:
         -array/stack/queue?
         O(n^2) worst case to set up an increasing stock chart
         prefix / suffix?

    Solution: stack that is always decreasing
        ( val, count)
        # count is how many it squashed to get placed
    '''
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1

        # squash smaller ones, consuming their counts
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price,count))
        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)