from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.thesparksfoundationsingapore.org/")

print("|| Test Cases ||\n")

#Test Case 1 : To verify the existence of the logo
print("|| Test Case 1 ||\n")
try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/h1/a/img')
    print("Logo Verification Successful !!\n")
except NoSuchElementException:
    print("The Logo does not exist !!\n")

#Test Case 2 : To verify if the navigation bar appears
print("|| Test Case 2 ||\n")
try:
    driver.find_element(By.CLASS_NAME, "navbar-brand")
    print("Navigation Bar Verification Successful !!\n")
except NoSuchElementException:
    print("The Navigation Bar does not exist !!\n")

# Test Case 3 : Navigate to About Us Page
print("|| Test Case 3 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "About Us").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Executive Team").click()
    time.sleep(5)
    print("\'Executive Team\' Section Visit Successful !!\n")
    print("\'About Us\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Executive Team\' Page does not exist !!\n")

# Test Case 4 : Navigate to Programs Page
print("|| Test Case 4 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "Programs").click()
    time.sleep(5)
    try:
        driver.find_element(By.LINK_TEXT, "Student Scholarship Program").click()
        time.sleep(5)
        print("\'Student Scholarship Program\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Student Scholarship Program\' Section does not exist !!\n")

    try:
        driver.find_element(By.LINK_TEXT, "Internship Program").click()
        time.sleep(5)
        print("\'Internship Program\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Internship Program\' Section does not exist !!\n")

    try:
        driver.find_element(By.LINK_TEXT, "Workshops").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Career Choices").click()
        time.sleep(5)
        print("\'Career Choices\' Section Visit Successful !!\n")
        w = driver.window_handles
        print("Tab has changed. Move to Original tab and continue testing there. \n")
        time.sleep(5)
        driver.switch_to.window(w[0])
        time.sleep(5)
        print("We are back to the Original tab. \n")
        time.sleep(5)
    except NoSuchElementException:
        print("\'Career Choices\' Page does not exist !!\n")

    print("\'Programs\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Programs\' Page does not exist !!\n")

# Test Case 5 : Navigate to Polices and Code Page
print("|| Test Case 5 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "Policies and Code").click()
    time.sleep(5)
    try:
        driver.find_element(By.LINK_TEXT, "Whistle Blowing Policy").click()
        time.sleep(5)
        print("\'Whistle Blowing Policy\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Whistle Blowing Policy\' Section does not exist !!\n")

    try:
        driver.find_element(By.LINK_TEXT, "Service Quality Values").click()
        time.sleep(5)
        print("\'Service Quality Values\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Service Quality Values\' Section does not exist !!\n")

    print("\'Policies and Code\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Policies and Code\' Page does not exist !!\n")


# Test Case 6 : Navigate to LINKS Page
print("|| Test Case 6 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "LINKS").click()
    time.sleep(5)
    try:
        driver.find_element(By.LINK_TEXT, "AI in Education").click()
        time.sleep(5)
        print("\'AI in Education\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'AI in Education\' Section does not exist !!\n")

    try:
        driver.find_element(By.LINK_TEXT, "Salient Features").click()
        time.sleep(5)
        print("\'Salient Features\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Salient Features\' Section does not exist !!\n")

    print("\'LINKS\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'LINKS\' Page does not exist !!\n")

# Test Case 7 : Navigate to Contact Us Page
print("|| Test Case 7 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(5)
    ad = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/p")
    time.sleep(5)
    if ad.text == "THE HANGAR, NUS ENTERPRISE\n21 HENG MUI KENG TERRACE, SINGAPORE, 119613":
        print("The Contact Address is Correct !!")
    else:
        print("The Contact Address is NOT Correct !!")

    print("\'Contact Us\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Contact Us\' Page does not exist !!\n")

# Test Case 8 : Navigate to Join Us Page
print("|| Test Case 8 ||\n")
try:
    driver.find_element(By.LINK_TEXT, "Join Us").click()
    time.sleep(5)

    try:
        driver.find_element(By.LINK_TEXT, "Events Volunteer").click()
        time.sleep(5)
        driver.find_element(By.NAME, "Name").send_keys('Emma Chaplin')
        time.sleep(5)
        driver.find_element(By.NAME, "Email").send_keys('emchap@letsmail.com')
        time.sleep(5)
        sel = Select(driver.find_element(By.CLASS_NAME, "form-control"))
        time.sleep(5)
        sel.select_by_visible_text("Volunteer")
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "button-w3layouts").click()
        time.sleep(5)
        print("Form Verification Successful !!")
        time.sleep(5)
        print("\'Events Volunteer\' Section Visit Successful !!\n")
    except NoSuchElementException:
        print("\'Events Volunteer\' Section does not exist !!\n")

    print("\'Join Us\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Join Us\' Page does not exist !!\n")

# Test Case 9 : Navigate to Home Page via Home button and print page-title
print("|| Test Case 9 ||\n")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT, "The Sparks Foundation").click()
    time.sleep(5)
    print("We are back to Home Page. Home button Verification Successful !!")

    if driver.title:
        print("Title is : ")
        print(driver.title)
    else:
        print("Page title is NOT Correct.")

    print("\'Home\' Page Visit Successful !!\n")
except NoSuchElementException:
    print("\'Home\' Page does   not exist !!\n")