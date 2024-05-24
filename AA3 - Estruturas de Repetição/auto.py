custoKwh = float(input("Insira o valor do kWh: "))
consumidores = []
consumo = []
somaRes = 0
somaCom = 0
somaInd = 0

i = 0
while i < 5:
    nomeConsumidor = input("Insira o nome do consumidor: ")
    consumoConsumidor = float(input("Insira o consumo do consumidor: "))
    tipoConsumidor = int(input("Insira o tipo de consumidor (1 - Residencial, 2 - Comercial, 3 - Industrial): "))
    custo = consumoConsumidor * custoKwh
    print("O custo do consumo do consumidor", nomeConsumidor, "é:", custo)
    consumidores.append(nomeConsumidor)
    consumo.append(consumoConsumidor)
    if tipoConsumidor == 1:
        somaRes += consumoConsumidor
    if tipoConsumidor == 2:
        somaCom += consumoConsumidor
    if tipoConsumidor == 3:
        somaInd += consumoConsumidor
    i += 1

print("A soma dos valores de consumo para consumidores residenciais é:", somaRes)
print("A soma dos valores de consumo para consumidores comerciais é:", somaCom)
print("A soma dos valores de consumo para consumidores industriais é:", somaInd)