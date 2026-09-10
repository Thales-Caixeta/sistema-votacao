"""Sistema de Votação - votação entre duas opções (A e B)"""

opcoes = {"A": 0, "B": 0}

def votar(opcao):
    if opcao in opcoes:
        opcoes[opcao] += 1
        print(f"Voto computado para {opcao}!")
    else:
        print("Opção inválida.")
