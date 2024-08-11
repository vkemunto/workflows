# OpenMRS  Login Automation

## Approach
This project automates the login process for the OpenMRS platform using Selenium. It includes tests for both successful and unsuccessful login attempts.

## Assumptions
- The OpenMRS platform is accessible at `https://qa.kenyahmis.org/openmrs/spa/login`.
- ChromeDriver is installed and configured correctly.

## Instructions


### Prerequisites
##Python 3.x
sudo apt update
sudo apt install -y python3 python3-pip
sudo apt install -y python3-venv
python3 --version
pip3 --version
mkdir myproject
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
deactivate

#ChromeDriver
sudo apt update
sudo apt install -y wget unzip
VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/${VERSION}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
chromedriver --version

#Selenium
pip install selenium


### Setup
1. **Clone the repository:**
(https://github.com/vkemunto/workflows/blob/main/interview.py)
