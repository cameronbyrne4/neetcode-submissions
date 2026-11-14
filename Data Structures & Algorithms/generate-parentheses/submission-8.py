class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Idea 1: generate all string of len 2n and then verify if it works

        Goes up to 7
        2^14 possibilities

        But how can we do it with dp? must prune
        
        Strings are invalid if there are more ) than ( at any point in time (can just track with an int)

        Don't need to verify because all will be correct at the end
        '''
        output = []
        def bt(length, ratio, cur_list):
            if length == 2 * n:
                if ratio == 0:
                    output.append(''.join(cur_list))    # do we need to do a copy?
                return
            if ratio < 0: 
                return # error invalid no matter what
            
            cur_list.append("(")
            bt(length+1, ratio+1, cur_list) # case -> add another open
            cur_list.pop()
            cur_list.append(")")
            bt(length+1, ratio-1, cur_list)
            cur_list.pop()
        

        bt(1,1,["("])
        return output