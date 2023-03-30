import csv

#fiter out all lines which do not have "http://" in them
with open('filtered.csv', 'r') as f:
    reader = csv.reader(f)
    with open('new-filtered.csv', 'w') as f:
        writer = csv.writer(f)
        for row in reader:
            row.insert(-1, '|')
            writer.writerow(row)