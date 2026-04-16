from data_structure_heap import MaxHeap

def heap_sort(arr, key=lambda x: x):
    class KeyedMaxHeap(MaxHeap):
        def insert(self, item):
            self.heap.append(item)
            self.sift_up(len(self.heap)-1)
        
        def sift_up(self, i):
            while i > 0:
                parent = (i - 1) // 2
                if self.heap[i][0] > self.heap[parent][0]:
                    self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                    i = parent
                else:
                    break
        
        def sift_down(self, i):
            n = len(self.heap)
            while True:
                left, right = 2*i+1, 2*i+2
                max_idx = i
                if left < n and self.heap[left][0] > self.heap[max_idx][0]:
                    max_idx = left
                if right < n and self.heap[right][0] > self.heap[max_idx][0]:
                    max_idx = right
                if max_idx != i:
                    self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                    i = max_idx
                else:
                    break
        
        def pop_max(self):
            if not self.heap:
                return None
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            return self.heap.pop()

    mh = KeyedMaxHeap()
    for elem in arr:
        mh.insert((key(elem), elem))
    
    sorted_arr = []
    while mh.heap:
        _, elem = mh.pop_max()
        sorted_arr.insert(0, elem)
    return sorted_arr

if __name__ == "__main__":
    test1 = [5,2,9,1,5,6]
    print("Original list: ", test1)
    print("After Heap Sort: ", heap_sort(test1))
    
    test2 = [3,1,2]
    print("Original list: ", test2)
    print("After Heap Sort: ", heap_sort(test2))