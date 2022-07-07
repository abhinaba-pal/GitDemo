from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Creating xpath with common locator to capture the complete list of check boxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

# Number of checkboxes present on the page
print(len(checkboxes))

# It will select all the check boxes with the help of common locator
#  for i in checkboxes:
#   i.click()

# Selecting particular checkboxes [Here, "Option 2"]
# 2 ways: 1. Selecting directly via., dedicated attribute
# driver.find_element_by_id("checkBoxOption2").click()

# 2. For looping through the check boxes dynamically and selecting it
for i in checkboxes:

    # Extracting the required attribute
    if i.get_attribute('value') == 'option2':
        i.click()

        # Checking the condition inside the loop so, validation should be done inside the loop only
        #assert i.is_selected()


# Radio buttons and check boxes are handled in the same way
# NOTE: Radio button is static, i.e., only one option can be selected at a time so iterables/loops doesn't work here
# Radio button is validated in basic way
#radiobutton = driver.find_elements_by_xpath("//input[@name='radioButton']")

# It is a list object, so we can directly select via., index position
#radiobutton[1].click()

#assert radiobutton[1].is_selected()


# To check if the selection was successfully happened or not. How do you validate?
# is_selected() method will tell whether the specific checkboxes are selected or not
# assertion will tell if its selected or not, if not it will give assertion error of being FALSE and test will fail
# assert i.is_selected()





