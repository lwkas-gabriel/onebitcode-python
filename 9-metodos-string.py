gameName = "Fifa 23";
gameDescription = """
    Fifa 23 é um jogo de futebol,
    desenvolvido pela EA Sports,
    e que possibilita jogar localmente ou online
""";

print(gameName.upper()); # retornar string em maiusculo
print(gameName.lower()); # retornar string em minusculo
print(gameName.capitalize()); # apenas primeira letra em maiusculo
print(gameName.title()); # apenas a primeira letra em maiusculo
print(gameName.center(10, '-')); # retorna a string centralizada com caractere de preenchimento
print(gameName.find("0")); # retorna a posicao do caracter dddentro da string, se nào encontrar, retorna -1
print(gameDescription.count("f")); # conta caracteres
print(gameDescription.count("a")); # conta caracteres
print(gameDescription.replace("Fifa", "Pes")); # altera um elemento por outro
print(gameDescription.split(",")); # cria substrings