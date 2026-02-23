
# Recursive Binary Search
def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    return -1

# Sample Execution
data = [10, 20, 30, 40, 50]
result = binary_search(data, 0, len(data) - 1, 40)
print("Element found at index:", result)
