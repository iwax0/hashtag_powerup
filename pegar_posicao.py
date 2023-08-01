# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

# abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)


# Passo 2: Fazer login
pyautogui.click(x=1301, y=377)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("@1#$%62s")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de produtos para cadastrar
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=1288, y=275)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")
# Passo 5: Repetir o processo de cadastro até o fim

