class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        # Find all permutations
        output = []
        if digits == "":
            return output

        def backtrack(i, cur_str):
            if i == len(digits):
                output.append(cur_str)  # dont need to copy because we are doing a string and not a list
                                        # does take more space tho!
                return
            
            for c in letters[int(digits[i])]:
                # Backtrack try adding each one to the current string
                
                backtrack(i+1, cur_str + c)

        backtrack(0, '')
        return output