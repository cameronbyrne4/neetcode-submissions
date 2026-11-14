class StockSpanner:
    '''
    I'm not tryna use a stack??
    Can we just use an array
    '''
    def __init__(self):
        self.stack = []           # stack as pairs (price,span)

    def next(self, price: int) -> int:
        '''
        if price is equal or larger than the top of the stack, we replace the 
        top of the stack with the new price, incrementing the span on that onE
            -- DO THIS ON A LOOP

        otherwise just add a new thing to the stack
        
        return the second element of the top of the stack
        '''
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()


        self.stack.append((price,span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)