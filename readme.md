# Kabum Store Automation

## Setup:
* Python 3
* Lib uiautomator (pip install uiautomator)
* PyTest (pip install pystest)
* Install Kabum store app on your Android mobile phone

## How to run the Test Cases:
1. Clone the project in any directory of your computer
2. Open a terminal inside the project folder
3. Plug your mobile phone on a USB port
4. Start the test cases running the command line 'pytest kabum.py'

## Why UiAutomator + Python?
Since I found Python I liked how it is easier to learn and to read, also the UiAutomator python wrapper makes me feel very confortable using it, the setup is easy and the understanding of what we can do is quickly learned thorugh the documentation.

# Kabum Store Automation + BDD Gherkin

Inside the folder features you'll find all files needed to run the test over BDD. For that please follow the instructions below:

1. You'll need to install 'behave' for that use: ```pip install behave```
2. Clone the project to any directory of your preference
3. Inside the folder 'features' run this command line: ```behave``` (yes, only that, if the setup was done correclty it will run the three test cases)
