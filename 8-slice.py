gameName = "Fifa 23";
gameDescription = """
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilita jogar localmente ou online
""";


## string[inicio:fim] - indice comeca na posicao 0 | indice final -1

#1 - busque toda string apartir da primeira posicao
print(gameName[0:]);

#2 - busque toda a string até a ultima posicao
print(gameName[:7])

#3 - busque toda a string da terceira até a ultima posicao
print(gameName[2:])

"""
string[inicio:fim:passo] - indice comeca na posicao 0 | indice final -1
passo - determina o incremento. por padrao esse numero é o 1.
"""

#4 - busque todo a string de dois em dois caracteres
print(gameName[::2]);

#5 - busque toda a string nos indices impares
print(gameName[1::2])

#6- inverter uma string de tras para frente
print(gameName[::-1])
