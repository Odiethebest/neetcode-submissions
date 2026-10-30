class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(lo,hi):
            if lo>hi:return [None]
            answer=[]
            for value in range(lo,hi+1):
                for left in build(lo,value-1):
                    for right in build(value+1,hi):answer.append(TreeNode(value,left,right))
            return answer
        return build(1,n)
