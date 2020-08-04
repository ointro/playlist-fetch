import requests
from bs4 import BeautifulSoup
import lxml
import time

print()
print()
print("Starting to fetch page")
target_page = 'https://nowyswiat.online/playlista/'

print("Target page is: {}".format(target_page))
print("=====================================================================================================")

source = requests.get(target_page).text
soup = BeautifulSoup(source, 'lxml')

div_page_content = soup.find('div', id="pageContent")
rows = div_page_content.find_all('tr')

timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = "/var/opt/playlist-fetch/playlist-{}.csv".format(timestr)

print("Creating file: {}".format(file_name))



with open(file_name, "w") as my_file:
    for row in rows:
        [td_time, td_info] = row.children
        rowText = "{}|{}|{}".format(td_time.text, td_info.b.text, td_info.contents[1].string.lstrip(" - "))
        print(rowText)
        my_file.write(rowText)

print("Saving file")
print("=====================================================================================================")