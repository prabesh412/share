import csv


with open('meroshare/spiders/dataset.csv', encoding="utf8") as file:
    reader = csv.reader(file)
    titles = []
    for row in reader:
        titles.append(row[0])
    title = str(titles[1:])

