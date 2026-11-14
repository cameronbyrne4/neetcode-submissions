class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        makes sense to start from the largest string possible (len of the smaller str)

        At each length:
            * see if the len perfectly divides each string
            * use len to concat on itself iteratively and see if that == the str

        Answer is the first one that works
        '''
        if len(str2) < len(str1):
            str1, str2 = str2, str1

        # Str 1 will be shorter
        # we start with the entire length of str 1
        m, n = len(str1), len(str2)

        for i in range(m, 0, -1):   # i represents the length that we have
            print(f"checking i={i}")
            # check length is valid
            # check characters are the same
            if m % i != 0 or n % i != 0:
                print("invalid")
                continue
            
            # assume m and n can validly be filled by the length
            cur = str1[:i]
            print(cur)
            print(m//i * cur, n//i * cur)
            if str1 == (m//i * cur) and str2 == (n//i * cur):
                return cur

        return ""

       