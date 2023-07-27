
class Heap:
    """
    根据初始化时的堆类型生成相应的小根堆或大根堆
    """
    __instance = None
    
    #  实现单例模式
    def __new__(cls, heap_type):
        if not cls.__instance:
            cls.__instance =  super().__new__(cls) # 调用原始父类Object的__new__方法
        return cls.__instance
    
    def __init__(self, heap_type: str = 'max') -> None:
        if heap_type not in ('max', 'min'):
            raise ValueError('Heap type must be max or min')
        if heap_type == 'max':
            self.heap_type = heap_type
            self.heapify = self._max_heapify
        else:
            self.heap_type = heap_type
            self.heapify = self._min_heapify
    
    def _max_heapify(self, arr, n, i):
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
            self.heapify(arr, n, largest)
    
    def _min_heapify(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[smallest] > arr[left]:
            smallest = left
        if right < n and arr[smallest] > arr[right]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self._min_heapify(arr, n, smallest)
            
    
    def build_heap(self, arr : list)-> "Heap":
        n = len(arr)
        for i in range(n // 2 -1, -1, -1):
            self.heapify(arr, n, i)
            
    def heap_sort(self, arr : list)-> list:
        if self.heap_type == 'max':
            self.build_heap(arr)
            for i in range(len(arr), 1, -1):
                arr[0], arr[i-1] = arr[i-1], arr[0]
                self.heapify(arr, i-1, 0)
        
        else:
            self.build_heap(arr)
            for i in range(0, len(arr)-1):
                arr[i], arr[-1] = arr[-1], arr[0]
                self.heapify(arr, len(arr) - i - 1, i+1)

