def inserir_votos(matriz_eleicao, nomes, regioes):
    for c in range(len(nomes)):  
        candidatos = []  
        for r in range(len(regioes)):  
            votos = int(input(f"Insira a quantidade de votos do candidato(a) {nomes[c]} na região {regioes[r]}: "))  
            candidatos.append(votos)  
        total = sum(candidatos)  
        print(f"A quantidade de votos total do candidato {nomes[c]} foi de {total}")  
        matriz_eleicao.append(candidatos)  

def alterar_votos(matriz_eleicao, nomes, regioes):   
    while True: 
        alteracao = input("\nDeseja fazer uma alteração nos votos de algum candidato de determinada região? (Responda S para sim e N para não): ").upper() 
        if alteracao == 'N': 
            break 
        elif alteracao == 'S': 
            candidato = int(input(f"Informe o número do candidato (0 para {nomes[0]}, 1 para {nomes[1]}, 2 para {nomes[2]}): "))
            regiao = int(input(f"Informe o número da região (0 para {regioes[0]}, 1 para {regioes[1]}, 2 para {regioes[2]}, 3 para {regioes[3]}, 4 para {regioes[4]}): ")) 
            novo_voto = int(input("Informe a nova quantidade de votos: ")) 
            matriz_eleicao[candidato][regiao] = novo_voto
        else: 
            print("Resposta inválida") 

def maiorVotos_regioes(matriz_eleicao):
    maior1 = maior2 = maior3 = maior4 = maior5 = 0
    for m in range(len(matriz_eleicao)):  
        if matriz_eleicao[m][0] > maior1:  
            maior1 = matriz_eleicao[m][0]  
        if matriz_eleicao[m][1] > maior2:   
            maior2 = matriz_eleicao[m][1]   
        if matriz_eleicao[m][2] > maior3:   
            maior3 = matriz_eleicao[m][2]   
        if matriz_eleicao[m][3] > maior4:   
            maior4 = matriz_eleicao[m][3]   
        if matriz_eleicao[m][4] > maior5:  
            maior5 = matriz_eleicao[m][4]  

    print(f'\nA quantidade maior de votos da região sul foi de {maior1} votos.')   
    print(f'A quantidade maior de votos da região sudeste foi de {maior2} votos.')   
    print(f'A quantidade maior de votos da região norte foi de {maior3} votos.')   
    print(f'A quantidade maior de votos da região nordeste foi de {maior4} votos.')   
    print(f'A quantidade maior de votos da região centro-oeste foi de {maior5} votos.') 

def mostrar_matriz(nomes, matriz_eleicao):
    print("\nMatriz de votos:")
    print(f"{'Candidato':<10} {'Sul':<10} {'Sudeste':<10} {'Norte':<10} {'Nordeste':<10} {'Centro-Oeste':<10}")

    for i in range(len(nomes)): 
        print(f"{nomes[i]:<10} {matriz_eleicao[i][0]:<10} {matriz_eleicao[i][1]:<10} {matriz_eleicao[i][2]:<10} {matriz_eleicao[i][3]:<10} {matriz_eleicao[i][4]:<10}")   

def main():
    regioes = ['sul', 'sudeste', 'norte', 'nordeste', 'centro-oeste']
    nomes = ['João', 'Sérgio', 'Marina']
    matriz_eleicao = []

    while True:
        print("\nMenu:")
        print("1. Inserir votos")
        print("2. Alterar votos")
        print("3. Mostrar maiores votos por região")
        print("4. Mostrar matriz")
        print("5. Sair")
        
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            inserir_votos(matriz_eleicao, nomes, regioes)
        elif opcao == "2":
            if not matriz_eleicao:
                print("Primeiro você precisa inserir os votos.")
            else:
                alterar_votos(matriz_eleicao, nomes, regioes)
        elif opcao == "3":
            if not matriz_eleicao:
                print("Primeiro você precisa inserir os votos.")
            else:
                maiorVotos_regioes(matriz_eleicao)
        elif opcao == "4":
            if not matriz_eleicao:
                print("Primeiro você precisa inserir os votos.")
            else: 
                mostrar_matriz(nomes, matriz_eleicao)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
