class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)
        return

    def pop(self) -> int:
        if not self.front:
            while self.back:
                x = self.back.pop()
                self.front.append(x)

        x = self.front.pop()
        return x
            

    def peek(self) -> int:
        '''
        if not self.back:
            while self.front:
                x = self.front.pop()
                self.back.append(x)
        return self.back[-1]
        '''
        if self.front:
            return self.front[-1]
        else:
            return self.back[0]

    def empty(self) -> bool:
        if not self.front and not self.back:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()