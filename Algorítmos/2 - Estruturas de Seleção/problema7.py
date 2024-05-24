idade=int(input("Informe a idade do nadador: "))

if idade >=5 and idade <= 7:
  categoria = ("Infantil A")
if idade >=8 and idade <= 10:
  categoria = ("Infantil B")
if idade >=11 and idade <= 13:
  categoria = ("Juvenil A")
if idade >=14 and idade <= 18:
  categoria = ("Juvenil B")
if idade >=18:
  categoria = ("Sênior")

print(categoria)