salario = float(input("Escreva seu salario: "))
if salario <= 280:
    porcentagem=salario*20/100
    salarionovo=salario+porcentagem
    print("Salario antigo",salario,"Salario novo",salarionovo,"aumento de 20%, valor do aumento de ",porcentagem)
elif salario > 280 and salario<700:
    porcentagem=salario*15/100
    salarionovo=salario+porcentagem
    print("Salario antigo",salario,"Salario novo",salarionovo,"aumento de 15%, valor do aumento de ",porcentagem)
elif salario >= 700 and salario<1500:
    porcentagem=salario*10/100
    salarionovo=salario+porcentagem
    print("Salario antigo",salario,"Salario novo",salarionovo,"aumento de 10%, valor do aumento de ",porcentagem)
elif salario >= 1500:
    porcentagem=salario*5/100
    salarionovo=salario+porcentagem
    print("Salario antigo",salario,"Salario novo",salarionovo,"aumento de 5%, valor do aumento de ",porcentagem)

    