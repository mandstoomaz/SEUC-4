contador = 0
contVermelha = 0
contVerde = 0
somaPressao = 0
qtdLidos = 0

def mediaPressao(somaPressao, qtdLidos):
     media = 0
     media = somaPressao / qtdLidos
     return media

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
        print("Classificação: Zona verde")
        contVerde += 1
    else:
        if pressao < 250:
            print("Classificação: Zona amarela")
        else:
            if pressao > 250:
                print("Classificação: Zona vermelha")
                contVermelha += 1
    return contVerde, contVermelha
        
        
		
leituras = int(input("Quantas leituras você vai querer realizar?: "))

while (leituras > contador):
    pressao = int(input("Digite a pressão: "))
    qtdLidos += 1
    pressaoAjustada = ajusteTermico(pressao)
    somaPressao += pressaoAjustada
    #função classificacao
    contVerde, contVermelha = classificacao(pressaoAjustada, contVerde, contVermelha)
    print(contVerde)
    print(contVermelha)
    # if para verificar a se há duas leituras consecutivas da Zona Vermelha
    if (contVermelha == 2):
        contador = leituras
    
    contador += 1
    
