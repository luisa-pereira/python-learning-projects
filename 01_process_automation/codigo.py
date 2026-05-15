# Passo a passo do seu programa (lógica de programação):

import pyautogui
import time
import pandas

#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta em um atalho (hotkey)

pyautogui.PAUSE = 0.5  #pausa a cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(448, 378)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Teste")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Abrir a base de dados
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto 
    #codigo
    pyautogui.click (x=431, y=260) #clicar no campo do código
    codigo = str(tabela.loc [linha, "codigo"]) #sempre entre colchetes [linha, coluna]
    pyautogui.write (codigo)
    #marca
    pyautogui.press ("tab") #passar para o próximo campo
    marca = str(tabela.loc [linha, "marca"])
    pyautogui.write (marca)
    #tipo
    pyautogui.press ("tab") #passar para o próximo campo
    tipo = str(tabela.loc [linha, "tipo"])
    pyautogui.write (tipo)
    #categoria
    pyautogui.press ("tab") #passar para o próximo campo
    categoria = str(tabela.loc [linha, "categoria"])
    pyautogui.write (categoria)
    #preço
    pyautogui.press ("tab") #passar para o próximo campo
    preco = str(tabela.loc [linha, "preco_unitario"])
    pyautogui.write (preco)
    #custo
    pyautogui.press ("tab") #passar para o próximo campo
    custo = str(tabela.loc [linha, "custo"])
    pyautogui.write (custo)
    #obs
    pyautogui.press ("tab") #passar para o próximo campo
    obs = str(tabela.loc [linha, "obs"])
    if obs != "nan":
        pyautogui.write (obs)
    pyautogui.press ("tab") #passar para o botão enviar
    pyautogui.press ("enter")

    #voltar para o início da tela
    pyautogui.scroll (5000)  #números positivos sobem na tela, negativos descem

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
