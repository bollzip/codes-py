try:
    a = int(input("Digite uma palavra: "))
except ValueError:
    print ('Digite apenas números')
except:
    print ("Erro desconhecido")
finally:
    print ("Final do algoritimo")