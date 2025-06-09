import random

print("----CADASTRO----")
cadastro = input("Insira um nome: ")
cadastrosenha = input("Insira uma senha: ")

print("\n----LOGIN----")

login = input("Insira seu nome: ")
loginsenha = input("Insira sua senha: ")

if login != cadastro and loginsenha != cadastrosenha:
    print("Informações inválidas, tente novamente.")
else:
    numerocartao1 = random.randint(1000, 9999)
    numerocartao2 = random.randint(1000, 9999)
    numerocartao3 = random.randint(1000, 9999)
    numerocartao4 = random.randint(1000, 9999)
    saldo = random.randint(0, 9999999)
    dia = random.randint(1, 30)
    mes = random.randint(1, 12)
    
    print("\n----Cartão MONEDAS----")
    print(f"Seja bem-vindo {cadastro}!")
    print(f"{numerocartao1} {numerocartao2} {numerocartao3} {numerocartao4}")
    print(f"Saldo: {saldo}.00")
    if mes <= 9:
        print(f"Data de validade: {dia}/0{mes}")
    elif dia <= 9:
        print(f"Data de validade: 0{dia}/{mes}")
    elif dia <= 9 and mes <= 9:
        print(f"Data de validade: 0{dia}/0{mes}")
    else:
        print(f"Data de validade: {dia}/{mes}")
