class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''

        '''
        res = []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i, curstring):
            if len(curstring) == len(digits):
                res.append(curstring)
                return
            for letter in phone_map[digits[i]]:
                
                backtrack(i+1, curstring + letter)
                
            # either adding it or its siblings, so start a loop

        backtrack(0,'')
        if not digits: return []
        return res
