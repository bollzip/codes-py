import os
while True:
    try:
        num1 = float(input("Digite um número: " ))
        num2 = float (input("Digite um número: "))
    except ValueError:
        print ("Digite apenas números")
        continue
    cal = int(input("Informe o calculo \n 1) adc \n 2)subt\n3)mult\n4)div 0)Sair "))
    if cal == 0:
        print ("saindo")
        break
    os.system ('cls')
    calf = 0
    if cal ==1:
        calf = num1 + num2
        print ('resultado',calf)
    if cal ==2:
        calf = num1 - num2
        print ('resultado', calf)
    if cal ==3:
        calf = num1 * num2
        print ('resultado', calf) 
    try:
        if cal ==4:
            calf = num1/num2
            print (f'resultado:  {calf:.2f}')
    except ZeroDivisionError:
        print ("Não é possivel dividir por 0")
    continue
        
