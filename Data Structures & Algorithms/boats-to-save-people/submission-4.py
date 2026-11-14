class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Need to sort then 2 pointer
        Trying to pair ppl up
        Take heaviest person, then pair them up with the heaviest that won't tip it?
        or just give them the lightest dude
        '''
        people.sort()
        n = len(people)
        l,r = 0, n-1
        boats = 0
        while l <= r:
            print("comparing", people[l], people[r], "at", l, r)
            # if l == r:  # last person
            #     boats += 1
            #     break
            if people[l] + people[r] > limit: # too heavy need own boat!            
                r -= 1
            else:
                l += 1
                r -= 1
            boats +=1
                

        return boats
    