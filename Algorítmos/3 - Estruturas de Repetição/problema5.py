somaPositivos = 0
contagemNegativos = 0
for i in range (4):
  num = int(input("Digite um número inteiro: "))
  if num > 0:
    somaPositivos = somaPositivos + num
  else:
    contagemNegativos += 1
print("A soma dos números positivos é: ", somaPositivos)
print("A contagem de números negativos é: ",contagemNegativos)