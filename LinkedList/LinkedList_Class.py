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

    #delete value
    def _delete_value(self, value):
        pass

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
        count = 1
        pTemp = self.pHead
        while pTemp.pNext:
            count += 1
            pTemp = pTemp.pNext
        return count


def test():
    myLinkedList = LinkedList()

test()
