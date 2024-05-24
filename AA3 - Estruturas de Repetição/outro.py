preco_kwh = float(input("Insira o preço do kWh: "))
n_consumidores = int(input("Insira a quantidade de consumidores: "))

consumos = []
tipo_consumidores = []

soma_res = 0
soma_com = 0
soma_ind = 0

maior_consumo = 0
menor_consumo = float('inf')

for i in range(n_consumidores):
    consumo = float(input(f"Insira o consumo do mês do consumidor {i+1}: "))
    tipo_consumidor = int(input(f"Insira o tipo de consumidor do consumidor {i+1} (1: residencial, 2: comercial, 3: industrial): "))

    consumos.append(consumo)
    tipo_consumidores.append(tipo_consumidor)

    if consumo > maior_consumo:
        maior_consumo = consumo

    if consumo < menor_consumo:
        menor_consumo = consumo

    if tipo_consumidor == 1:
        soma_res += consumo
    elif tipo_consumidor == 2:
        soma_com += consumo
    elif tipo_consumidor == 3:
        soma_ind += consumo

for i in range(n_consumidores):
    print(f"O total a pagar do consumidor {i+1} é de: R$ {consumos[i] * preco_kwh:.2f}")

print(f"O maior consumo verificado na amostra de consumidores foi de: {maior_consumo:.2f} kWh")
print(f"O menor consumo verificado na amostra de consumidores foi de: {menor_consumo:.2f} kWh")

print("O total do consumo para cada um dos três tipos de consumidores foi de:")
print(f"Residencial: {soma_res:.2f} kWh")
print(f"Comercial: {soma_com:.2f} kWh")
print(f"Industrial: {soma_ind:.2f} kWh")