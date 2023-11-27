#importar as bibliotecas necessárias
import pyautogui
import time
import cv2 #opencv

#pausa segura
pyautogui.PAUSE = 2 
pyautogui.FAILSAFE = True#Ponto de salvamento seguro, caso atinja a coordenada zero zero

#abrir o Google Formulário para inserir os dados
#O formulário será aberto em seu navegador padrão

pyautogui.hotkey("win","r")
pyautogui.typewrite("https://docs.google.com/forms/d/e/1FAIpQLSdmzzuuV5NQmt8T43sWymRoDwqO6R6Do2ZztKvzEJEPSYEEEQ/viewform \n")
#https://docs.google.com/forms/d/e/1FAIpQLSdmzzuuV5NQmt8T43sWymRoDwqO6R6Do2ZztKvzEJEPSYEEEQ/viewform
#Esperar o intervalo de 5 segundos para que a pagina carregue
time.sleep(5)

#abre o arquivo csv  contendo os dados dos membros da bibliotecas.
with open("D:\CURSO\Automatizando Processos Criando Bots com Python\membros_biblioteca.csv") as f:#as f (para entender que a leitura é em linhas e colunas)
    #desconsidere a primeira linha(pular a primeira linha) ou seja pula a primeira linha
    next(f)#pulou para a segunda linha (pula o cabeçalho)
    #Para cada linha do arquivo csv
    for line in f:#Lê todas a linhas 
        #extrair os dados dos membros: nome, e-mail e telefone. Colete as informações necessárias
        line = line.strip()#strip para ler os caracteres
        line = line.split(';')#le os comandos e que são informações diferentes.
        
        #imprimir essas dados no terminal
        print("Dados: ", line)

        #Atribuir os dados do membro as variável
        name = line[0] # na posicao 0 (1 coluna) possui o nome
        email = line[1] # na posicao 1 (2 coluna) possui o email
        phone = line[2] #na posicao 2 (3 coluna) possui o telefone

        #localizar a imagem do campo "nome do funcinário" na tela
        #Clicar em sua resposta e cadastrar o dado

        pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\nome.png",confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\resposta.png",confidence=0.8), duration = 1)
        #digitar o nome do membro no campo "resposta"
        pyautogui.typewrite(name, interval=0.25)

        #localizar a imagem do campo "e-mail do funcinário" na tela
        #Clicar em sua resposta e cadastrar o dado
        pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\email.png", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\resposta.png", confidence=0.8), duration=1)
        #digitar o e-mail do membro no campo "resposta"
        pyautogui.typewrite(email, interval=0.25)

        #localizar a imagem do campo "Telefone do funcinário" na tela
        #Clicar em sua resposta e cadastrar o dado
        pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\telefone.png", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\resposta.png", confidence=0.8), duration=1)
        #digitar o telefone do membro no campo "resposta"
        pyautogui.typewrite(phone, interval=0.25)


        #Gerar uma captura de tela do formulário preenchido e salvar "cadastro_{nome}.png"
        pyautogui.screenshot(f"_cadastro_{name}.png")

        #clicar no botão enviar
        pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\enviar.png", confidence = 0.8), duration = 1)

        #ponto de espera sempre que for abrir uma nova pagina.
        time.sleep(3)

        #cadastrar um novo usuário: clicando no botão "outro cadastro"
        pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\CURSO\Automatizando Processos Criando Bots com Python\2 aula sincrona\img\outrocadastro.png", confidence = 0.8), duration =1)

#Exibe na tela uma msg de alerta informando que o programa foi finalizado com sucesso
pyautogui.alert(text="Cadastro finalizado com sucesso!", title='Aviso do Sistema', button="ok")