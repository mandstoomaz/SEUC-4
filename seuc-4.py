contador = 0
pressaoAjuste = 0
somaPressao = 0
quantidadePressao = 0

numPressao = int(input("Digite a pressão: "))
def ajusteTermico(numPressao):
	if numPressao > 150:
		acrescimo = numPressao * 1.08
		return acrescimo
	else:
		reducao = numPressao * 0.96
		return reducao