# OpenMRS  Login Automation

## Approach
This project automates the login process for the OpenMRS platform using Selenium. It includes tests for both successful and unsuccessful login attempts.

## Assumptions
- The OpenMRS platform is accessible at `https://qa.kenyahmis.org/openmrs/spa/login`.
- ChromeDriver is installed and configured correctly.

## Instructions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")
try:
    username = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("admin")
    
    password = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("Admin123")
    
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )
    login_button.click()
    
    WebDriverWait(driver, 20).until(
        EC.title_contains("Home")
    )
    print("Login successful!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    input("Press Enter to close the browser...")
    driver.quit()
username.send_keys("wrong_user")
password.send_keys("wrong_password")
login_button.click()

error_message = driver.find_element(By.CLASS_NAME, "error-message").text
print(f"Error message displayed: {error_message}")

with open("test_report.txt", "w") as report:
    report.write("Login Test Report\n")
    report.write("---------------\n")

    if "Home" in driver.title:
        report.write("Test Passed: Login was successful.\n")
    else:
        report.write("Test Failed: Login was unsuccessful.\n")



### Prerequisites
- Python 3.x
- ChromeDriver

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/openmrs-automation.git
   cd openmrs-automation
