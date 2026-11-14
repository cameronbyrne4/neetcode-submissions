class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        obviously there parenthesis must be:
        -- even
        -- same number of open to close
        -- first one is ( and last is )
        -- ** USE STACK TO VALIDATE **

        Cases:
        A - too many closing
        -- just knock off the next closing ones if the stack is empty
        B - too amy open
        -- mark down the indexes i guess and remove the last ones until there are even


        input: string with a bunch of parenthesis
        output: string with minimal parenthesis removed so that its still valid
        '''

        
        resultChar = []

        # Pass one, we manage a stack. Any excess closing P will be removed
        # if the stack is empty at the end, then we are done!
        # stack stores the index of the open parenthesis
        stack= []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(len(resultChar))
            elif s[i] == ')':
                # Case - this is extra **DONT APPEND**
                if not stack:
                    continue
                # Case - this is valid
                else:
                    stack.pop()
            resultChar.append(s[i])

        # shave off any excess
        while stack:
            resultChar.pop(stack.pop())
        return ''.join(resultChar)

        