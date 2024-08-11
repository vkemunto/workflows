from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Navigate to the OpenMRS login page
driver.get("https://qa.kenyahmis.org/openmrs/spa/login")

try:
    # Wait until the username field is visible
    username = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("admin")
    
    # Wait until the password field is visible and interactable
    password = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("Admin123")
    
    # Locate the login button and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )
    login_button.click()
    
    # Wait for the landing page to load and verify successful login
    WebDriverWait(driver, 20).until(
        EC.title_contains("Home")
    )
    print("Login successful!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Optionally, you can keep the browser open for debugging
    input("Press Enter to close the browser...")
    driver.quit()
 # Example of incorrect credentials
username.send_keys("wrong_user")
password.send_keys("wrong_password")
login_button.click()

# Check for error message
error_message = driver.find_element(By.CLASS_NAME, "error-message").text
print(f"Error message displayed: {error_message}")

# Create a simple log file
with open("test_report.txt", "w") as report:
    report.write("Login Test Report\n")
    report.write("---------------\n")

    if "Home" in driver.title:
        report.write("Test Passed: Login was successful.\n")
    else:
        report.write("Test Failed: Login was unsuccessful.\n")

