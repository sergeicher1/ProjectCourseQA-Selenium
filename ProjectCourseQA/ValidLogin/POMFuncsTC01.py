"""
Author: Sergei Chernyahovsky
Date : 06\08\2022
# Functions to call from main file.

"""


from datetime import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import *
from POMTC01 import *

ser = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=ser)


# create logging file
def createLog():
    with open("LogValidLogin.txt", "w") as newFile:
        newFile.write(f"\t\t{datetime.now()}  " + "Log File - start logging")


# Log the appropriate message
def logMessage(message):
    with open("LogValidLogin.txt", "a") as newFile:
        newFile.write(f"\n{datetime.now()} " + message)


# open web
def openWeb():
    print("Creating log file")
    createLog()
    print("Opening the browser")
    logMessage(message="Opening the browser - PASS")
    driver.get(Elements.pathURL)
    print("Entering the path to target site")
    logMessage(message="Entering the path to target site - PASS")
    driver.maximize_window()
    print("Maximizing the window for better look")
    logMessage(message="Maximizing the window for better look - PASS")
    # wait for complete load of the site, take screenshot and write to log
    sleep(3)
    print("Waiting 3 seconds to allow website to fully load")
    logMessage(message="Waiting 3 seconds to allow website to fully load - PASS")
    driver.get_screenshot_as_file("Successful load of the web.png")
    print("Creating \"png\" screenshot of successful page load")
    logMessage(message="Successful web open - PASS")
    print("Logging...")
    print("Successful web open")


# function  to validate a valid login
def validLogin():
    # Doesn't work on my machine
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located(Elements.callLoginField)).click()
    # WebDriverWait(driver, 10).until(EC.alert_is_present()).click()

    logingLink = driver.find_element(By.ID, Elements.callLoginField)
    print("Finding the link button to popup the login form")
    logMessage(message="Finding the link button to popup the login form - PASS")
    logingLink.click()
    print("Clicking...")
    logMessage(message="Clicking the link - PASS")
    sleep(1)
    driver.get_screenshot_as_file("Login form popup showed up.png")
    print("Creating screenshot...")
    logMessage(message="Creating screenshot... - PASS")
    logMessage(message="Clicking the login link to popup \"LOG IN\" window - PASS")
    logMessage(message="The window is popped up successfully with screenshot created- PASS")

    loginField = driver.find_element(By.ID, Elements.loginFieldByID)
    loginField.clear()
    print("Clearing the field...")
    logMessage(message="Clearing email address field - PASS")
    loginField.send_keys(Elements.loginAccount)
    driver.get_screenshot_as_file("Entered data to email field.png")
    print("Sending text to email field: sergeicher87@gmail.com")
    logMessage(message="Entering text to email field: sergeicher87@gmail.com - PASS")
    sleep(1)

    passField = driver.find_element(By.ID, Elements.passFieldByID)
    passField.clear()
    print("Clearing the field...")
    logMessage(message="Clearing password field - PASS")
    passField.send_keys(Elements.loginPass)
    driver.get_screenshot_as_file("Entered data to password field.png")
    print("Sending text to password field: Q1@3456q")
    logMessage(message="Entering text to password field: Q1@3456q - PASS")
    sleep(1)

    print("Finding the login button to click")
    logMessage(message="Finding the login button to click - PASS")
    loginButton = driver.find_element(By.XPATH, Elements.loginButtonByXPATH)
    loginButton.click()
    print("Clicking... Login button")
    logMessage(message="Clicking... Login button - PASS")
    sleep(3)
    if driver.find_element(By.ID, Elements.successLoginById):
        print("Taking the screenshot of successful login")
        logMessage(message="Taking the screenshot of successful login - PASS")
        logMessage(message="Successfully logged in - PASS")
        driver.get_screenshot_as_file("Successfully logged in.png")
        logMessage(message="End of program, closing the web - PASS")
        print("End of program, closing the web")
    else:
        print("Taking the screenshot of Unsuccessful login")
        logMessage(message="Taking the screenshot of Unsuccessful login - FAIL")
        driver.get_screenshot_as_file("Not logged in.png")
        logMessage(message="End of program, closing the web - PASS")
        print("End of program, closing the web")


# close web
def closeWeb():
    sleep(10)
    driver.quit()
