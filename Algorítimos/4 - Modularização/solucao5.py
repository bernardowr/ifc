def diasSemana():
  diaSemana = ["SEG","TER","QUA","QUI","SEX","SAB","DOM"]
  if diaNum >=1 and diaNum <= 7:
    print(diaSemana[diaNum-1])
  else:
    print("Dia invalido")

def diasNumericos():
  global diaNum
  diaNum = int(input(f"(Informe o dia da semana de 1 a 7)"))
  diasSemana()
  return diaNum
    
diasNumericos() 