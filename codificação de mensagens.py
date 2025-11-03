def zenit_polar_replace(text):
    # Aplicar a codificação Z-E-N-I-T P-O-L-A-R utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    # Entrada da frase e aplicação da codificação
    frase = "The quick brown fox jumps over the lazy dog"
    frase_titulo = frase.title() # Primeira letra de cada palavra em maiúscula

    # Dividir a frase em palavras
    palavras = frase_titulo.split()

    # Processar cada palavra na lista usando ZENIT POLAR
    palavras_cod = [zenit_polar_replace(palavra) for palavra in palavras]

    # Juntar todas as palavras codificadas em uma frase
    frase_cod = " ".join(palavras_cod)
    print("Original:", frase)
    print("Título:", frase_titulo)
    print("Codificada:", frase_cod)

if __name__ == "__main__":
    main()