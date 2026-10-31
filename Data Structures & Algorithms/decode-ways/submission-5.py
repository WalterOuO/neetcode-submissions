class Solution:
    def numDecodings(self, s: str) -> int:
        # s = '2018'
        memo = {}

        # 在 index = i 時的方法數
        def dfs(i): 
            if i < 0:
                return 1

            if i in memo:
                return memo[i]

            res = 0
            # 第一種：只取當下位元
            if s[i] != '0':
                res += dfs(i-1)

            # 第二種：跳過當下位元，與前一位元合併解碼
            if i > 0:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    res += dfs(i-2)
            memo[i] = res
            return res

        return dfs(len(s) - 1)
