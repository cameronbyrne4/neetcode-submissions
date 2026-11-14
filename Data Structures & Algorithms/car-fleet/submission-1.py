class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        We can
        -- A: start with a count of n, then reduce every time a car catches up to another car
        -- B: start with a count of 0, and ++ per group of car counted somehow

        Car speed by the end depends on what's in front

        if a car BEHIND a car is the same speed or slower, we know it wont catch up

        buffer to 'catch up' grows every time a new car catches up


        STEPS:
        -- make pairs then sort by position
        -- calculate time for each car to reach target
         (target - position) // speed  **ROUND UP**
        -- see if the second car reaches same tie o

        SOLUTION
        -- each element of the stack is a fleet
        '''

        n = len(position)
        res = n

        cars = [] # pairs [pos, speed, time to arrival]
        # Create pairs from the two arrays and sort it
        for i in range(n):
            cars.append([position[i], speed[i], ((target-position[i])/speed[i])])
        cars.sort(key=lambda x : x[0]) # , reverse = True

        # GO IN REVERSE ORDER
        # stack = [] # each value is when the slowest part of the fleet will arrive
        for i in range(len(cars)-1,0,-1):
            # if this car is arriving at the same time or slower than the car before it.
            # -- decrement res
            # -- change the arrival time of the car before it to the slower one

            if cars[i][2] >= cars[i-1][2]:
                res -= 1
                cars[i-1][2] = cars[i][2]

        return res