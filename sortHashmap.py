def sort_map_by_value(input_map):
    # Sort the dictionary by value using sorted() and a lambda function as the key
    sorted_items = sorted(input_map.items(), key=lambda x: x[1])
    
    # Convert the sorted list of tuples back to a dictionary
    sorted_map = dict(sorted_items)
    
    return sorted_map

# Example usage
input_map = {101: 'John Doe', 102: 'Jane Smith', 103: 'Peter Johnson'}
sorted_map = sort_map_by_value(input_map)

print("Sorted Map:", sorted_map)
