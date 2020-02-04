from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

url = "https://www.leboncoin.fr/recherche/?category=9&text=maison&owner_type=private&real_estate_type=1&square=50-max"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

