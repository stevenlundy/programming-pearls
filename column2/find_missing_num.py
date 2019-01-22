import math

def find_missing_num(numbers, max_number, min_number=0):
    upper_bound = max_number
    lower_bound = min_number
    mid = (upper_bound + lower_bound) / 2.0

    while upper_bound > lower_bound:
        below = []
        above = []
        for n in numbers:
            if n > mid:
                above.append(n)
            else:
                below.append(n)

        if len(below) < len(above):
            numbers = below
            upper_bound = mid
        else:
            numbers = above
            lower_bound = mid
        mid = (upper_bound + lower_bound) / 2.0

        if len(numbers) == 0:
            return math.ceil(mid)

assert find_missing_num([1,4,2,3,8], 8) in [5, 6, 7]
assert find_missing_num([1,4,2,3,8,5,7], 8) in [6]
assert find_missing_num([1,4,2,3,6,5,7], 8) in [8]
assert find_missing_num([8,4,2,3,6,5,7], 8) in [1]
