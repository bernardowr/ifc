def numRomanos():
  romanos = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI',
           'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 
           'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 
           'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 
           'XXXVII', 'XXXVIII', 'XXXIX', 'XL','XLI','XLII','XLIII',"XLIV", "XLV",
           "XLVI","XLVII","XLVIII","XLIX","L",]
  if 1 <= num <= 50:
   return romanos[num-1]
  else:
      return "Número inválido."

def leitorNum():
  global num
  num = int(input(f"Digite um número de 1 a 50: "))
  print(numRomanos())
  
leitorNum()
  

  
  
