contador = 0
contVermelha = 0
contVerde = 0
somaPressao = 0
qtdLidos = 0
menor = 0

def porcentagemZonaVerde(contVerde, qtdLidos):
    porcentagem = 0
    porcentagem = (contVerde / qtdLidos) * 100
    return porcentagem

def mediaPressao(somaPressao, qtdLidos):
     media = 0
     media = somaPressao / qtdLidos
     return media

def recebeMenorPressao(menor, pressao):
    if menor == 0:
        menor = pressao
    else:
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
        print("Classificação: Zona verde (Estável)")
        contVerde += 1
    else:
        if pressao < 250:
            print("Classificação: Zona amarela (Oscilação)")
        else:
            if pressao > 250:
                print("Classificação: Zona vermelha (Critíca)")
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
        print("\nPrograma interrompido por 2 leituras consecutivas da Zona Vermelha\n")

    contador += 1
    # A menor pressão registrada durante todo o processo
    menor = recebeMenorPressao (menor, pressaoAjustada)
    print(f"O menor é -> {menor}")
    

print("----------------- Métricas finais -----------------\n")
print(f"\nMédia das pressões: {mediaPressao(somaPressao, qtdLidos):.2f}")
print("\nMenor pressão registrada duranto todo o processo: ", recebeMenorPressao(pressao))
print(f"\nA porcentagem de leituras na Zona Verde: {porcentagemZonaVerde(contVerde, qtdLidos):.2f}%")
print(f"\nPercentual das leituras realizadas: {leituras/qtdLidos:.2f}%\n")