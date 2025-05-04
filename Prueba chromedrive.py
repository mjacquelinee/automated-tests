from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("")
driver.close()

