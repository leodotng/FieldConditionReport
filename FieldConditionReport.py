# ***
# Field Condition Report Automated Entry
# Project runs Selenium browser
# Open URL https://opssuitemain.swacorp.com/station-management/conditions
# C:\Users\e86742\Desktop\Projects\pythonprojects\FieldConditionReport>
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


def opssuite_login():
    driver.get("https://opssuitemain.swacorp.com/station-management/conditions")
    driver.maximize_window()
    driver.find_element_by_id(
        "ContentPlaceHolder1_MFALoginControl1_UserIDView_txtUserid_UiInput").send_keys("E86742")
    driver.find_element_by_id(
        "ContentPlaceHolder1_MFALoginControl1_UserIDView_tbxPassword_UiInput").send_keys("Kotaemasu.8")
    driver.find_element_by_class_name("btn--login").click()


opssuite_login()

def clickFCR():
    driver.find_element("//*[contains(text(),'Create FCR')]").click()

clickFCR()
   




# finalDepartureRunways = []
# ArrivalRunways = []
# while True:
#     x = str(input("Please Enter a Departure Runway"))
#     y = str(input("Please Enter a Arrival Runways"))
#     break
# #locate Braking Action
# fcrURL = 'https://opssuitemain.swacorp.com/station-management/conditions'
# Click Create FCR
"""
Variables for Runways
"""
# Ensure Update radio button is selected
# Find Section
# Click within Ramp Section
"""
Braking Action Dropdown
Condition
Reported By
Observation Time 
Remarks
"""
# Click Add Runway Button
# Taxiway
# Format Time units
