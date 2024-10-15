nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))



if nota1>=7: 
  print ("Aprovado")

else: 
    if nota1<=7:
       print ("Reprovado")
    else:
       if nota1==10:
          print ("Aprovado com distinção")
          if nota2 >=7:
             print ("Aprovado")
          else:
             if nota2<=7:
                print ("Reprovado")
             else:
                if nota2==10:
                   print ("Aprovado com distinção")