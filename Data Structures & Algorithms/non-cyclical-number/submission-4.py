class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        * hash set stores the sums we'd already hit
        * return false if sum is repeated
        * return true if sum is 1
        * otherwise add sum to hash set and iterate over it's digits recursively
        '''
        seen = set()

        def helper(m):
            # calculate sum
            curSum = 0
            print("running helper on ", m)
            for i in range(len(str(m))):
                digit = int(str(m)[i])
                print(digit)
                curSum += pow(digit, 2)
            
            # check if repeated
            if curSum in seen:
                return False
            
            # check if done
            if curSum == 1:
                return True

            # Other wise keep looping
            seen.add(curSum)
            return helper(curSum)

        return True if helper(n) else False
