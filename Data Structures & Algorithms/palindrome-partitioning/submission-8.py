class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        '''
        def check(s) -> bool:   # true if s is a palindrom
            l,r = 0, len(s)-1
            while l<= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            # s is a list btw for better space

        # use backtracking to split up at all index...
        out = []
     
        
        def bt(i, cur_list, cur_str): # str add to lsit, list add to out
            if i == len(s)-1:   # assume cur_str already includes s[i]
                if not check(cur_str):
                    return  # invalid solution because the remaining cur_str doesnt work
                else:
                    cur_list.append(''.join(cur_str))
                    out.append(cur_list.copy())
                    cur_list.pop()
                return
            
            # If palindrome -> both partition and continue growing
            # If not -> keep growing

            # will ALWAYS grow,
            cur_str.append(s[i+1])
            bt(i+1, cur_list, cur_str)
            cur_str.pop()   # no need to check for index here because the bt() run on final 

            if len(cur_str)>0 and check(cur_str):
                # partition grows list but not str
                cur_list.append(''.join(cur_str))
                bt(i+1, cur_list, [s[i+1]])
                cur_list.pop()
            
            
        
        bt(0, [], [s[0]])
        return out
            
