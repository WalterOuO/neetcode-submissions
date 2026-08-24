class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s or not t:
            return ""
        
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for x in t:
            t_map[x] += 1

        have, need = 0, len(t_map)
        l = 0
        # first = 1
        ans = ""
        for r in range(len(s)):
            if s[r] in t_map:
                # nooooo need
                # if first:
                #     l = r
                #     first -= 1

                # add have
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]:
                    have += 1

                # condition
                while have == need:
                    res = s[l:r+1]
                    if not ans or len(res) < len(ans):
                        ans = res
                    
                    if s[l] in t_map:
                        s_map[s[l]] -= 1
                        if s_map[s[l]] < t_map[s[l]]:
                            have -= 1
                    l += 1            
        return ans
