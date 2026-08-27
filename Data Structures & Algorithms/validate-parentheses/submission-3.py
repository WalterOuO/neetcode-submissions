class Solution:
    def isValid(self, s: str) -> bool:
        # first in first out
        stack = []
        closeTOopen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # 已經走到後括號了 } ] )，開始檢驗前括號是否匹配
            if c in closeTOopen:
                if stack and stack[-1] == closeTOopen[c]:
                    stack.pop()
                else: return False
            else:
                # 加入 前括號 ( [ {
                stack.append(c)
        
        return True if not stack else False