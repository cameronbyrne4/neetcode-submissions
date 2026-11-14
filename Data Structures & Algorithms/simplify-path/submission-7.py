class Solution:
    def simplifyPath(self, path: str) -> str:
        inputs = path.split('/') # does store the whitespaces btw, so keep that in mind
        stack = []

        for i in inputs:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i) 


        return  "/" + "/".join(stack)