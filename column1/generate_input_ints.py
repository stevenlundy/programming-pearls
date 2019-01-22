import sys
import random

def set_bit(bitmap, bit):
    return bitmap | 1<<int(bit)

def is_bit_set(bitmap, bit):
    return bool(bitmap & 1<<int(bit))

def generate_random_integers(quantity, max_number, output_file):
    bitmap = 0
    numbers_generated = 0
    while numbers_generated < quantity:
        new_number = random.randint(0, max_number)
        if not is_bit_set(bitmap, new_number):
            bitmap = set_bit(bitmap, new_number)
            numbers_generated += 1

    with open(output_file, 'w') as f:
        for index, bit in enumerate(reversed("{0:b}".format(bitmap))):
            if bit is "1":
                f.write(str(index) + '\n')

def main():
    quantity = sys.argv[1] if len(sys.argv) > 1 else 100000
    max_number = sys.argv[2] if len(sys.argv) > 2 else 1000000
    output_file = sys.argv[3] if len(sys.argv) > 3 else 'integers.txt'
    generate_random_integers(quantity, max_number, output_file)

if __name__ == "__main__":
    main()
