from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome() 


def scrap():
    driver.get("https://www.leagueoflegends.com/en-us/news/tags/patch-notes/")
    time.sleep(1)

    # Hol den neusten Patch
    patch = driver.find_element(By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/div[2]/div/div[1]/div/ol/li[1]/a/article/div[2]/div/h2")
    patch.click()
    time.sleep(0.2)

    target_name = driver.find_elements(By.XPATH, "//*[@id='patch-notes-container']/div")



    with open("", "w",encoding='utf-8') as f:
        for name in target_name:
            f.write(name.text)
            f.write("\n" * 2)
            f.write("- - - - - - - - -")
            f.write("\n" * 2)




scrap()
