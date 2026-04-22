contador = 0
contVermelha = 0
contVerde = 0
somaPressao = 0

def receberMenorPressao(pressao):
    menor = 99999999
    if pressao < menor:
        menor = pressao
        return menor

def ajusteTermico(pressao):
	if pressao > 150:
		acrescimo = pressao * 1.08
		return acrescimo
	else:
		reducao = pressao * 0.96
		return reducao

def classificacao(pressao, contVerde, contVermelha):
    if pressao >= 120 and pressao <= 180:
        print("Zona verde")
        contVerde += 1
        return contVerde
    else:
        if pressao < 250:
            print("Zona amarela")
        else:
            if pressao > 250:
                print("Zona vermelha")
                contVermelha += 1
                return contVermelha
        
        
		
leituras = int(input("Quantas leituras você vai querer realizar?: "))

while (leituras < contador):
    pressao = int(input("Digite a pressão: "))
    pressaoAjustada = ajusteTermico(pressao)
    somaPressao += pressaoAjustada
    #função classificacao
    classificacao(pressaoAjustada, contVerde, contVermelha)
    # if para verificar a se há duas leituras consecutivas da Zona Vermelha
