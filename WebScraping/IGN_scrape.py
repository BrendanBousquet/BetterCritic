from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

url = "http://www.ign.com/games/reviews"
driver.get(url)


all_titles = driver.find_elements_by_xpath("//div[@class='item-title']//a")
all_scores = driver.find_elements_by_xpath("//span[@class='scoreBox-score']")

for title, score in zip(all_titles, all_scores):
    print("{}, {}".format(title.text, score.text))

driver.quit()

