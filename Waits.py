# Waits are required to tell the script to wait for few seconds until and unless the data is loaded
# 3 types of waits:
# 1. Implicit wait / Global wait ==> selenium
# Setting wait for complete driver object so that it's applied globally to each & every test step of the file

# 2. Explicit wait ==> selenium
# Targeting specific element/elements to apply selenium wait explicitly
# It wont effect the other steps
# Defining explicit wait:
# Class named "WebDriverWait()", inside which deriver itself & time in sec is passed as parameter defines explicit wait
# Syntax: WebdriverWait(driver_name, time)

# 3. Using time class (it basically pauses the test for few seconds) ==> python


# Goal is to wait till the Promo code Applied message gets displayed
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# Invoking implicit wait for the complete driver object
# Declaring that: Wait until 5 seconds if object is not displayed
#driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

validate_text = 'applied'

# Entering characters and adding all displayed elements into the cart
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

# Waiting for the output to be displayed (implicit/explicit waits can be used as well)
#NOTE: Here, implicit or explicit won't work as both selenium waits only wait for the first element to be loaded
# and here we want all the element with "ber" as substring to be loaded properly before grabbing it
# this can only be done by fully haulting/pausing code execution for few seconds with time.sleep()
time.sleep(4)


# List of products displayed based on the search
# find_elements is used as it will pull all the elements
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
assert count == 3

# Adding all the items to the cart
selectingitems = driver.find_elements_by_xpath("//div[@class='products']/div/div[3]/button")

# 2nd option
# //div[@class='product-action']/button

for i in selectingitems:
    i.click()

# Opening the cart
driver.find_element_by_xpath("//img[@alt='Cart']").click()

# Proceed with the checkout
driver.find_element_by_css_selector("div[class='action-block'] button").click()

# Since, selenium is so fast it won't wait for seconds for the pages to be loaded
# Implicit/explicit wait can be used as well
#time.sleep(5)
# Explicit wait can also be defined here
wait = WebDriverWait(driver, 7)

# For Explicit wait, we can even define conditions until which we want to wait by using until() method
# Ex: We can ask to wait until alert is present, or element goes in clickable mode etc etc
# For this one more class is invoked: elements_conditions under which all these conditions are present
# Here, we want to wait textbox of promo code appears in the page as w/o mentioning wait it will fail
# Here, it will wait until element presence is located, i.e, until element is rendered on DOM
# Presence of element will be defined in parameter as locator
# We are telling that it will wait until the PromoCode ClassName is present as the located element
# Syntax: wait.until(expected_conditions.presence_of_element_located((By.locator, "locator_name")))
# (By.locator, "locator_name") must be passed as a single argument in the above method
# "By" is a class which helps us in identifying the locator with locator name
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))


# Putting text on promo code textbox
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()

# Wait
#time.sleep(6)
# Using same wait object we can recall explicit wait again in another element
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

promotext = driver.find_element_by_css_selector("span.promoInfo").text

assert validate_text in promotext




