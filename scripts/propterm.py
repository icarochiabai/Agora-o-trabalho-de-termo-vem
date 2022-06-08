import pyautogui, keyboard, time, os

def localizarJanela():
	files = os.listdir("./targets/janelas/")
	janela = None
	
	for f in files:
		if janela == None:
			janela = pyautogui.locateOnScreen("./targets/janelas/" + f, confidence=0.6)
		else:
			break

	return janela

def clicarEm(s, c, janela, conf=0.8):
	x_offset = -30
	y_offset = 0
	obj = pyautogui.locateCenterOnScreen("./targets/" + s + ".png", region=janela, confidence=conf)
	try:
		pyautogui.click(obj.x + x_offset, obj.y + y_offset, clicks=c)
	except:
		obj = pyautogui.locateOnScreen("./targets/error.png", 0.8)
		if obj != None:
			print("deu erro")
def digitarEm(s, texto, janela):
	clicarEm(s, 2, janela)
	pyautogui.typewrite(str(texto))

def calcularIsoterma():	
	tempInicial = float(input("Digite o valor da temperatura:\nExemplo: 123.4\n"))
	valorInicial = float(input("Digite o valor inicial para a pressão:\nExemplo: 70\n"))
	passo = float(input("Digite a variação de pressão a cada cálculo:\nExemplo: 0.1\n"))

	#1st Time
	janela = localizarJanela()
	digitarEm('k', tempInicial, janela)
	digitarEm('bar', valorInicial, janela)
	clicarEm('calcula', 1, janela)
	clicarEm('grava_valores', 1, janela)
	valorInicial -= passo	

	input("***************\nSalve o arquivo dentro da pasta isotermas.\nDigite enter AQUI quando terminar de salvar.\n***************\n")
	while valorInicial >= 1:
		if keyboard.is_pressed('alt'):
			break
		digitarEm('bar', valorInicial, janela)
		clicarEm('calcula', 1, janela)	
		clicarEm('grava_valores', 1, janela)
		valorInicial -= passo	
		valorInicial = round(valorInicial, 2)
		if valorInicial < 1:
			clicarEm('retorna', 2, janela)
			clicarEm('isotermas', 1, janela, 0.7)

def calcularEnvelope():
	tempCrit = float(input("Digite o valor crítico da temperatura:\nExemplo: 369.75\n"))
	valorInicial = float(input("Digite o valor inicial para a temperatura:\nExemplo: 200.0\n"))
	passo = float(input("Digite a variação de temperatura a cada cálculo:\nExemplo: -0.1\n"))
	
	#1st Time
	janela = localizarJanela()
	digitarEm('k', valorInicial, janela)
	clicarEm('calcula', 1, janela)
	clicarEm('grava', 1, janela)
	valorInicial -= passo	

	input("***************\nSalve o arquivo dentro da pasta envelope.\nDigite enter quando terminar de salvar.\n***************\n")
	
	while valorInicial <= tempCrit:
		if keyboard.is_pressed('alt'):
			break
		digitarEm('k', valorInicial, janela)
		clicarEm('calcula', 1, janela)
		clicarEm('grava', 1, janela)
		valorInicial -= passo	
		valorInicial = round(valorInicial, 2)
		if valorInicial < 1:
			clicarEm('retorna', 2, janela)

def calcular():
	escolha = int(input("Calcular para:\n[1] - Isotermas\n[2] - Envelope\n"))

	if escolha == 1:
		calcularIsoterma()

	elif escolha == 2:
		calcularEnvelope()

	mais = int(input("Deseja calcular mais?\n[1] - Sim\n[2] - Não\n"))
	if mais == 1:
		calcular()
	else:
		pass

calcular()
