# OpenMRS  Login Automation

## Approach
This project automates the login process for the OpenMRS platform using Selenium. It includes tests for both successful and unsuccessful login attempts.

## Assumptions
- The OpenMRS platform is accessible at `https://qa.kenyahmis.org/openmrs/spa/login`.
- ChromeDriver is installed and configured correctly.

## Instructions

# Update package index
sudo apt update

# Install Python 3 and pip
sudo apt install -y python3 python3-pip

# Install Python virtual environment package
sudo apt install -y python3-venv

# Check Python and pip versions
python3 --version
pip3 --version

# Create and set up a virtual environment
mkdir myproject
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
deactivate

# Install ChromeDriver
sudo apt update
sudo apt install -y wget unzip
VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/${VERSION}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
chromedriver --version

# Install Selenium
source venv/bin/activate
pip install selenium
deactivate



### Setup
1. **Clone the repository:**
(https://github.com/vkemunto/workflows/blob/main/interview.py)
