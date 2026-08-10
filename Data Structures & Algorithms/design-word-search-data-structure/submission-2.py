class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end = True
    def search(self, word: str) -> bool:
        # To solve ".ac", "b..", need recursion
        
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                w = word[i]
                if w != ".":
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
                else:
                    for ch in cur.children.values():
                        
                        if dfs(i+1, ch):
                            return True
                    return False
            return cur.end
        return dfs(0, self.root)

