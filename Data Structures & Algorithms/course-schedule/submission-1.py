class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 为每门课程创建一个映射，存储它的所有先修课程
        preMap = {i:[] for i in range(numCourses)}
        
        # 根据prerequisites构建课程的先修关系图
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # 用集合记录当前DFS遍历路径上的课程（检测环）
        visiting = set()

        def dfs(crs):
            # 如果当前课程已在访问路径中，说明存在环，无法完成所有课程
            if crs in visiting:
                return False
            
            # 如果该课程没有先修课程，说明可以直接学习，返回True
            if preMap[crs] == []:
                return True
            
            # 将当前课程加入访问路径
            visiting.add(crs)
            
            # 递归检查所有先修课程是否都可以完成
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # 当前课程的所有先修课程都检查完毕，将其从访问路径中移除
            visiting.remove(crs)
            
            # 清空该课程的先修课程列表（标记为已处理，避免重复检查）
            preMap[crs] = []
            
            # 该课程及其先修课程都可以完成
            return True
        
        # 对每门课程都进行一次DFS检查
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        # 所有课程都可以完成
        return True