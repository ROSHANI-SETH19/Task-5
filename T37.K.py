import heapq

def find_k_largest(nums, k):
    # Edge case: if k is 0 or the list is empty
    if k == 0 or not nums:
        return []
    
    # Initialize a min-heap with the first k elements (negative to simulate max-heap)
    heap = nums[:k]
    heapq.heapify(heap)
    
    # Process the rest of the elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap

# Example usage
nums = [3, 1, 5, 12, 2, 11]
k = 3
print(f"The {k} largest elements are: {find_k_largest(nums, k)}")
