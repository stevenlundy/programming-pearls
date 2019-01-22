import sys

def set_bit(bitmap, bit):
    return bitmap | 1<<int(bit)

def sort_file_on_disk(input_file, output_file):
    bitmap = 0

    with open(input_file) as f:
        for number in f:
            bitmap = set_bit(bitmap, number)

    with open(output_file, 'w') as f:
        for index, bit in enumerate(reversed("{0:b}".format(bitmap))):
            if bit is "1":
                f.write(str(index) + '\n')

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'out.txt'
    sort_file_on_disk(input_file, output_file)

if __name__ == "__main__":
    main()
