from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Scholarship:

    PATH = '/home/andrew/dev/chromedriver' #Path to chromedriver
    driver = webdriver.Chrome(PATH)

    def __init__(self, url):
        self.url = url
        self.driver.get(self.url)
        self.data = self.get_data()
        self.name = self.get_name()
        self.website = self.get_website()

    def get_data(self):
        d = {}
        for i in range(1, 25):
            label_xpath = '/html/body/div[4]/div[1]/form/div[3]/div[4]/section[1]/div/div/div/table/tbody/tr[{}]/td[1]'.format(i)
            data_xpath = '/html/body/div[4]/div[1]/form/div[3]/div[4]/section[1]/div/div/div/table/tbody/tr[{}]/td[2]'.format(i)
            try:
                label = self.driver.find_element('xpath', label_xpath).text
            except NoSuchElementException:
                break
            try:
                data = self.driver.find_element('xpath', data_xpath).text.replace(',', '')
                data = data.replace('\n', ' ')
            except NoSuchElementException:
                break
            d[label] = data
        return d

    def get_name(self):
        xpath = '/html/body/div[4]/div[1]/form/div[3]/div[4]/section[1]/div/div/div/table/thead/tr/th'
        element = self.driver.find_element('xpath', xpath)
        attribute = element.text
        self.data['Name'] = attribute
        return attribute
    
    def get_website(self):
        if 'Website' in self.data:
            return self.data['Website']
        elif 'For more information' in self.data:
            return self.data['For more information']
        else:
            return 'No website found'