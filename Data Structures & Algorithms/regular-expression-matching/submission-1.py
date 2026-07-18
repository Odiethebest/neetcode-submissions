class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[j] 表示：从字符串s的当前位置开始，能否匹配模式p[j:]
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True  # 空模式总是能匹配空字符串

        # 从后往前遍历字符串s
        for i in range(len(s), -1, -1):
            # 创建新的dp数组，用于存储当前行的结果
            nextDp = [False] * (len(p) + 1)
            
            # 空模式只能匹配空字符串
            # 只有当i == len(s)时（即s已经全部匹配完），空模式才返回True
            nextDp[len(p)] = (i == len(s))

            # 从后往前遍历模式p
            for j in range(len(p) - 1, -1, -1):
                # 检查当前位置是否匹配
                # match为True表示：s[i]和p[j]可以匹配（相同或p[j]是'.'）
                is_current_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                # 检查下一个位置是否是'*'
                has_star_next = (j + 1) < len(p) and p[j + 1] == "*"

                if has_star_next:
                    # 情况1：p[j]*的处理
                    # nextDp[j + 2]：*匹配0个字符的情况
                    nextDp[j] = nextDp[j + 2]
                    
                    # 如果当前字符匹配，我们还可以选择*匹配1个或多个字符
                    # dp[j]：移动到s的下一个位置，p[j]保持不变（继续匹配*）
                    if is_current_match:
                        nextDp[j] = nextDp[j] or dp[j]
                else:
                    # 情况2：普通字符的处理
                    # 只有当前字符匹配时，才能继续匹配后续的模式
                    if is_current_match:
                        nextDp[j] = dp[j + 1]
                    # 如果不匹配，nextDp[j]保持False

            # 更新dp为下一行的数据
            dp = nextDp

        return dp[0]