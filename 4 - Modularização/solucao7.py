def divisor():
  global x , y
  x = int(input("Digite o valor de x: "))
  y = int(input("Digite o valor de y: "))
  if x % y == 0:
    return 1
  else:
    return 0
  
def teste():
  if divisor() == 1:
    print("É divisível")
  else:
    print("Não é divisível")
    
teste()
    