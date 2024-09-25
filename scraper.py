from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_announcements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://coe1.annauniv.edu/home/exp_msg_home.php')  
    time.sleep(5)  

  
    elements = driver.find_elements(By.CLASS_NAME, 'info')  
    announcements = [element.text for element in elements]

    driver.quit()
    return announcements
