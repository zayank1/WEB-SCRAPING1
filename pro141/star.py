import pandas as pd
from selenium import webdriver
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.get(START_URL)
headers = ["Name","Distance","Mass","Radius"]

star_data = []

for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        star_data.append(temp_list)
browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


planet_df_1 = pd.DataFrame(star_data,columns=headers)


planet_df_1.to_csv("planets.csv",index=True,index_label="id")