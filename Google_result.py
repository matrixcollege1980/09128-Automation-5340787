from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")

def google_search():
    SearchBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span/svg')
    SearchBtn.send_keys("Github Tutorial")
    SearchBtn.click()
