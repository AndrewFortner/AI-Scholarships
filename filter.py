import csv

#fiter out all lines which do not have "http://" in them
with open('scholarship-info.csv', 'r') as f:
    reader = csv.reader(f)
    with open('filtered.csv', 'w') as f:
        writer = csv.writer(f)
        for row in reader:
            for item in row:
                if 'http://' in item:
                    split = item.split(' ')
                    link = ''
                    for i in range(len(split)):
                        if 'http://' in split[i]:
                            link = split[i]
                            break
                    row.insert(0, "Link: {}".format(link))
                    writer.writerow(row)
                    break