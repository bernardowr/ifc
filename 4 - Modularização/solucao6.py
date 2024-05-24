def numPrimo():
    global num
    num = int(input("Digite um número: "))
    if num > 1:
       for i in range(2, num):
          if (num % i) == 0:
             return 0
       else:
          return 1
  
def teste():
  if numPrimo() == 1:
      print(num, "é um número primo")
  else:
      print(num, "não é um número primo")

teste()    
  