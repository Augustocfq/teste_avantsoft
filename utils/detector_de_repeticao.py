from collections import Counter

def detector_de_repeticao(nome: str) -> str:
    
    nome_minusculo = nome.lower()
    contagem_de_caracteres = Counter(nome_minusculo)

    for char in nome_minusculo:
        if contagem_de_caracteres[char] == 1:
            return char

    return '_'
