nivel1 = 20
nivel2 = 25
nivel3 = 30

nivel = int(input("Informe o nível do professor: "))
hora = int(input("Informe quantas horas ele trabalhou no mês: "))

if nivel == 1:
  salario = (nivel1 * hora)
if nivel == 2:
      salario = (nivel2 * hora)
if nivel==3:
  salario = (nivel3 *hora)
  
print("O salário deste professor, nível ",nivel,", é: ", salario)

