class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        I did this for plaid bruh
        
        OPTIONS
        . - nothing
        .. - goes back
        anything else - goes into the directory
        / - whatever

        we can turn the path str into a list of inputs
        '''
        # VOODOO BLACK MAGIC PATH SPLITTING MANEUVERS
        res = []
        paths = path.split('/')

        for p in paths:
            if p == "..":
                if res:
                    res.pop()
            else:
                if p == '' or p == '.':
                    continue
                else:
                    res.append(p)


        return  '/' + "/".join(res)