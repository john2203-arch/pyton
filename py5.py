salario=int(input("Digite o seu salário"))

if salario> 1250:
    # aumento_menor=salario *0.15
    novo_salario =salario +(salario*0.15)
    aumento1= salario*0.15
    print("aumento: R$", aumento1)
    print("salario:R$", novo_salario)
   
    
else:
    
    aumento_maior= salario+(salario*0.10)
    aumento2= salario*0.10
    print("aumento: R$", aumento2)
    print("novo salário: R$", aumento_maior)
