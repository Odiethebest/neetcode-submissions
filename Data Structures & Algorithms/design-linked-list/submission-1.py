class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        # create a node
        newNode = ListNode(val)
        # link to next:
        newNode.next = self.dummy.next
        # link to prev:
        self.dummy.next = newNode

        self.size += 1


    def addAtTail(self, val: int) -> None:
        # create a node
        newNode = ListNode(val)
        curr = self.dummy

        #只要节点后还有节点，就继续往后走
        while curr.next:
            curr = curr.next
        curr.next = newNode

        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        # 第一关：如果指定的 index 比当前链表长度还要大，直接拒绝，什么也不做
        if index > self.size:
            return 
    
        # （特殊处理：如果 index 是负数，题目要求默认插在头部，即 index=0）
        if index < 0:
            index = 0
            
        # --- 正常找位置和插入节点的逻辑 ---
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
            
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        
        # 第二关（关键！）：节点已经成功安插进去了，链表变长了，记账员赶紧加 1！
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
            
        delete = self.dummy
        for _ in range(index):
            delete = delete.next
        delete.next = delete.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)