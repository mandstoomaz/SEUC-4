contador = 0
contVermelha = 0
contVerde = 0



def ajusteTermico(numPressao):
	if numPressao > 150:
		acrescimo = numPressao * 1.08
		return acrescimo
	else:
		reducao = numPressao * 0.96
		return reducao

def classificacao(numPressao, contVermelha, contVerde):
    if numPressao >= 120 and numPressao <= 180:
        print("Zona verde")
        contVerde += 1
    else:
        if numPressao < 250:
            print("Zona amarela")
        else:
            if numPressao > 250:
                print("Zona vermelha")
                contVermelha += 1
        
        
		
leituras = int(input("Quantas leituras você vai querer realizar?: "))

while (leituras < contador):
    pressao = int(input("Digite a pressão: "))
    pressaoAjustastada = ajusteTermico(pressao)
    #função classificacao
    # if para verificar a se há duas leituras consecutivas da Zona Vermelha
