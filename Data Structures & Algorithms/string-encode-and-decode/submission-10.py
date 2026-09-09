class Solution:
    # Will the s in strs always begin with capital character? not sure 
    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        # 5#Hello5#World
        return encoded_s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])    
            str_start = j + 1
            str_end = str_start + length
            res.append(s[str_start:str_end])
            i = str_end
        return res

        # assume len(strs) == n, len( longest s in strs) == m
        # Time: encode O(n) + while loop O(n)
        # Space: res O(n)
