def numExtenso():
  num = int(input(f"Digite um número de 0 a 50: "))
  if 0 <= num <= 50:
      extenso : ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
                  "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
                  "vinte", "vinte e um", "vinte e dois", "vinte e três", "vinte e quatro", "vinte e cinco",
                  "vinte e seis", "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um",
                  "trinta e dois", "trinta e três", "trinta e quatro", "trinta e cinco", "trinta e seis",
                  "trinta e sete", "trinta e oito", "trinta e nove", "quarenta", "quarenta e um", "quarenta e dois",
                  "quarenta e três", "quarenta e quatro", "quarenta e cinco", "quarenta e seis", "quarenta e sete",
                  "quarenta e oito", "quarenta e nove", "cinquenta"]
      return extenso[num]
  else:
      return "Número inválido."

def teste():
  print(numExtenso())

teste()