from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
# import urllib3
import urllib.request
import argparse

searchterm = 'forklift' # will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome(r'chromedriver_win32\chromedriver.exe')
browser.get(url)
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

save_dir = os.path.join('dataset', 'google_search1')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        # http = urllib3.PoolManager()
        # req = http.request('GET', url=Screencaps, headers=header)
        req = urllib.request.Request(img, headers=header)
        raw_img = urllib.request.urlopen(req).read()
        File = open(os.path.join(save_dir, searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(raw_img)
        File.close()
        succounter = succounter + 1
    except Exception as e:
            print(e)

print(succounter, "pictures succesfully downloaded")
browser.close()
