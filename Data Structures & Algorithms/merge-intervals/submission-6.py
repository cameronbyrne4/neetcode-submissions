class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []
        n = len(intervals)
        i = 0 
        # always less than n as an index


        # add first one's start
        self.front = intervals[0][0]
        self.back = intervals[0][1]
        # for all the others... 
        for i in range(1,n):
            print("i is ", i)
            # Head < old tail
            if intervals[i][0] <= self.back:
                print('loop 1')
                self.back = max(intervals[i][1], self.back)
                print("front back is: ", self.front, self.back)
            else:
                print('else')
                res.append([self.front,self.back])
                self.front = intervals[i][0]
                self.back = intervals[i][1]
        res.append([self.front,self.back])
        return res
# IF the head is overlapping, we adjust the tail to be the max

# if the head is NOT overlapping, we add the old one to res and restart with a new front