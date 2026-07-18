class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 建立邻接表：每个字符指向它后面的字符
        adj = {}
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()

        # 比较相邻两个单词，找出字符的顺序关系
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # 检查是否违反顺序：w1比w2长但是w1是w2的前缀
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # 找出第一个不同的字符，建立关系
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # DFS + 拓扑排序，检测环并收集结果
        visited = {}  # {char: True/False} True表示在当前路径上，False表示已处理
        res = []

        def dfs(char):
            # 如果已经访问过，返回是否存在环
            if char in visited:
                return visited[char]

            # 标记为在当前路径上（用于检测环）
            visited[char] = True

            # 访问所有邻接字符
            for neighbor_char in adj[char]:
                if dfs(neighbor_char):
                    return True  # 发现环

            # 标记为已完全处理
            visited[char] = False
            # 添加到结果（拓扑排序）
            res.append(char)
            return False

        # 对所有字符进行DFS
        for char in adj:
            if dfs(char):
                return ""  # 发现环，无效的字典序

        # 反转得到正确的拓扑顺序
        res.reverse()
        return "".join(res)