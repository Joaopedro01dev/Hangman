import random

def sortear_palavra() -> str:
    try:
        with open("words.txt", "r", encoding="utf-8") as arquivo:
            palavras = arquivo.read().split()
            if not palavras:
                print("Erro: O arquivo 'words.txt' está vazio. Encerrando o jogo")
                return
            return random.choice(palavras).strip().upper()
    except FileNotFoundError:
        print("Erro: Arquivo 'words.txt' não encontrado. Encerrando o jogo.")
        return

def main() -> None:
    print("=" * 30)
    print("  BEM VINDO AO JOGO DA FORCA!  ")
    print("=" * 30)

    palavra_sorteada = sortear_palavra()
    if not palavra_sorteada:
        return
    tentativas = 6
    letras_tentadas = []
    acompanhar_jogo = ["_" for _ in palavra_sorteada]

    print(f"\nPalavra: {' '.join(acompanhar_jogo)}")
    print(f"Tentativas restantes: {tentativas}")

    while tentativas > 0:
        print("-" * 30)
        letra = input("Digite uma letra: ").upper().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite somente uma única letra!")
            continue

        if letra in letras_tentadas:
            print(f"Você já tentou a letra '{letra}'. Tente outra!")
            continue

        letras_tentadas.append(letra)

        if letra in palavra_sorteada:
            print(f"Boa! A letra '{letra}' está na palavra!")
            for i, char in enumerate(palavra_sorteada):
                if char == letra:
                    acompanhar_jogo[i] = letra
        else:
            print(f"A letra '{letra}' não está na palavra.")
            tentativas -= 1

        print(f"\nPalavra: {' '.join(acompanhar_jogo)}")
        print(f"Tentativas: {tentativas}")
        print(f"Letras usadas: {', '.join(letras_tentadas)}")

        if "_" not in acompanhar_jogo:
            print(f"PARABÉNS! Você venceu! A palavra era: {palavra_sorteada}")
            return

    print(f"Fim de jogo! Você perdeu. A palavra era: {palavra_sorteada}")

if __name__ == "__main__":
    main()
