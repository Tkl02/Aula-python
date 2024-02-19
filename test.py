from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desabilita o log do webdriver
options = webdriver.EdgeOptions()
options.add_argument('--log-level=3')

# Cria o driver do Edge
driver = webdriver.Edge(options=options)

# Define a URL do site
url = "https://www.site.com/"

# Acessa o site
driver.get(url)

# Espera o elemento de verificação de boot aparecer
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "verificacao_boot")))

# Injeta JavaScript para ocultar o elemento de verificação de boot
driver.execute_script("""
document.getElementById("verificacao_boot").style.display = "none";
""")

# Interage com o site como de costume
# ...

# Fecha o driver
driver.quit()