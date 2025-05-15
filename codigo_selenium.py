from selenium import webdriver
import time
#Abrindo navehador
navegador = webdriver.Chrome()
#Acessando o site
navegador.get('https://www.hashtagtreinamentos.com/')
#Colocando navegador tela cheia 
navegador.maximize_window()
#selecionando o elemento
botao_verde=navegador.find_element("class name", "botao-verde").click()

#Tempo que mantem o navegador aberto
timesleep(20)