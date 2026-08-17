class Solution:
    def numDecodings(self, s: str) -> int:
        # Top-Down + Memory Dynamic Programming
        # Initialize: set the way to decode last digit as 1
        dp = { len(s) : 1}

        def dfs(i):
            # base case: if i is end of string
            if i in dp:
                return dp[i]
            # bad base case: a single 0 cannot decode to any ch
            if s[i] == "0":
                return 0

            # recursivly count
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == '1')):
                res += dfs(i + 2)
            if (i + 1 < len(s) and (s[i] == '2') and ('0' <= s[i+1] <= '6')):
                res += dfs(i + 2)
            # store the number of way to dictionary
            dp[i] = res
            return res

        return dfs(0)