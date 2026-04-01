import pyautogui
from time import sleep

pyautogui.click(1021,617, duration=1)
pyautogui.write("123")
pyautogui.press('enter')
sleep(1)
pyautogui.click(1041,598, duration=2)
sleep(1)
pyautogui.click(111,105, duration=2)
sleep(1)
pyautogui.click(40,51, duration=1)
##Adicionar produtos
with open('itens_ti.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]

        pyautogui.click(216,84, duration=1)
        pyautogui.write(id_prod)
        pyautogui.click(217,152, duration=1)
        pyautogui.write(nome)
        pyautogui.click(209,217, duration=1)
        pyautogui.write(qntd)
        pyautogui.click(209,280, duration=1)
        pyautogui.write(preco)
        ##Clicar no salvar
        pyautogui.click(231,336)
        sleep(2)
        pyautogui.press('enter')