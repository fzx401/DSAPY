import random
from BinaryTree.heap import Heap

heap = Heap(heap_type='min')
print(heap)

heap2 = Heap(heap_type='min')
print(heap2)

heap3 = Heap(heap_type='max')
print(heap3)

if not heap:
    print('singleton yes')
# random.seed(4)
# nums = [random.randint(0, 7) for _ in range(6)]
# print('---before---')
# print('---array---')
# print(nums)
# print('-------')
# print('\n')

# heap.build_heap(nums)
# print('---after---')
# print('---heap---')
# print(nums)

# heap.heap_sort(nums, order='desc')
# print('---after---')
# print('---heap sort(asc)---')
# print(nums)