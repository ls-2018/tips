'''
两种方法
方法一:顺序遍历两次,第一次获取长度n
方法二:两个指针,快的比慢的先前移K步,在一起移动
'''


class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None


# 构造单链表
def ConstructList():
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    return head

    # head 1 2 3 4 5 6 7


def PrintList(head):
    cur = head.next
    while cur != None:
        print('->', cur.data, end='', sep='')
        cur = cur.next
    print()


def FindLastk(head, k):
    if head == None or head.next == None:
        return
    slow = head.next
    fast = head.next
    i = 0
    while i < k:
        fast = fast.next
        i += 1
    if i < k:
        return
    while fast != None:
        slow = slow.next
        fast = fast.next
    return slow


if __name__ == '__main__':
    head = ConstructList()
    result = None
    PrintList(head)
    result = FindLastk(head, 3)
    print(result.data)
