
def find_position(values, target):
    bottom = 0
    top = len(values) - 1
    while top >= bottom:
        middle = (top + bottom) // 2
        if values[middle] > target:
            top = middle - 1
        elif values[middle] < target:
            bottom = middle + 1
        else:  # values[middle] == target
            return middle
    return -1

assert find_position([1,2,3], 2) == 1
assert find_position([1,2,3,4], 2) == 1
assert find_position([1,3,4,5], 5) == 3
assert find_position([1,3,4,5], 1) == 0

assert find_position([1,3,4,5], 2) == -1
assert find_position([1,3,4,5], 7) == -1
assert find_position([1,3,4,5], 0) == -1
