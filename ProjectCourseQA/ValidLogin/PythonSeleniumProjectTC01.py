"""
Author: Sergei Chernyahovsky
Date : 06\08\2022
# MAIN program, here you import only POM - Functions and work with them. ENJOY!
Login to site with VALID data

"""

from POMFuncsTC01 import *
from datetime import *

# call the functions from POM
try:
    openWeb()
except:
    print("Something went wrong...Creating screenshot")
    driver.get_screenshot_as_file("Unsuccessful openWeb.png")
    print("Writing to Log file")
    logMessage(message="Unsuccessful web open - FAIL")
    print("The web didn't open, check the screenshot and log file")

try:
    validLogin()
except:
    print("Something went wrong...Creating screenshot")
    driver.get_screenshot_as_file("validLogin FAILED.png")
    print("Writing to Log file")
    logMessage(message="validLogin FAILED - FAIL")
    print("The successful login failed, check the screenshot and log file")

try:
    closeWeb()
except:
    driver.get_screenshot_as_file("Unsuccessful closeWeb.png")

# write to Final Results file
try:
    # in next call just append instead of create new one
    with open(r"D:\ProjectCourseQA\FinalResults.txt", "w") as newFile:
        newFile.write(f"\t\t{datetime.now()}  " + "Final Results.")

    with open("LogValidLogin.txt", "r") as newFile:
        content = newFile.read()
        if "FAIL" in content:
            print("Test Case - 01 FAILED!")
            with open(r"D:\ProjectCourseQA\FinalResults.txt", "a") as file:
                file.write(f"\n{datetime.now()}" + " Test Case 01: The validLogin Test Case FAILED!")
        else:
            print("Test Case - 01 PASSED!")
            with open(r"D:\ProjectCourseQA\FinalResults.txt", "a") as file:
                file.write(f"\n{datetime.now()}" + " Test Case 01: The validLogin Test Case PASSED!")
except:
    print("Problem adding the results to Final Results file")
