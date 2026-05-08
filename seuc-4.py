VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
AZUL = '\033[96m'
RESET = '\033[0m'

contador = 0
contFalhas = 0
altaPressao = 0
baixaPressao = 0
contVerde = 0
somaPressao = 0
qtdLidos = 0
menor = -1
maior = -1

def iniciarSistema():
    print(f"{AZUL}--------------------------------------------------")
    print("Iniciando SEUC-4 (Sistema de Escoamento de Unidades de Carga)")
    print("Estabelecendo conexão com os sensores do Duto Principal...")
    print("Calibrando buffers de memória volátil...")
    print("SISTEMA PRONTO PARA OPERAÇÃO MANUAL.")
    print(f"--------------------------------------------------{RESET}\n")

def porcentagemZonaVerde(contVerde, qtdLidos):
    porcentagem = (contVerde / qtdLidos) * 100
    return porcentagem

def mediaPressao(somaPressao, qtdLidos):
     media = somaPressao / qtdLidos
     return media

def menorPressao(menor, pressao):
    if menor == -1:
        menor = pressao
    else:
        if pressao < menor:
            menor = pressao
    return menor

def maiorPressao(maior, pressao):
    if maior == -1:
        maior = pressao
    else:
        if pressao > maior:
            maior = pressao
    return maior
            
def ajusteTermico(pressao):
    if pressao > 150:
        acrescimo = pressao * 1.08
        return acrescimo
    else:
        reducao = pressao * 0.96
        return reducao

def classificacao(pressao, contVerde, baixaPressao, altaPressao):
    if pressao < 90:
        print(f"-> Classificação: {AZUL}ZONA AZUL (Crítica - Cristalização){RESET}")
        altaPressao = 0
        baixaPressao += 1
    else:
        if pressao < 120:
            print(f"-> Classificação: {AMARELO}ZONA AMARELA (Oscilação de Baixa Pressão){RESET}")
            altaPressao = 0
        else:
            if pressao <= 180:
                print(f"-> Classificação: {VERDE}ZONA VERDE (Estável){RESET}")
                contVerde += 1
                altaPressao = 0
            else:
                if pressao < 250:
                    print(f"-> Classificação: {AMARELO}ZONA AMARELA (Oscilação de Alta Pressão){RESET}")
                    altaPressao = 0
                else:
                    print(f"-> Classificação: {VERMELHO}ZONA VERMELHA (Crítica - Alta Pressão){RESET}")
                    altaPressao += 1
    return contVerde, baixaPressao, altaPressao      
        

iniciarSistema()
leituras = int(input("Quantas leituras você realizará neste turno?: "))

while (leituras > contador):
    print(f"\n--- [ Leitura {contador + 1} de {leituras} ] ---")
    pressao = int(input("Digite a pressão (UPC): "))
    
    if pressao <= 0:
        contFalhas += 1
        print(f"{VERMELHO}ERRO NA LEITURA: Valor de UPC Negativo detectado{RESET}")
    else:
        qtdLidos += 1
        pressaoAjustada = ajusteTermico(pressao)
        somaPressao += pressaoAjustada
        
        contVerde, baixaPressao, altaPressao = classificacao(pressaoAjustada, contVerde, baixaPressao, altaPressao)
        if (altaPressao == 2):
            contador = leituras
            print(f"\n{VERMELHO}  / \\  ")
            print(" / ! \\  ALERTA CRÍTICO")
            print("/_____\\ RUPTURA DO DUTO DETECTADA")
            print(f"Fluxo interrompido por segurança.{RESET}\n")

        if (baixaPressao == 1):
            contador = leituras
            print(f"\n{AZUL}  / \\  ")
            print(" / * \\  ALERTA CRÍTICO")
            print("/_____\\ CRISTALIZAÇÃO EMINENTE")
            print(f"Fluxo interrompido por perigo de entupimento do sistema.{RESET}\n")
        
        menor = menorPressao(menor, pressao)
        maior = maiorPressao(maior, pressao)
    contador += 1
    

if qtdLidos > 0:
    print(f"{VERDE}----------------- Relatório do Turno -----------------{RESET}")
    print(f"Média das pressões: {mediaPressao(somaPressao, qtdLidos):.2f} UPC")
    print(f"Menor pressão bruta registrada: {menor} UPC")
    print(f"Maior pressão bruta registrada: {maior} UPC")
    print(f"Porcentagem de leituras na Zona Verde: {porcentagemZonaVerde(contVerde, qtdLidos):.2f}%")
    print(f"Falhas de sensor registradas: {contFalhas}")
else:
    print(f"{VERMELHO}ALERTA: Nenhuma pressão lida foi validada durante o turno. Sem métricas finais.{RESET}")

if leituras > 0:
    print(f"Percentual das leituras realizadas: {(qtdLidos / leituras) * 100:.2f}%\n")
else:
    print(f"{VERMELHO}ERRO: Nenhuma leitura foi programada para este turno.{RESET}\n")