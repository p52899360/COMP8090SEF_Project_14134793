from data_structure_heap import MaxHeap

def heap_sort(arr):
    """
    Sort an input list using the Heap Sort algorithm.
    Args:
        arr (list): Unsorted list of comparable elements
    Returns:
        list: Sorted list in ascending order
    """
    # Phase 1: Build a Max-Heap from the input array
    max_heap = MaxHeap()
    for num in arr:
        max_heap.insert(num)

    # Phase 2: Repeatedly extract max and build sorted array
    sorted_arr = []
    while len(max_heap.heap) > 0:
        current_max = max_heap.pop_max()
        # Insert max at the BEGINNING of sorted list to get ASCENDING order
        sorted_arr.insert(0, current_max)

    return sorted_arr

# Test code for Heap Sort (runs only when this file is executed directly)
if __name__ == "__main__":
    print("=== Testing Heap Sort ===")
    test1 = [5, 2, 9, 1, 5, 6]
    print(f"Original list 1: {test1}")
    print(f"Sorted list 1:   {heap_sort(test1)}")

    test2 = [3, 1, 2, 7, 4, 8, 5]
    print(f"\nOriginal list 2: {test2}")
    print(f"Sorted list 2:   {heap_sort(test2)}")