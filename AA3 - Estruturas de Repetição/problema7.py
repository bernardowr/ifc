custoKwh = float(input("Insira o valor do kWh: "))
consumidores = []
consumo = []

i = 0
nomeConsumidor = input("Insira o nome do consumidor: ")
consumoConsumidor = float(input("Insira o consumo do consumidor: "))
custo = consumoConsumidor * custoKwh
print("O custo do consumo do consumidor", nomeConsumidor, "é:", custo)
consumidores.append(nomeConsumidor)
consumo.append(custo)
i += 1
print("O total de consumidres é: " , len(consumidores))
soma = sum(consumo)
print("A soma dos valores de consumo é:", soma)
while True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == 'n':
        break 
    else:
      nomeConsumidor = input("Insira o nome do consumidor: ")
      consumoConsumidor = float(input("Insira o consumo do consumidor: "))
      custo = consumoConsumidor * custoKwh
      print("O custo do consumo do consumidor", nomeConsumidor, "é:", custo)
      consumidores.append(nomeConsumidor)
      consumo.append(custo)
      i += 1
      print("O total de consumidres é: " , len(consumidores))
      soma = sum(consumo)
      print("A soma dos valores de consumo é:", soma)

      
    
      