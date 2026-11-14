class TimeMap:
    '''
    dict where we just have (t, val) as the stored items in a list? will be in order already
    '''
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        # look within d[key] using binary search or whatever man
        # go left once we realize we cant find the exact time
        
        # Error case: return "" if there are no prev
        if not self.d[key] or timestamp < self.d[key][0][0]:
            return ""
        
        l,r = 0, len(self.d[key])-1

        while l <= r:
            m = (l+r) // 2
            #print(m)
            time_m, val_m = self.d[key][m]
            if time_m == timestamp:
                return val_m
            
            elif time_m < timestamp: # --> move right
                l = m+1
            else:   #move left if time_m too big
                r = m-1
        
        # final return once r < l and we didnt find it :(
        return self.d[key][min(l,r)][1]
        
