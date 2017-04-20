from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

url = "http://www.ign.com/games/reviews"
driver.get(url)

all_titles = driver.find_elements_by_xpath("//div[@class='item-title']//a")
all_scores = driver.find_elements_by_xpath("//span[@class='scoreBox-score']")
all_descrip = driver.find_elements_by_xpath("//p[@class='item-details']")

f = open("IGN_scrape.txt", "w")
for title, score, descrip in zip(all_titles, all_scores, all_descrip):
    print >> f, "{}\n {}\n {}\n".format(title.text, score.text, descrip.text)
f.close()

driver.quit()

