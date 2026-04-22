contador = 0
contVermelho = 0
contVerde = 0



def ajusteTermico(numPressao):
	if numPressao > 150:
		acrescimo = numPressao * 1.08
		return acrescimo
	else:
		reducao = numPressao * 0.96
		return reducao
		
leituras = int(input("Quantas leituras você vai querer realizar?: "))

while (leituras < contador):
    pressao = int(input("Digite a pressão: "))
    pressaoAjustastada = ajusteTermico(pressao)
    #função classificacao
    # if para verificar a se há duas leituras consecutivas da Zona Vermelha
    
    