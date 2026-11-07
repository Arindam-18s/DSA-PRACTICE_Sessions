import heapq        # MAILY IS A PRIORITY QUEUE 

"""
T1 : 5
T2 : 4
T3 : 9      * Max Heap * Returns This - Largest element at the Top
T4 : 6
T5 : 1      * Min Heap * Returns This - Smallest element at the Top
"""

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
heapq.heapify(data)           # Implements MIN-HEAP By Default

print(data)     # [1, 1, 17, 2, 2, 65, 43, 44, 10, 3, 20] 

"""

if i am at position i, 
my first child is at the index - (2 * i + 1)
my first child is at the index - (2 * i + 1)
my PARENT is at the index - (i - 1) // 2

"""

print(heapq.heappop(data))  # To Get the data with the most priority | Gets the data from the front of the HEAP, 
print(heapq.heappop(data))  # and Heapifies the HEAP with the remaining vals

heapq.heappush(data, 2)     # Adding new element into the heap
# print(data)

""" MAX HEAP Implementation """

max_heap_data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1] 
max_heap_data = [-x for x in max_heap_data]
heapq.heapify(max_heap_data)                # Method 1: Basic, Just use neagtive vals, with General Heap fn.'s

print(max_heap_data)

# -----------                               
class MaxHeap:
  def __init__(self):
    self.heap = []

  def push(self, val):
    self.heap.append(val)
    self._heapify_up(len(self.heap) - 1)

  def pop(self):
    if not self.heap:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    max_val = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._heapify_down(0)
    return max_val

  def peek(self):
    return self.heap[0] if self.heap else None

  def _heapify_up(self, index):
    parent = (index - 1) // 2
    if index > 0 and self.heap[index] > self.heap[parent]:
      self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
      self._heapify_up(parent)

  def _heapify_down(self, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < len(self.heap) and self.heap[left] > self.heap[largest]:
      largest = left
    if right < len(self.heap) and self.heap[right] > self.heap[largest]:
      largest = right
    if largest != index:
      self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
      self._heapify_down(largest)

  # Add this method to allow direct printing of the heap
  def __str__(self):
    return str(self.heap)


# Example Usage:
custom_heap = MaxHeap()
for num in [10, 30, 20, 400]:
  custom_heap.push(num)

print(custom_heap)  # Outputs: [400, 30, 20, 10]
print("Custom Max:", custom_heap.peek())  # Outputs: 400
print("Custom Popped:", custom_heap.pop())  # Outputs: 400
print(custom_heap)  # Outputs the remaining heap: [30, 10, 20]

# -----------

# Two List Combined and HEAPIFIED

l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]

l3 = heapq.merge(l1, l2)
# print(list(l3))