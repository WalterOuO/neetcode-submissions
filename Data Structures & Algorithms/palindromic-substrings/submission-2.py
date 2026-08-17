class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.count(s, i, i)
            res += self.count(s, i, i + 1)
        return res

    # Two pointer
    def count(self, s, l, r):
        res = 0
        while l >=  0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
    
    # Evaluation 
    ## Time: O(n^2) for and while loop
    ## Space: O(1) only need res