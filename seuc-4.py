contador = 0
contVermelha = 0
contVerde = 0
somaPressao = 0
qtdLidos = 0
menor = -1

def porcentagemZonaVerde(contVerde, qtdLidos):
    porcentagem = (contVerde / qtdLidos) * 100
    return porcentagem

def mediaPressao(somaPressao, qtdLidos):
     media = somaPressao / qtdLidos
     return media

def recebeMenorPressao(menor, pressao):
    if menor == -1:
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
    if pressao < 120:
         print("Classificação: Zona amarela (Oscilação)")
         contVermelha = 0
    else:
        if pressao <= 180:
            print("Classificação: Zona verde (Estável)")
            contVerde += 1
            contVermelha = 0
        else:
            if pressao < 250:
                print("Classificação: Zona amarela (Oscilação)")
                contVermelha = 0
            else:
                print("Classificação: Zona vermelha (Critíca)")
                contVermelha += 1
    return contVerde, contVermelha
        
        
		
leituras = int(input("Quantas leituras você vai querer realizar?: "))

while (leituras > contador):
    pressao = int(input("Digite a pressão: "))
    if pressao < 0:
        print("ERRO NA LEITURA: Valor de UPC Negativo detectado")
    else:
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
        
        # A menor pressão registrada durante todo o processo
        menor = recebeMenorPressao (menor, pressao)
        print(f"O menor é -> {menor}")
        
    contador += 1
    
    
if qtdLidos > 0:
    print("----------------- Métricas finais -----------------\n")
    print(f"\nMédia das pressões: {mediaPressao(somaPressao, qtdLidos):.2f}")
    print("\nMenor pressão registrada duranto todo o processo: ", menor)
    print(f"\nA porcentagem de leituras na Zona Verde: {porcentagemZonaVerde(contVerde, qtdLidos):.2f}%")
else:
    print("ALERTA: Nenhuma leitura válida foi registrada durante o turno, portanto não há MÉTRICAS FINAIS DO TURNO")
print(f"\nPercentual das leituras realizadas: {(qtdLidos / leituras) * 100:.2f}%\n")