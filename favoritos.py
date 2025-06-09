favoritos = [
    {"nome": "Maria Oliveira", "tipo": "Pessoa", "dados": "CPF 123.456.789-00", "conta": "98765-4"},
    {"nome": "Energia Elétrica", "tipo": "Serviço", "dados": "Código 3456789012", "conta": ""},
    {"nome": "João Souza", "tipo": "Pessoa", "dados": "CPF 987.654.321-00", "conta": "54321-0"},
    {"nome": "Internet Fibra", "tipo": "Serviço", "dados": "Contrato 78901234", "conta": ""},
    {"nome": "Supermercado Preço Bom", "tipo": "Estabelecimento", "dados": "CNPJ 12.345.678/0001-90", "conta": "13579-0"}
]
codigo = True

print("---- CADASTRO ----")
cadastro = input("Insira um nome: ")
cadastrosenha = input("Insira uma senha: ")

print("\n---- LOGIN ----")

login = input("Insira seu nome: ")
loginsenha = input("Insira sua senha: ")

while codigo == True:
    if login != cadastro and loginsenha != cadastrosenha:
        print("Informações inválidas, tente novamente.")
    else:
        print("\n---- BANCO MONEDAS ----")
        print("\nMENU DE FAVORITOS")
        print("1. Ver favoritos cadastrados")
        print("2. Adicionar novo favorito")
        print("3. Realizar transferência para favorito")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            print("\n---- SEUS FAVORITOS ----")
            for i, fav in enumerate(favoritos, 1):
                print(f"{i}. {fav['nome']} ({fav['tipo']})")
                print(f"   Dados: {fav['dados']}")
                if fav['conta']:
                    print(f"   Conta: {fav['conta']}")
                print()
            input("\nPressione Enter para voltar...")
        elif escolha == "2":
            print("\n---- ADICIONAR FAVORITO ----")
            nome = input("Nome: ")
            tipo = input("Tipo (Pessoa/Serviço/Estabelecimento): ")
            dados = input("Dados (CPF/CNPJ/Código/Contrato): ")
            conta = input("Número da conta (deixe em branco se não tiver): ")
            
            novo_fav = {
                "nome": nome,
                "tipo": tipo,
                "dados": dados,
                "conta": conta
            }
            
            favoritos.append(novo_fav)
            print(f"\n{nome} foi adicionado aos seus favoritos!")
            input("Pressione Enter para voltar...")
        
        elif escolha == "3":
            valor = input("Digite um valor para enviar: ")
            nomepago = input("Para quem será enviado esse dinheiro? ")
            print(f"\nO dinheiro foi enviado para {nomepago}!")
            input("Pressione Enter para voltar...")
        
        elif escolha == "4":
            print("Até depois!")
            break
            
        
        
