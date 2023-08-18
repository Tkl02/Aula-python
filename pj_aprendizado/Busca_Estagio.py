from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Options = Options()

Options.add_argument("start-maximized")
Options.add_argument("disable-notifications")
Options.add_argument("disable-extensions")
Options.add_argument("disable-gpu")
# Options.add_argument("useAutomationExtension", False)
# Options.add_argument("excludeSwitches", ['enable-logging'])
Options.add_argument("user-agent=Chrome/116.0.5845.97 ")



driver = webdriver.Chrome(options=Options)

driver.get("https://br.indeed.com/")

input("close the page")
driver.close()