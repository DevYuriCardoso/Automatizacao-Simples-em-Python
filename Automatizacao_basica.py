#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pyautogui
import time
import pyperclip

#pyautogui.click -> Clicar com o mouse 
#pyautogui.write -> Escrever um texto
#pyautogui.press -> Apertar uma tecla 
#pyautogui.hotkey-> Apertar uma Combinação de teclas

#Passo 1 : Acessar o Sistema 
#pyautogui.press ("win")
#pyautogui.write ("Opera")
#pyautogui.press ("enter")

pyautogui.PAUSE = 0.5

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter") 
time.sleep(2)


#Passo 2 : Fazer Login no Sistema
pyautogui.click (x=603, y=351)
pyautogui.write ("Irineu")
pyautogui.click (x=639, y=423)
pyautogui.write ("Você Não Sabe Nem Eu")
pyautogui.click (x=648, y=486)

#Passo 3 : Baixar a Base De Dados
time.sleep(10)
pyautogui.click (x=520, y=318,button = "right")
pyautogui.click (x=629, y=607)
time.sleep(4)
pyautogui.press("enter") 
time.sleep(2)
pyautogui.click (x=542, y=48)








# In[54]:


#Passo 4 : Calculas os Indicadores 
import pandas as pd

tabelas = pd.read_csv(r"C:\Users\yuris\Documents\FaculdadeCiênciadaComputação\Python\Compras.csv", sep= ";")
display(tabelas)
#Calcular Indicadores 
#Total Gasto ->Somar Coluna Valor Final
totalGasto = tabelas ["ValorFinal"].sum()
#Quantidade  ->Somar Coluna Quantidade
quantidade = tabelas ["Quantidade"].sum()
#Preço Medio -> Total Gasto / Quantidade 
precoMedio = totalGasto / quantidade




# In[55]:


#Passo 5 : Enviar o Email para o diratório. 

#Entrar no Email 
pyautogui.hotkey("ctrl","t")
time.sleep(2)
pyautogui.click (x=542, y=48)

pyautogui.write("https://mail.google.com/mail/u/0/")
pyautogui.hotkey("enter")
time.sleep(4)
#Clicar em Escrever 
pyautogui.click(x=50, y=159)
time.sleep(4)
pyautogui.write("lixeiradoyuno@gmail.com")
time.sleep(3)
pyautogui.hotkey("tab")
time.sleep(2)

pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(1)
pyautogui.write("Relatório de Compra")
time.sleep(1)
pyautogui.hotkey("tab")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
texto1 = """Prezados, segue o relatório de compra:
total gasto :
Quantidade de produto :
Preço médio :
Ass: Yuri Cardoso"""
pyperclips = texto1
pyperclip.copy(pyperclips)
pyautogui.hotkey("ctrl","v")

#Preencher Email 

#Enviar Email 


# In[56]:


x=520, y=318!pip install pyautogui


# In[ ]:


time.sleep(5)
print (pyautogui.position())


# In[ ]:




