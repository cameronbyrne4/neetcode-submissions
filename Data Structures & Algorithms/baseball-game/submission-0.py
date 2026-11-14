class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        # all ops are valid!
        # we can optimize space by having 3 points total
        for o in operations:
            if o == "C":    # Assume not empty
                record.pop()
            elif o == "D":  # Assume at least one prev score (not 2)
                record.append(record[-1]*2)
            elif o == "+":  # Assume there exists 2 prev scores
                a,b = record[-1], record[-2]
                record.append(a+b)
            else:
                record.append(int(o))

        return sum(record) if record else  0