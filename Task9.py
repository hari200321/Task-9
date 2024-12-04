''''
Task9.py
Program Name : Python Selenium automation code
DATE : 4-DEC- 2024
Programmer Name : Hari Prasad
Caveats : None
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class HariPrasad:
    def __init__(self,web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# The Automation start method
    def start (self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True


        except Exception:
            print("Check your code once!")
            return False
# The Automation Shutdown Method

    def shutdown(self):
        self.driver.quit()

# Method to Fetch the URL

    def fetch_url(self):
        if self.start():
            return self.driver.current_url
        else:
            return "Error: Unable to fetch the URL"

# Method to fetch the Title of the web application

    def fetch_title(self):
        if self.start():
            return self.driver.title
        else:
            return "Error: Unable to Fetch the Title!"


# Main Execution program

if __name__ == "__main__":

    url = "https://www.saucedemo.com/"

    hari = HariPrasad(url)

    print(hari.fetch_url())
    print(hari.fetch_title())