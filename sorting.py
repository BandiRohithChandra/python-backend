def sorted_squares(arr):
    n = len(arr)
    result = [0] * n  # Initialize the result array
    left, right = 0, n - 1
    pos = n - 1  # Position to place the next largest square
    
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        
        pos -= 1
    
    return result

# Example usage
input_array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
output_array = sorted_squares(input_array)
print(output_array)
