class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def inputList(self, l1: ListNode, l2: ListNode):
        node1 = l1
        node2 = l2
        inputList1 = []
        inputList2 = []
        while node1 != None:
            if node1.val != None:
                inputList1.append(node1.val)
            if node1.next != None:
                node1 = node1.next
            else:
                node1 = None

        while node2 != None:
            if node2.val != None:
                inputList2.append(node2.val)
            if node2.next != None:
                node2 = node2.next
            else:
                node2 = None
        print(f"Input: l1 = {inputList1}, l2 = {inputList2}")

    def outputList(self, mergeList: ListNode):
        node = mergeList
        ansList = []
        while node != None:
            if node.val != None:
                ansList.append(node.val)
            if node.next != None:
                node = node.next
            else:
                node = None
        print("Output: ", ansList)


def main():
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    solution.inputList(l1, l2)
    mergeList = solution.mergeTwoLists(l1, l2)
    solution.outputList(mergeList)

if __name__ == "__main__":
    main()
