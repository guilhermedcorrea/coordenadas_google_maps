import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



#enderecos_df = pd.read_csv(r"D:\extracao_coordenadas\enderecos.csv",sep=";")
#print(enderecos_df)




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com.br/maps/preview")





driver.implicitly_wait(4)


   
dados = pd.read_csv("D:\extracao_coordenadas\enderecos.csv",sep=";")
lista_enderecos = dados['enderecos'].values.tolist()
lista_dicts = []
for lista_endereco  in lista_enderecos:
    print(lista_endereco)
    dicts = {}
    try:
        name = driver.find_element(By.NAME,"q")
        name.clear()
        name.send_keys(lista_endereco)
    except:
        pass

    dicts["nomebusca"] = lista_endereco
    time.sleep(2)
    try:
        confirm = driver.find_element(By.ID,"searchbox-searchbutton").click()
    except:
        pass
    time.sleep(2)
    try:
        confirm = driver.find_element(By.ID,"searchbox-searchbutton").click()
    except:
        pass
    
    try:
        endereco = driver.find_elements(
            By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div/div[2]/div[1]')[0].text
        print(endereco)
        dicts['endereco'] = endereco
    except:
        pass

    try:
        contato = driver.find_elements(
            By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/button/div/div[2]/div[1]')[0].text
        print(contato)
        dicts["contato"] = contato
        time.sleep(20)
    except:
        pass
    url_atual = driver.current_url
    dicts["url"] = url_atual
    coordenadas = str(url_atual).split("/@")[-1]
    
    
    dicts["coordenadas"] = coordenadas.split("/data")[0].split(",17z")[0]

    print(dicts)
    lista_dicts.append(dicts)

dados = pd.DataFrame(lista_dicts)
dados.to_csv("coleta4.csv")

    
