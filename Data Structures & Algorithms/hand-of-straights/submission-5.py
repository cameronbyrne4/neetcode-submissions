from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        Every group of consecutive numbers is length divisible by groupsize
        DUPES CAN HAPPEN

        Is there a way that doesnt use space?
        '''
        if len(hand) % groupSize != 0:
            return False
        hand = Counter(hand)
        starters = deque() # stores which numbers we want to start counting from

        for k,v in hand.items():
            if (k-1 not in hand) or (hand[k-1] < hand[k]):
                starters.append(k)
            
        
        print(hand)
        print(starters)
        while starters:    # go until we modulo by groupsize. need to start from it v times?
            k = starters.popleft()
            
            for i in range(1, groupSize):
                print("K,i = ", k, i, ", Checking for K+i = ", k+i)
                if k+i not in hand:
                    return False
                print("Checks for new starter: ", i, "==", groupSize-1)
                print(k+i+1, "in hand")
                print(hand[k+i])
                if i == groupSize-1 and k+i+1 in hand and hand[k+i] == hand[k+i+1]:
                    print("appending new starter: ", k+i+1)
                    starters.append(k+i+1)
                hand[k+i] -= 1
                if hand[k+i] == 0:
                    del hand[k+i]

        
        
        return True

            
