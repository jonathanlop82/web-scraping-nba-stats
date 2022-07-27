from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = "https://www.nba.com/stats/"

player_table_stats = []
heads = []

driver = webdriver.Chrome(executable_path="/Users/tecnologia/WORKDIR/chromedriver")

driver.get(url)

player_stats = driver.find_element(by=By.XPATH, value='//*[@id="daily_leaders"]/div/div[1]/div[1]/a')

player_stats.click()

time.sleep(7)

table_heads = driver.find_elements(by=By.CSS_SELECTOR, value='div.nba-stat-table__overflow th')

for head in table_heads:
    heads.append(head.text)

table_players = driver.find_elements(by=By.CSS_SELECTOR, value='div.nba-stat-table__overflow tbody tr')

i = 0
temp = {}
for row in table_players:
    element = row.find_elements(by=By.CSS_SELECTOR, value='td')
    for value in element:
        temp[heads[i]] = value.text
        i += 1
        # print(value.text)
    player_table_stats.append(temp)
    temp = {}
    i = 0

print(heads)
print(player_table_stats)

with open('player_stats.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = heads)
    writer.writeheader()
    writer.writerows(player_table_stats)

driver.close()
driver.quit()