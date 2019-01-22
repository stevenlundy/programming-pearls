def flip_array_section(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1
    return array

def rotate_array(array, index):
    index = index % len(array)
    flip_array_section(array, 0, index - 1)
    flip_array_section(array, index, len(array) - 1)
    flip_array_section(array, 0, len(array) - 1)
    return array


