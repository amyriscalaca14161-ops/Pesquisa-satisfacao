# Inicialização das caixas que vão contar os votos
excelente = 0
ruim = 0

# Vamos rodar o programa 10 vezes para o seu teste
for i in range(1, 11):
    print(f"\n--- Entrevistado {i} de 10 ---")
    
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    # Pergunta a opinião e só aceita se for 1, 2 ou 3
    while True:
        print("Opinião sobre o atendimento:")
        print("1: EXCELENTE | 2: BOM | 3: RUIM")
        opiniao = input("Digite o número da opção: ")
        
        if opiniao == "1":
            excelente += 1
            break
        elif opiniao == "2":
            break
        elif opiniao == "3":
            ruim += 1
            break
        else:
            print("Opção inválida! Digite apenas 1, 2 ou 3.")

# Mostra o resultado final na tela
print("\n=== RESULTADO DA PESQUISA ===")
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")
