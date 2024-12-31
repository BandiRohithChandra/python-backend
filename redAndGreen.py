def sort_balls(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    # Iterate through the array
    while mid <= high:
        if arr[mid] == 'R':
            # Swap arr[low] and arr[mid], then increment both
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            # Just move forward with mid
            mid += 1
        else:  # arr[mid] == 'B'
            # Swap arr[mid] and arr[high], then decrement high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage
input_array = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
sorted_array = sort_balls(input_array)
print(sorted_array)
