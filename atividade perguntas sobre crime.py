cont=0
q1 = input("Telefonou para vitima?: ")
if q1=="sim":
    cont=cont+1
q2 = input ("Esteve no local do crime?:  ")
if q2=="sim":
    cont=cont+1
q3 =input ("Mora perto da vitima?:  ")
if q3=="sim":
    cont=cont+1
q4 = input ("Devia para a vitima?:  ")
if q4=="sim":
    cont=cont+1
q5 = input ("Ja trabalhou com a vitima?: ")
if q5 =="sim":
  cont=cont+1
print(cont)

if cont==0 or cont==1:
    print ("Inocente")
elif cont==2:
    print ("Suspeito")
elif cont==3 or cont==4:
    print ("Cúmplice")
elif cont==5:
    print ("Assassino")
