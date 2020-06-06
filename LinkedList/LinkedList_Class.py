class Node:
    def __init__(self, value):
        self.data = value
        self.pNext = None

class LinkedList:
    def __init__(self):
        self.pHead = None
        self.listReverse = []
        
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

    # update value
    def _update_value(self, oldValue, newValue):
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        pTemp = self.pHead
        while pTemp:
            if pTemp.data == oldValue:
                pTemp.data = newValue
            pTemp = pTemp.pNext

    # find value
    def _find_index(self, value) -> list:
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        listIndex = []
        pTemp = self.pHead
        index = 0
        while pTemp:
            if pTemp.data == value:
                listIndex.append(index)
            index += 1
            pTemp = pTemp.pNext
        if len(listIndex) == 0:
            print('LinkedList does not have {}!\n'.format(value))
        return listIndex

    # def _extend_another(self, linkedList2: LinkedList):
    #     if self.pHead is None:
    #         self.pHead = linkedList2.pHead
    #         return
    #     if linkedList2.pHead is None:
    #         print('LinkedList is not exists!')
    #         return
    #     if self.pHead is None and linkedList2.pHead is None:
    #         print('Both LinkedList is not exists!')
    #         return
    #     pTemp = self.pHead
    #     while pTemp:
    #         pTemp = pTemp.pNext
    #     pTemp.pNext = linkedList2.pHead

    def _print_list_left_right(self):
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        listVal = []
        pTemp = self.pHead
        while pTemp:
            listVal.append(pTemp.data)
            pTemp = pTemp.pNext
        print(listVal)
        # return listVal

    def _get_list_reverse(self, pNode: Node):
        if self.pHead is None:
            print('LinkedList is not exists!')
            return
        if pNode is None:
            return
        self._get_list_reverse(pNode.pNext)
        # print('{} '.format(pNode.data))
        self.listReverse.append(pNode.data)

    def _print_list_right_left(self):
        self._get_list_reverse(self.pHead)
        print(self.listReverse)

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

def _add_linked2_to_linked1(linked1, linked2):
    if linked1.pHead is None and linked2.pHead is None:
        print('Both linkedlist is not exists!')
        return
    if linked1.pHead is None and linked2.pHead is not None:
        linked1.pHead = linked2.pHead
        return
    if linked2.pHead is None:
        print('Linkedlist2 is not exists!')
        return
    pTemp = linked1.pHead
    while pTemp.pNext:
        pTemp = pTemp.pNext
    pTemp.pNext = linked2.pHead

def test():
    myLinkedList = LinkedList()
    # print('Adding at the begining of LinkedList 0->9')
    # [myLinkedList._add_at_begining(i) for i in range(10)]
    # myLinkedList._print_list_left_right()

    # print('Adding at the ending of LinkedList 0->9')
    # [myLinkedList._add_at_ending(i) for i in range(10)]
    # myLinkedList._print_list_left_right()
    
    # print('Insert 100 after 9, 2')
    # myLinkedList._add_after_value(100, 9)
    # myLinkedList._add_after_value(100, 2)
    
    # print('LinkedList left to right')
    # myLinkedList._print_list_left_right()
    
    # print('LinkedList right to left')
    # myLinkedList._print_list_right_left()
    
    # print('Delete 0, 5')
    # myLinkedList._delete_value(0)
    # myLinkedList._delete_value(5)
    # myLinkedList._print_list_left_right()
    
    # print('Update value 8 = 200')
    # myLinkedList._update_value(8, 200)
    # myLinkedList._print_list_left_right()

    # print('Finding index of value=200: {}\n'.format(myLinkedList._find_index(200)))
    
    # print('length:{}'.format(myLinkedList._get_len()))

    A = LinkedList()
    [A._add_at_ending(i) for i in range(0, 10, 2)]
    print('Linkedlist A:')
    A._print_list_left_right()
    B = LinkedList()
    [B._add_at_ending(i) for i in range(1, 10, 2)]
    print('Linkedlist B:')
    B._print_list_left_right()
    _add_linked2_to_linked1(A, B)
    print('Linkedlist A:')
    A._print_list_left_right()
    

    

test()
