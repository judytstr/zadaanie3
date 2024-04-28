import csv
import sys

def read_csv(input_file):
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def apply_changes(data, changes):
    for change in changes:
        x, y, value = map(str.strip, change.split(','))
        data[int(y)][int(x)] = value
    return data

def write_csv(output_file, data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Użycie: python reader.py <plik_wejściowy> <plik_wyjściowy> <zmiana_1> <zmiana_2> ... <zmiana_n>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    data = read_csv(input_file)
    modified_data = apply_changes(data, changes)
    write_csv(output_file, modified_data)

    print("Z pliku", input_file + ":")
    for row in modified_data:
        print(','.join(row))