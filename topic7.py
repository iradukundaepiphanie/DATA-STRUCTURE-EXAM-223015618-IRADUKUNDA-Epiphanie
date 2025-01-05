def merge_sort(events):
    """Sort a list of events based on their priority using Merge Sort."""
    if len(events) <= 1:
        return events

    # Split the list into halves
    mid = len(events) // 2
    left_half = merge_sort(events[:mid])
    right_half = merge_sort(events[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]['priority'] <= right[j]['priority']:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Example usage
def main():
    events = [
        {"event_name": "Wedding", "priority": 3},
        {"event_name": "Conference", "priority": 1},
        {"event_name": "Birthday Party", "priority": 4},
        {"event_name": "Corporate Meeting", "priority": 2},
    ]

    print("Unsorted Events:")
    for event in events:
        print(event)

    sorted_events = merge_sort(events)

    print("\nSorted Events by Priority:")
    for event in sorted_events:
        print(event)

if __name__ == "__main__":
    main()