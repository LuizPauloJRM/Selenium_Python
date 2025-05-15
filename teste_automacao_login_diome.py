from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o navegador
driver = webdriver.Chrome()
driver.get("https://www.dio.me")

# Espera o botão "Entrar" aparecer e clica nele
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Entrar"))).click()

# Espera os campos de login aparecerem
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
senha_input = driver.find_element(By.ID, "password")

# Preenche os campos
email_input.send_keys("juninhopaulo55@hotmail.com")
senha_input.send_keys("Deusefiel100")

# Clica no botão "Entrar"
login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")
login_btn.click()

# Mantém o navegador aberto até você pressionar ENTER
input("Pressione ENTER para fechar o navegador...")

# Fecha o navegador
driver.quit()
