def digiteNum():
  global num
  num = int(input("Digite um número inteiro de 0 a 10: "))
  return num

def numExtenso():
  num
  numeros=["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez"]
  if num >=0 and num <= 10:
    print(numeros[num])
  else:
    print("Número inválido")

digiteNum()
numExtenso()