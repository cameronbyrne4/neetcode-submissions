class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Backtracking needs a decision tree!
        - this is common when we are tryna find all combinations
        - should use a helper

        We can either add a '(' or a ')' until we have n*2 characters in the string
            - could check if valid at the end
            - could check if valid during formation


        '''
        result = []

        def isValid(path: str) -> bool:
            stack = []
            for p in path:
                if p == '(':
                    stack.append(1)
                if p == ')':
                    # bad if we add ) to an empty stack
                    if len(stack) < 1:
                        return False
                    # Bad if we add )
                    else:
                        stack.pop()
            # make sure no trailing (
            return not stack
        def backtrack(path):
            if len(path) == n * 2:
                # if valid, we add to our list
                if isValid(path):
                    result.append(path)
                return
            
            # Path 1: add open parenthesis
            path += '('
            backtrack(path)
            path = path[:-1]
            path += ')'
            backtrack(path)
            # Path 2: add close parenthesis
            
        backtrack("")
        return result

