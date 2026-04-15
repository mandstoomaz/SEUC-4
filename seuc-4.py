numPressao = int(input(""))

contador = 0
pressaoAjuste = 0
somaPressao = 0
quantidadePressao = 0

while numPressao >= 120:
	if numPressao > 150:
		acrescimo = numPressao + 8%
		pressaoAjuste += acrescimo
	else:
		reducao = numPressao - 4%
		pressaoAjuste += reducao
	contador += 1
	if ?? < 180: