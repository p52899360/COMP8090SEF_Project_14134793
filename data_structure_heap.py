class MaxHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            max_idx = i
            if left < n and self.heap[left] > self.heap[max_idx]:
                max_idx = left
            if right < n and self.heap[right] > self.heap[max_idx]:
                max_idx = right
            if max_idx != i:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx
            else:
                break

    def insert(self, num):
        self.heap.append(num)
        self.sift_up(len(self.heap)-1)

    def pop_max(self):
        if len(self.heap) == 0:
            print("No elements in heap, cannot pop!")
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_num = self.heap.pop()
        self.sift_down(0)
        return max_num

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

if __name__ == "__main__":
    h = MaxHeap()
    h.insert(3)
    h.insert(8)
    h.insert(5)
    h.insert(1)
    print("Current heap elements: ", h.heap)
    print("Max element in heap: ", h.get_max())
    print("Pop max element: ", h.pop_max())
    print("Heap elements after pop: ", h.heap)