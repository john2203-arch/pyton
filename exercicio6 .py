soma=0
quantidade=0

while True: 
    numero = float(input("Digite um número( ou 0 para parar): "))
    if numero == 0:
        break

    soma += numero
    quantidade += 1
    if quantidade>0:
        media= soma / quantidade
        print("_" * 30)
        print(f"Quantidade de números digitados: {quantidade}")
        print(f"somatória dos numeros: {soma}")
        print(f"média aritimética: {media:.2f}")
        print("_" * 30)
    else:
        print(" Nenhum número além de zero digitado")



