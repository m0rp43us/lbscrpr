from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

url0="https://www.leboncoin.fr"
url = "https://www.leboncoin.fr/recherche/?category=9&text=maison&owner_type=private&real_estate_type=1&square=50-max"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(60)
driver.get(url)

pybutton = driver.find_elements_by_xpath("//*[contains(text(), 'Ventes immobilières')]")
print(pybutton)
pybutton.click()

