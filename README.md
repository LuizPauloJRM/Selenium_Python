# Selenium_Python
Automatizando tarefas com  ferramenta selenium python , controlando seu navegador 
O que é

Instalação

Configuração do WebDriver

Exemplos práticos

Boas práticas

Dicas extras

Você pode usar esse README para seus projetos ou estudos.

📄 README.md – Selenium com Python
markdown
Copiar
Editar
# Selenium com Python 🐍🧪

Automação de navegadores com Selenium em Python – ideal para testes, scraping e tarefas repetitivas na web.

---

## 🚀 O que é Selenium?

Selenium é uma ferramenta de automação que permite controlar navegadores por código. Com ele, você pode:

- Acessar sites automaticamente
- Preencher e enviar formulários
- Clicar em botões e links
- Fazer login automático
- Capturar dados de páginas (web scraping)
- Testar aplicações web de forma automatizada

---

## 📦 Instalação

### 1. Instale o Selenium:
```bash
pip install selenium
2. Instale o WebDriver (ChromeDriver ou outro)
Chrome:
Acesse: https://sites.google.com/chromium.org/driver/

Baixe a versão compatível com seu Google Chrome

Extraia o executável e adicione ao seu PATH, ou especifique o caminho no script:

python
Copiar
Editar
driver = webdriver.Chrome(executable_path="caminho/para/chromedriver.exe")
✅ Exemplo básico
python
Copiar
Editar
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o navegador
driver = webdriver.Chrome()

# Abre um site
driver.get("https://www.google.com")

# Espera alguns segundos
time.sleep(2)

# Encontra o campo de busca e faz uma pesquisa
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.submit()

# Aguarda e fecha
time.sleep(5)
driver.quit()
📚 Comandos comuns
Acessar elementos:
python
Copiar
Editar
driver.find_element(By.ID, "elemento_id")
driver.find_element(By.NAME, "elemento_nome")
driver.find_element(By.CLASS_NAME, "classe_css")
driver.find_element(By.LINK_TEXT, "Texto do link")
driver.find_element(By.XPATH, "//tag[@atributo='valor']")
Interações:
python
Copiar
Editar
element.send_keys("texto")  # Digitar
element.click()             # Clicar
element.clear()             # Limpar campo
⏱️ Esperas
1. Espera fixa (não recomendada sempre)
python
Copiar
Editar
import time
time.sleep(3)
2. Espera explícita (melhor prática)
python
Copiar
Editar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
📌 Automatizando Login (Exemplo DIO)
python
Copiar
Editar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.dio.me")

# Clica em "Entrar"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Entrar"))).click()

# Preenche e envia o login
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
senha = driver.find_element(By.ID, "password")
email.send_keys("seuemail@exemplo.com")
senha.send_keys("suaSenha123")

driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]").click()

input("Pressione ENTER para fechar...")
driver.quit()
💡 Dicas
Use input() no fim do script para evitar que o navegador feche automaticamente.

Use try/except para tratar erros de carregamento.

Combine Selenium com BeautifulSoup para scraping mais avançado.

Para testes automatizados, integre com frameworks como pytest.

🧰 Recursos úteis
Documentação oficial: https://www.selenium.dev/documentation/webdriver/

XPATH Cheatsheet: https://devhints.io/xpath

Ferramentas para encontrar seletores: DevTools do navegador (F12 > Inspecionar)

📁 Estrutura recomendada de projeto
bash
Copiar
Editar
selenium-automacao/
│
├── drivers/
│   └── chromedriver.exe
│
├── scripts/
│   └── login_dio.py
│
├── requirements.txt
└── README.md
✅ Requisitos
Python 3.7+

Google Chrome (ou outro navegador)

ChromeDriver (ou outro WebDriver compatível)

Selenium (pip install selenium)

🔐 Segurança
Nunca compartilhe senhas em texto no código. Use variáveis de ambiente:

python
Copiar
Editar
import os
senha = os.getenv("SENHA_DIO")
🧪 Exemplo de teste automatizado com pytest
python
Copiar
Editar
def test_titulo():
    driver = webdriver.Chrome()
    driver.get("https://dio.me")
    assert "DIO" in driver.title
    driver.quit()
👨‍💻 Autor
Luiz Paulo Medeiros da Cunha Júnior
Seu portfólio • Desenvolvedor Web Fullstack

yaml
Copiar
Editar

---

Se quiser, posso gerar o arquivo `README.md` automaticamente ou adaptá-lo com mais foco em scraping, testes automatizados, ou integração com `pytest`. Deseja que eu adicione mais exemplos avançados ou publique esse conteúdo num repositório?








