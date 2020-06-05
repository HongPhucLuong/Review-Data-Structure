class Node:
    def __init__(self, value):
        self.data = value
        self.pNext = None

class LinkedList:
    def __init__(self):
        self.pHead = None

    def _add_at_begining(self, newValue):
        newNode = Node(newValue)
        newNode.pNext = self.pHead
        self.pHead = newNode

    def _add_at_ending(self, newValue):
        if self.pHead is None:
            self.pHead = Node(newValue)
            return

        pTemp = self.pHead
        while pTemp.pNext:
            pTemp = pTemp.pNext
        pTemp.pNext = Node(newValue)

    # add vi tri bat ki
    # linkedlist se k dung index
    def _add_after_value(self, newValue, value1):
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        pTemp = self.pHead
        while pTemp:
            if pTemp.data == value1:
                newNode = Node(newValue)
                newNode.pNext = pTemp.pNext
                pTemp.pNext = newNode
            pTemp = pTemp.pNext


    #delete value
    def _delete_value(self, value):
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        pTemp = self.pHead
        pPre = pTemp
        while pTemp:
            if pTemp.data != value:
                pPre = pTemp
                pTemp = pTemp.pNext
            else:
                pDel = pTemp
                pPre.pNext = pTemp.pNext
                pTemp = pTemp.pNext
                del pDel

    #delete index
    def _delete_index(self, index):
        pass

    def _print_list_left_right(self):
        listVal = []
        pTemp = self.pHead
        while pTemp:
            listVal.append(pTemp.data)
            pTemp = pTemp.pNext
        print(listVal)
        return listVal

    def _get_len(self) -> int:
        if self.pHead is None:
            return 0
        if self.pHead.pNext is None:
            return 1
        count = 1
        pTemp = self.pHead
        while pTemp.pNext:
            count += 1
            pTemp = pTemp.pNext
        return count


def test():
    myLinkedList = LinkedList()
    # [myLinkedList._add_at_begining(i) for i in range(10)]
    # [myLinkedList._add_at_begining(i) for i in range(10)]
    # myLinkedList._add_after_value(100, 9)
    # myLinkedList._add_after_value(100, 2)
    # myLinkedList._print_list_left_right()
    # print('len={}'.format(myLinkedList._get_len()))
    # myLinkedList._delete_value(0)
    # myLinkedList._delete_value(5)
    # myLinkedList._print_list_left_right()
    # print('len={}'.format(myLinkedList._get_len()))

    

test()
