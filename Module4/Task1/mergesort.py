def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Split the arr into two halves
    left_half = arr[:len(arr) // 2]
    right_half = arr[len(arr) // 2:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge while there are elements in both lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append remaining elements, if any
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_list)
    print("Unsorted List:", unsorted_list)
    print("Sorted List:", sorted_list)