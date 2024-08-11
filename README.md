# OpenMRS Login Automation

## Approach
This project automates the login process for the OpenMRS platform using Selenium. It includes tests for both successful and unsuccessful login attempts.

## Assumptions
- The OpenMRS platform is accessible at `https://qa.kenyahmis.org/openmrs/spa/login`.
- ChromeDriver is installed and configured correctly.

## Instructions

### Prerequisites

- **Selenium**
- **WebDriver**
- **Python**

### Installation Steps

```bash
sudo apt update
# Update package index
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Install Python virtual environment package
sudo apt install -y python3-venv

# Create and set up a Python virtual environment
mkdir myproject
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Install ChromeDriver
sudo apt install -y wget unzip
VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/${VERSION}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
chromedriver --version

# Install Selenium
pip install selenium



# Deactivate the virtual environment
deactivate
