total_locais = 17
locais_restantes = 17

total_chefes = 17
chefes_restantes = 17

total_magias = 6
magias_restantes = 6

total_habilidades = 7
habilidades_restantes = 7

total_amuletos = 40
amuletos_restantes = 40

percentual_atual = 0
percentual_restante = 100

minhas_conquistas = {}

def adicionar_conquista(item, tipo):
    minhas_conquistas[item] = tipo
    print(f"\nConquista adicionada!\n")

def calcular_porcentagem_atual(tipo):
    global percentual_atual
    global percentual_restante

    if tipo == "Habilidade":
        percentual_atual += 2
        percentual_restante -= 2
    else:
        percentual_atual += 1
        percentual_restante -= 1


print("-" * 70)
print("-" * 70)
print("PROGRESS-OMETER\n".center(60))
print("""
    Seja bem vindo ao progressometer, sua ferramenta preferida 
            de analise de progresso em jogos

    \n""".center(60))
print("-" * 70)
print("-" * 70)
print("\n")

print("JOGO SELECIONADO ----> HOLLOW KNIGHT <----\n\n")

option = 0

while option != 4:
    print("-" * 70)
    print("OPERACOES\n")
    print("1 - Inserir nova conquista")
    print("2 - Ver progresso atual")
    print("3 - Progresso Restante")
    print("4 - Sair\n")

    option = int(input("Qual operacao deseja realizar?: "))

    match option:
        case 1:
            print("\nCATEGORIAS DE CONQUISTA\n")
            print(" --> Chefe")
            print(" --> Local")
            print(" --> Amuleto")
            print(" --> Magia")
            print(" --> Habilidade\n")
            conq = input("Qual tipo de conquista deseja adicionar?: ")
            conq = conq.capitalize()

            match conq:
                case "Chefe":
                    chefe = input("Qual chefe foi derrotado?: ")
                    adicionar_conquista(chefe.capitalize(), conq)
                    chefes_restantes -= 1
                    calcular_porcentagem_atual(conq)
                case "Local":
                    local = input("Qual local foi explorado?: ")
                    adicionar_conquista(local.capitalize(), conq)
                    locais_restantes -= 1
                    calcular_porcentagem_atual(conq)
                case "Amuleto":
                    amuleto = input("Qual amuleto foi obtido?: ")
                    adicionar_conquista(amuleto.capitalize(), conq)
                    amuletos_restantes -= 1
                    calcular_porcentagem_atual(conq)
                case "Magia":
                    magia = input("Qual magia foi descoberta?: ")
                    adicionar_conquista(magia.capitalize(), conq)
                    magias_restantes -= 1
                    calcular_porcentagem_atual(conq)
                case "Habilidade":
                    hab = input("Qual habilidade foi encontrada?: ")
                    adicionar_conquista(hab.capitalize(), conq)
                    habilidades_restantes -= 1
                    calcular_porcentagem_atual(conq)

        case 2:
            print("\nSuas conquistas atuais sao:")
            for item, conq in minhas_conquistas.items():
                print(f" --> {item}, {conq}")

            print(f"\nPercentual de conclusao: --> {percentual_atual}% <--\n")

        case 3: 
            print(f"\nResta {percentual_restante}% para a conclusao do jogo")
            
            print("\nConquistas restantes:")
            print(f" --> {chefes_restantes} chefes")   
            print(f" --> {locais_restantes} locais")   
            print(f" --> {amuletos_restantes} amuletos")   
            print(f" --> {habilidades_restantes} habilidades")   
            print(f" --> {magias_restantes} magias\n")  

        case 4: 
            print("\nBoa sorte na sua jornada!")
            