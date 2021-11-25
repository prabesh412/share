import csv


with open('meroshare/spiders/dataset.csv', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)