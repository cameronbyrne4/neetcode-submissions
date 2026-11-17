class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        Input: weights of packages in the order they are shipped
            * days we have to ship all weights

        Output: Minimum weight of the ship that will be able to ship all the packages in time

        We have to choose a proper ship_weight val
        Either start huge (the sum of all weights) for 1 day and decrement? or do a little bin search
        '''

        def canShip(capacity):
            # helper function that determines if the current ship weight can can successfully ship
            # if valid, go left
            # if invalid, go right
            days_used = 0   # compare to says
            cur_day = 0
            for w in weights:
                # print(f"w,cap, day used, curday = {w}, {capacity}, {days_used}, {cur_day}")
                if w > capacity:
                    # edge case -> weight never fits
                    return False
                if cur_day + w > capacity:
                    # move to next ship
                    days_used += 1
                    cur_day = w
                else:
                    # works
                    cur_day += w
                    # days doesnt change
            if cur_day > 0:
                days_used += 1
            
            # Final check
            if days_used > days:
                return False
            else:
                return True

            # at the end, cur_day might still have some in it
        max_weight = sum(weights)
        l,r = 0, max_weight
        
        while l <= r:
            m = (l+r)//2
            # print(f"m={m}, canShip = {canShip(m)}")
            if canShip(m):
                r = m-1
            else:
                l = m+1
        return l # updated last on proper ship








