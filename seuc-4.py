contador = 0
altaPressao = 0
baixaPressao = 0
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

def classificacao(pressao, contVerde, baixaPressao, altaPressao):
    if pressao < 90:
        print("Classificação: ZONA AZUL (Crítica - Cristalização)")
        altaPressao = 0
        baixaPressao += 1
    else:
        if pressao < 120:
            print("Classificação: ZONA AMARELA (Oscilação de Baixa Pressão)")
            altaPressao = 0
        else:
            if pressao <= 180:
                print("Classificação: ZONA VERDE (Estável)")
                contVerde += 1
                altaPressao = 0
            else:
                if pressao < 250:
                    print("Classificação: ZONA AMARELA (Oscilação de Alta Pressão)")
                    altaPressao = 0
                else:
                    print("Classificação: ZONA VERMELHA (Crítica - Alta Pressão)")
                    altaPressao += 1
    return contVerde, baixaPressao, altaPressao      
        
		
leituras = int(input("Quantas leituras você realizará neste turno?: "))

while (leituras > contador):
    pressao = int(input("Digite a pressão: "))
    if pressao < 0:
        print("ERRO NA LEITURA: Valor de UPC Negativo detectado")
    else:
        qtdLidos += 1
        pressaoAjustada = ajusteTermico(pressao)
        somaPressao += pressaoAjustada
        
        #função classificacao
        contVerde, baixaPressao, altaPressao = classificacao(pressaoAjustada, contVerde, baixaPressao, altaPressao)
        print(contVerde)
        print(altaPressao)
        
        # if para verificar a se há duas leituras consecutivas da Zona Vermelha
        if (altaPressao == 2):
            contador = leituras
            print("\nPrograma interrompido por 2 leituras consecutivas da Zona Vermelha\n")

        if (baixaPressao == 1):
            contador = leituras
            print("\nPRESSÃO CAIU DEMAIS! Fluxo interrompido por perigo de cristalização\n")
        
        # A menor pressão registrada durante todo o processo
        menor = recebeMenorPressao (menor, pressao)
        print(f"O menor é -> {menor}")
        
    contador += 1
    
    
if qtdLidos > 0:
    print("----------------- Métricas finais     -----------------\n")
    print(f"\nMédia das pressões: {mediaPressao(somaPressao, qtdLidos):.2f}")
    print("\nMenor pressão registrada duranto todo o processo: ", menor)
    print(f"\nA porcentagem de leituras na Zona Verde: {porcentagemZonaVerde(contVerde, qtdLidos):.2f}%")
else:
    print("ALERTA: Nenhuma leitura válida foi registrada durante o turno, portanto não há MÉTRICAS FINAIS DO TURNO")
print(f"\nPercentual das leituras realizadas: {(qtdLidos / leituras) * 100:.2f}%\n")