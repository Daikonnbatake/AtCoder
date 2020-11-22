import heapq as heap

def heapSort(array):
    a = array
    heap.heapify(a)
    return [heap.heappop(a)for i in range(len(a))]