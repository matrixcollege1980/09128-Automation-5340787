from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")


def Youtube():
    search_youtube = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
    search_youtube.send_keys("pytest")
    search_youtube.click()
