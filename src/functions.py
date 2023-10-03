import csv


def csv_reader():
    with open('items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'name' and 'price' and 'quantity' in row:
                continue
            else:
                print(row)

print(csv_reader())