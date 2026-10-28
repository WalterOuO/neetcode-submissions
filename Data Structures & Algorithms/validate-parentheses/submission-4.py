class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for w in s:
            if w not in closetoopen:
                stack.append(w)
            else:
                if stack and stack[-1] == closetoopen[w]:
                    stack.pop()
                else:
                    return False

        return False if stack else True    
            