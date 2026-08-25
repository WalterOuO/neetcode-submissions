class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological Sort from DAG graph
        # Kahn's algorithm (BFS topological sort) 
        
        # dict: 給所有不重複字母建立set()，方便紀錄他們等等指向誰
        adj = { c:set() for w in words for c in w}
        # 入度表：紀錄每個字母被指到的次數(入度)
        indegree = {c:0 for c in adj}
            
        for i in range(len(words) -1):  # 兩兩一組所以要只走到倒數第二位
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            # to avoid ["addac", "add"] this condition
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                # ch不同就break, 但要先把順序關係加入set(), 更新入度表
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # queue 放入沒人指的 ch, 可作為 str開頭
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        
        while q:
            ch = q.popleft()
            res.append(ch)
            for child in adj[ch]:
                indegree[child] -= 1    # remove ch 指向 child的那個箭頭
                if indegree[child] == 0:
                    q.append(child)
        
        # last check: res len should same as ch num(len of indegree)
        if len(res) != len(indegree):
            return ""

        return "".join(res)