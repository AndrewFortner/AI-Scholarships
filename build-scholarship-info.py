import getInfo
from csv import writer

if __name__ == '__main__':
    #for each link in links.csv, create a Scholarship object from getInfo.py, and write it to scholarship-info.csv
    with open('links.csv', 'r') as f:
        links = f.read().split(',')
    with open('scholarship-info.csv', 'w') as f:
        wo = writer(f)
        for link in links:
            print(link)
            scholarship = getInfo.Scholarship(link)
            wo.writerow(['{}: {}'.format(key, val) for key, val in scholarship.data.items()])