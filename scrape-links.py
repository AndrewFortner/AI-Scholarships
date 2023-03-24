import time
from selenium import webdriver
from datetime import datetime

PATH = '/home/andrew/dev/chromedriver' #Path to chromedriver
driver = webdriver.Chrome(PATH)

scholarship_paths = ['/html/body/div[4]/div[1]/form/div[3]/div[4]/section[2]/div[2]/div/table/tbody/tr[{}]/td[1]/div/div[1]/a'.format(i) for i in range(1, 501)]

links = []
for i in range(1, 5):
    url = 'https://www.careeronestop.org/toolkit/training/find-scholarships.aspx?curPage={}&pagesize=500&studyLevelfilter=Bachelor~J~s%20Degree&georestrictionfilter=US&studyplacefilter=US'.format(i)
    driver.get(url)

    # Get xpaths to scholarship links
    xpaths = [driver.find_element('xpath', path) for path in scholarship_paths]
    links.append([path.get_attribute('href') for path in xpaths])

career_one_stop_links = []
for page in links:
    for link in page:
        career_one_stop_links.append(link)

links = career_one_stop_links

print(links)
with open('links.csv', 'w') as f:
    f.write(','.join(link for link in links))