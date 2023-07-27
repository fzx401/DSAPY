import random
from Heap.Heap import Heap


def heap_sort(arr : list)-> None:
    heap = Heap(heap_type='min')
    heap.build_heap(arr)
    heap.heap_sort(arr)

random.seed(5)
nums = [random.randint(0, 7) for _ in range(10)]
print(nums)
heap_sort(nums)
print(nums)


