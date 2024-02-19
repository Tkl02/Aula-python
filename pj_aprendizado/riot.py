from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.EdgeOptions()
options.add_argument('--log-level=3')


driver = webdriver.Edge(options=options)
driver.get("https://authenticate.riotgames.com/?client_id=player-support-zendesk&method=riot_identity&platform=web&redirect_uri=https%3A%2F%2Fauth.riotgames.com%2Fauthorize%3Fclient_id%3Dplayer-support-zendesk%26redirect_uri%3Dhttps%253A%252F%252Flogin.playersupport.riotgames.com%252Flogin_callback%26response_type%3Dcode%26scope%3Dopenid%2520email%26ui_locales%3Dpt-br%2520en-us")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "verificacao_boot")))

driver.execute_script("""
document.getElementById("verificacao_boot").style.display = "none";
""")

sleep(2)

login = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/div/div/div[1]/div[2]/div/input')
login.send_keys("diasgame006")
login.send_keys(Keys.RETURN)

sleep(0.5)

passwd = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/div/div/div[1]/div[3]/div/input')
passwd.send_keys("diasgamerbr0220")
passwd.send_keys(Keys.RETURN)

sleep(50)
driver.quit()