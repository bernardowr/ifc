def maiorNum():
  if n1 > n2:
    return n1
  else:
    return n2

def teste():
  global n1
  global n2
  n1 = float(input("Insira o 1º nº: "))
  n2 = float(input("Insira o 2º nº: "))
  print(f"O maior número é: {maiorNum()}")
  
teste()