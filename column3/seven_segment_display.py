DIGITS = {
    0: 0b1111101,
    1: 0b1010000,
    2: 0b0110111,
    3: 0b1010111,
    4: 0b1011010,
    5: 0b1001111,
    6: 0b1101111,
    7: 0b1010100,
    8: 0b1111111,
    9: 0b1011110
}

def get_byte_array(number):
    byte_array = []
    while number > 0:
        byte_array.append(DIGITS(number % 10))
        number //= 10
    byte_array.reverse()
    return byte_array
