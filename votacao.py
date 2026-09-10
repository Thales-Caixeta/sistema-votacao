"""Sistema de Votação - votação entre duas opções (A e B)"""

opcoes = {"A": 0, "B": 0}

def votar(opcao):
    if opcao in opcoes:
        opcoes[opcao] += 1
        print(f"Voto computado para {opcao}!")
    else:
        print("Opção inválida.")

def main():
    print("=== Sistema de Votação ===")
    print("Opções disponíveis: A, B")
    while True:
        escolha = input("Digite sua opção (ou 'sair' para encerrar): ").strip().upper()
        if escolha == "SAIR":
            break
        votar(escolha)

if __name__ == "__main__":
    main()

def mostrar_resultado():
    print("\n=== Resultado da votação ===")
    for opcao, votos in opcoes.items():
        print(f"{opcao}: {votos} voto(s)")
    vencedor = max(opcoes, key=opcoes.get)
    print(f"Vencedor: {vencedor}")
