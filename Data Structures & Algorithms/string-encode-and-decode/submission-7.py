class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        # join at end
        # just have length until you see "X" or whatever
        for s in strs:
            l = len(s)
            out.extend([str(l), "X", s])

        #print(out)
        return "".join(out)
    def decode(self, s: str) -> List[str]:
        # gotta look for numbers before X to know the length to go off of
        l,r = 0,0
        n = len(s)
        len_str = 0
        out = []
        # go until l == n
        while l < n:
            while s[r] != "X":
                r += 1
            len_str = int(s[l:r])
            out.append(s[r+1:r+1+len_str])
            l = r+1+len_str
            r = l
        return out

            