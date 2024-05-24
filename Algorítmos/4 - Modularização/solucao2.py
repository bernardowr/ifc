def lervalor():
  global mesNumero
  mesNumero = int(input("Insira o mês: "))
  mesExtenso()

def mesExtenso():
  meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
  if mesNumero >=1 and mesNumero <= 12:
    print(meses[mesNumero - 1])
  else:
    print("Erro: Insira um número inteiro entre 1 e 12")

lervalor()