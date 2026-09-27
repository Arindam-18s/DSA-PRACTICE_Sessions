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

#---------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
# Middle of a linked list (Using Slow-Fast Approach)

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 step
        return slow
#---------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------
