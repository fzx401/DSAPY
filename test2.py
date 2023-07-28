# def heapify(arr, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
    
#     if left < n and arr[smallest] > arr[left]:
#             smallest = left
#     if right < n and arr[smallest] > arr[right]:
#             smallest = right
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         heapify(arr, n, smallest)

# def build_heap(arr : list):
#     n = len(arr)
#     for i in range(n // 2 -1, -1, -1):
#         heapify(arr, n, i)


# def heap_sort(arr):
#     res = []
#     tmp = arr[:]
#     for i in range(0, len(arr)):
#         res.append(tmp[0])
#         tmp = tmp[1:]
#         build_heap(tmp)
#     return res
        
        
             
# arr = [7, 3, 2, 1, 9, 12, 5]
# print(f'array before heap build is {arr}')  
# build_heap(arr)
# print(f'array after heap build and before heap sort is {arr}')
# arr = heap_sort(arr)
# print(f'array after heap sort is {arr}')


def heapify(arr, n, i):
    largest = i  # 初始化最大值为根节点
    left = 2 * i + 1
    right = 2 * i + 2

    # 检查左子节点是否大于根节点
    if left < n and arr[i] < arr[left]:
        largest = left

    # 检查右子节点是否大于根节点和左子节点
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 如果根节点不是最大值，则进行交换并递归调用堆化函数
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def build_heap(arr : list):
    n = len(arr)
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    tmp = arr[:]
    # tmp = arr[:]
    for i in range(0, len(arr)):
        arr[i] = tmp[0]
        # res.append(tmp[0])
        tmp = tmp[1:]
        build_heap(tmp)
    return        
        
        
arr = [7, 3, 2, 1, 9, 12, 5]
print(f'array before heap build is {arr}')  
build_heap(arr)
print(f'array after heap build and before heap sort is {arr}')
heap_sort(arr)
print(f'array after heap sort is {arr}')