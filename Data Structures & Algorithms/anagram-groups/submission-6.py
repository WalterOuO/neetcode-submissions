class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group ["act", "cat"] together store in a list? a hash?
        # use freq list as idx of hashmap, val = list()
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            hashmap[key].append(s)
        
        return list(hashmap.values())

        # Time: O(n) for loop * O(m) for each s = O(n*m)
        # Space: O(n) for at most n diff key of s in strs