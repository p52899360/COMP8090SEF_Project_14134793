class MaxHeap:
    """
    A Max-Heap data structure implementation using a Python list.
    Core ADT operations: insert(), pop_max(), get_max().
    """
    def __init__(self):
        self.heap = []  # Underlying storage: 1D list

    def sift_up(self, i):
        """
        Helper: Move a node up the tree to restore heap property after insertion.
        Args:
            i (int): Index of the node to sift up
        """
        while i > 0:
            parent_idx = (i - 1) // 2  # Calculate parent index using list mapping
            # If current node is larger than parent, swap them
            if self.heap[i] > self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
                i = parent_idx  # Move up to parent for next iteration
            else:
                break  # Heap property restored, exit loop

    def sift_down(self, i):
        """
        Helper: Move a node down the tree to restore heap property after pop_max().
        Args:
            i (int): Index of the node to sift down
        """
        n = len(self.heap)
        while True:
            left_idx = 2 * i + 1   # Left child index
            right_idx = 2 * i + 2  # Right child index
            max_idx = i             # Assume current node is max initially

            # Update max_idx if left child exists and is larger
            if left_idx < n and self.heap[left_idx] > self.heap[max_idx]:
                max_idx = left_idx
            # Update max_idx if right child exists and is larger
            if right_idx < n and self.heap[right_idx] > self.heap[max_idx]:
                max_idx = right_idx

            # If max node is not current node, swap and continue sifting down
            if max_idx != i:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx
            else:
                break  # Heap property restored, exit loop

    def insert(self, value):
        """
        Add a new value to the heap while maintaining the heap property.
        Args:
            value: Comparable value to insert (int/float typically)
        """
        self.heap.append(value)  # Add new value to the end of the list
        self.sift_up(len(self.heap) - 1)  # Sift up the new value to correct position

    def pop_max(self):
        """
        Remove and return the maximum value (root) of the heap.
        Returns:
            Maximum value in the heap; None if heap is empty
        """
        if len(self.heap) == 0:
            print("Error: Heap is empty, cannot pop max!")
            return None
        # Step 1: Swap root (max) with last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # Step 2: Remove and store the last element (original max)
        max_value = self.heap.pop()
        # Step 3: Sift down the new root to restore heap property
        self.sift_down(0)
        return max_value

    def get_max(self):
        """
        Return the maximum value without removing it.
        Returns:
            Maximum value in the heap; None if heap is empty
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Test code for MaxHeap (runs only when this file is executed directly)
if __name__ == "__main__":
    print("=== Testing MaxHeap ===")
    heap = MaxHeap()
    test_values = [3, 8, 5, 1, 9, 6]
    print(f"Inserting values: {test_values}")
    for val in test_values:
        heap.insert(val)
    print(f"Heap list after inserts: {heap.heap}")
    print(f"Current max (get_max): {heap.get_max()}")
    print(f"Popping max: {heap.pop_max()}")
    print(f"Heap list after pop: {heap.heap}")