x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))
z = float(input("Informe o valor de z: "))
if x < (y + z) and y < (x+z) and z < (y+x): 
  if x == y and x == z:
    triangulo = "é triângulo equilátero."
  elif x == y or x == z or y ==z:
    triangulo = "é triângulo isóceles."
  elif x!= y and x!= z:
    triangulo = "é triângulo escaleno."
else:
  triangulo = "não é um triângulo."

print("O objeto informado", triangulo)