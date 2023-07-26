def heapify(nums, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[smallest] > nums[left]:
        smallest = left
    if right < n and nums[smallest] > nums[right]:
        smallest = right
    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        heapify(nums, n, smallest)

def build_min_heap(nums):
    n = len(nums)
    """
    1.堆化整体是从较深层向浅层上升
    2.但是在每层进行堆化的时候，都是一直向下直到不满足条件为止
    3.从最后一个非叶子节点开始堆化，逐渐向上
    """
    for i in range(n//2 - 1, -1, -1):
        heapify(nums, n, i)
    return nums

nums = [1, 2, 3, 4, 5]
print(build_min_heap(nums[::-1]))
print