# Singly linked list
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)        # head[1]--->A[4]--->B[6]--->C[9]
A = SinglyNode(4)
B = SinglyNode(6)
C = SinglyNode(9)

Head.next = A  # Linked LIst got connected here
A.next = B
B.next = C

curr = Head        # We Use traversal to print the Whole list - O(n)        # head[1]--->A[4]--->B[6]--->C[9]
while curr:                                                                 #   ^
    # print(curr)                                                             #  curr
    curr = curr.next

# print("Head val -> ", Head)     # Printing the value of the Head

def display(Head):      # Linked list printing Function
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    # print(' -> '.join(elements))        # ['a', 'b', 'c']  => 'a -> b -> c'  (list to string)

display(Head)           # head[1]--->A[4]--->B[6]--->C[9]  =>  1 -> 4 -> 6 -> 9

# Search for node value - O(n)
def search(Head, val):
    curr = Head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False

search(Head, 8)

# ---------------------------------------------------------------------------------------------------
# Doubly linked list

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


def displayDoubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))  

# displayDoubly(head)


head = tail = DoublyNode(2)     # Assigning the head and the tail the same node value, head ->[2]<- tail

# Insert at the begining - as manual insersion is not possible like a Singly linked list, cause the doubly has a next and a prev also
def insert_at_begining(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail       # => return 'head_of_new_list' , 'tail_of_new_list'

head, tail = insert_at_begining(head, tail, 3)  # Python does this behind the scenes: -> head = temp[0] & tail = temp[1] => head = new_node & tail = old_tail
displayDoubly(head)

# Insert at the end
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head,new_node        # => return 'head_of_new_list' , 'tail_of_new_list'

head, tail = insert_at_end(head, tail, 8)
displayDoubly(head)
# ---------------------------------------------------------------------------------------------------
# Middle of a linked list (Using Slow-Fast Approach)

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 step
        return slow
# ---------------------------------------------------------------------------------------------------
# 61. Rotate List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length  # Handle k values larger than length - here its 2 again

        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head

# 2. Convert the list [1, 2, 3, 4, 5] into real ListNode objects
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)  # This is the front of your list

sol = Solution()    # 3. Instantiate the Solution class

rotated_head = sol.rotateRight(head, k=2)   # 4. Call the method
# ---------------------------------------------------------------------------------------------------
# 141. Linked List Cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findListCycle(self, head: ListNode):
        slowPointer = head
        fastPointer = head

        if slowPointer != None and fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

            if slowPointer == fastPointer:
                return True
        return False
# ---------------------------------------------------------------------------------------------------
# Reversing a Linked List

def reverseList(head):     # O(n) Time, 0(1) Space
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# ---------------------------------------------------------------------------------------------------
# 234. Palindrome Linked List - Given the head of a singly linked list, return true if it is a palindrome
#                               or false otherwise. - Tcol -> O(n), Space -> O(1)
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True                         # Main Strategy is to first find the middle of the linked list
        slow = fast = head                      # Then reverse the secind half, And Check for pallindrome from
        while fast and fast.next:               # Behind and from the start until both intersects in the middle
            slow = slow.next
            fast = fast.next.next

        tail = slow
        prev = None
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        tail = prev     # Reversed Linked List Head At the last position
            
        while tail:
            if head.val == tail.val:
                head = head.next
                tail = tail.next
            else:
                return False
        return True

# ---------------------------------------------------------------------------------------------------
# Question - Given Head of a LinkedList And a num, eleminate all the listnodes with value < that given num, and return the List

# head = ListNode(3)        # head[3]--->A[5]--->B[1]--->C[6]--->D[7]
# A = ListNode(5)
# B = ListNode(1)
# C = ListNode(6)
# D = ListNode(7)

# head.next = A  # Linked LIst got connected here
# A.next = B
# B.next = C
# C.next = D

class Solution:
    def findNthnum(self, head:ListNode, num:int):
        temp = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while temp:
            if temp.val < num:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return dummy.next

sol = Solution()
result = sol.findNthnum(head, 5)
while result:
    print(result.val , end=" -> ")
    result = result.next

# ---------------------------------------------------------------------------------------------------
# 203. Remove Linked List Elements - Given the head of a linked list and an integer val, remove all the nodes 
                               #   of the linked list that has Node.val == val, and return the new head.

def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
    temp = head
    dummy = ListNode()
    dummy.next = head          #   head = [1,2,6,3,4,5,6], val = 6 Output: [1,2,3,4,5]
    prev = dummy
    while temp:
        if temp.val == val:
            prev.next = temp.next
            temp = temp.next
        else:
            prev = temp
            temp = temp.next
    return dummy.next

# ---------------------------------------------------------------------------------------------------
