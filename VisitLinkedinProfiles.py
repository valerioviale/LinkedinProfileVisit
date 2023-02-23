# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Start the webdriver
#driver = webdriver.Chrome("C:/Users/valerio/Desktop/Courses/LinkedinAuto/chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #starts the webdriver
# Open LinkedIn
driver.get("https://linkedin.com") #open a specific page


time.sleep(2)

# Locate the username and password fields and enter the credentials
username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys("YOURUSERNAME@gmail.com")
password.send_keys("YOURPASSWORD") 

time.sleep(6)

# Click the submit button to login
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click() #click on the submit button to login

time.sleep(10)

### end of the login process
import random

n_pages = 5 # number of pages you want to submit excluding the last one, range is not inclusive

# Loop through each page
for n in range(1, n_pages):
    # *** Add to the next line the page where you want to start to send messages, if you want to use recently added connection just remove +str(n)
    # and add https://www.linkedin.com/mynetwork/invite-connect/connections/
    driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103350119%22%5D&keywords=%22sustainability%20manager%22&origin=FACETED_SEARCH&page=" + str(n))
    
    # Wait for a random amount of time between 3 to 7 seconds before proceeding to the next step
    time.sleep(random.randint(3, 7))
    
    # Initialize an empty list for storing data
    data = []
    
    # Locate the elements and subtitles
    elements = driver.find_elements(By.CSS_SELECTOR, ".app-aware-link")

    # Click on each element to open in a new tab and then switch to that tab
    for element in elements:
        # Get the link to the profile
        link = element.get_attribute("href")
        
        # Open the link in a new tab
        driver.execute_script("window.open('" + link + "', 'new_window')")
        
        # Wait for a random amount of time between 3 to 7 seconds before proceeding to the next step
        time.sleep(random.randint(3, 7))
        
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        # Wait for a random amount of time between 3 to 7 seconds before proceeding to the next step
        time.sleep(random.randint(3, 7))
        
        # Close the current tab
        driver.close()
        
        # Switch back to the main tab
        driver.switch_to.window(driver.window_handles[0])
        
        # Wait for a random amount of time between 3 to 7 seconds before proceeding to the next step
        time.sleep(random.randint(3, 7))
