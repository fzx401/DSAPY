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


# 主函数来构建一个堆
def build_heap(arr):
    n = len(arr)

    # 从最后一个非叶子节点开始进行堆化
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# 示例用法
arr = [4, 10, 3, 5, 1, 7, 6]
build_heap(arr)
print(arr)



