total = 0
while total < 100:
    valor = int(input("Informe um valor inteiro: "))
    total+=valor
    print("O total agora é: " , total)
if total ==100:
    print ("Completou 100") 
elif total > 100:
    print ("Passou 100")