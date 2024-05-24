num1=int(input("Informe o primeiro número: "))
num2=int(input("Informe o segundo número: "))
num3=int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
  maior = num1
  if num2 > num3:
      menor = num3
  else:
      menor = num2
  if num2 > num1 and num2 > num3:
    maior = num2
  if num1 > num3:
      menor = num3
  else:
      menor = num1
else:
  maior = num3
  if num1 > num2:
    menor = num2
  else:
    menor = num1

print("A diferença entre o maior número - o menor número =", maior-menor)
