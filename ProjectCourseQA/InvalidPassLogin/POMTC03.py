"""
Author: Sergei Chernyahovsky
Date : 06\08\2022
# class to work with as an object for ELEMENTS

"""


class Elements:
    # PATH to target site
    pathURL = "https://www.scribens.com/"
    # find fields
    # successTitle = "Free, Powerful English Grammar Checker | SCRIBENS"
    callLoginField = "btncn"
    loginFieldByID = "inputIdC"
    passFieldByID = "inputMdpC"
    loginButtonByXPATH = "//*[@id='se-connecter-blocks']/td[1]/div[4]"
    # Valid Login
    loginAccount = "sergeicher87@gmail.com"
    loginPass = "Q1@3456q"
    # Invalid login
    loginAccountInvalid = "sergeicher@gmail.com"
    loginPassInvalid = "Q1@3456q123"
    textIcorredIdByXPATH = "//*[@id='LabelErrorId2']/b"
    textIcorredPassByXPATH = "//*[@id='LabelErrorId2']/b"
    # Successful login check
    successLoginById = "btnvp"
