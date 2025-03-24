from collections import Counter

def find_duplicates(nums):
    # Use Counter to count occurrences of each element
    count = Counter(nums)
    
    # Extract the elements that appear more than once
    duplicates = [num for num, freq in count.items() if freq > 1]
    
    return duplicates

# Example usage
nums = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1]
print(f"Duplicates: {find_duplicates(nums)}")