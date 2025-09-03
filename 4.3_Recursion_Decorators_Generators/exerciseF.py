def merge(left, right):
    result = []
    pos_left = pos_right = 0

    while pos_left < len(left) and pos_right < len(right):
        if left[pos_left] < right[pos_right]:
            result.append(left[pos_left])
            pos_left += 1
        else:
            result.append(right[pos_right])
            pos_right += 1

    result += left[pos_left:]
    result += right[pos_right:]

    return result


def merge_sort(r_list):
    if len(r_list) <= 1:
        return r_list
    
    mid = len(r_list) // 2
    left = r_list[:mid]
    right = r_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == "__main__":
    result = merge_sort([3, 2, 1])
    print(result)