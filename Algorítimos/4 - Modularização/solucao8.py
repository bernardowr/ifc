def quociente():
  x = int(input(f"(Digite o valor de x)"))
  y = int(input(f"(Digite o valor de y)"))
  if x % y != 0:
    return -1
  else: 
    return (f"O resultado da divisão é {x/y}")
  
def teste():
  print (quociente())
  
teste()