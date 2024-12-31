def min_platforms(arrivals, departures):
    # Sort the arrival and departure times
    arrivals.sort()
    departures.sort()
    
    n = len(arrivals)
    i = 0  # Pointer for arrival
    j = 0  # Pointer for departure
    platforms_needed = 0
    max_platforms = 0
    
    # Traverse the arrival and departure times
    while i < n and j < n:
        # If next train is arriving before or when the last train departs
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        
        # Update the maximum platforms required
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms

# Example usage
arrivals1 = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
departures1 = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']
print(min_platforms(arrivals1, departures1))  # Output: 3

arrivals2 = ['9:00', '9:40']
departures2 = ['9:10', '12:00']
print(min_platforms(arrivals2, departures2))  # Output: 1
