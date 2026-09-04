class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = collections.defaultdict(int)
        hash_t = collections.defaultdict(int)

        for r in s:
            hash_s[r] += 1
        for c in t:
            hash_t[c] += 1
        
        return hash_s == hash_t