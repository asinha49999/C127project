from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
time.sleep(10)

def scrape():
    ulline = []
    for i in range(0,100):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        trtags = soup.find_all("tr") #bunch of rows
        for trtag in trtags: # each ultag
            listitems = trtag.find_all("td") # bunch of li tags
            templist = []
            for index,td_tag in enumerate(listitems): #each li tag
                if index==0:
                    templist.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(td_tag.contents[0])
                    except:
                        templist.append("")
            ulline.append(templist)
    
    headers = ["V Mag.","Proper name","Bayer designation",'Distance',"Spectral class","Mass","Radius","Luminosity"]    
    with open("Nasa.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(ulline)
scrape()