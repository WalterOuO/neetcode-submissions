class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s or not t:
            return ""
        
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for x in t:
            t_map[x] += 1
            s_map[x] += 0

        have, need = 0, len(t_map)
        l = 0
        first = 1
        r = ""
        ans = ""
        for r in range(len(s)):
            if s[r] in t_map:
                if first:
                    l = r
                    first -= 1
                # add have
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]:
                    have += 1

                # condition
                if have < need:
                    continue
                else:
                    while have == need:
                        if s[l] not in t_map:
                            l += 1
                            continue
                        # now s[l] in s_map
                        if s_map[s[l]] > t_map[s[l]]:
                            s_map[s[l]] -= 1
                            l += 1
                            continue
                        res = s[l:r+1]
                        if not ans or len(res) < len(ans):
                            ans = res
                        
                        s_map[s[l]] -= 1
                        if s_map[s[l]] < t_map[s[l]]:
                            have -= 1
                        l += 1
            
        return ans


        # t = XXYZ
        # OXXXOOYOZOOXYZOX
        #  l