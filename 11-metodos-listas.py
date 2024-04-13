gameList = ["Resident Evil 4", "Star Wars Jedi Survivor",
            "The Legend of Zelda", "Red Dead 2", "Mario Odissey"];


#1 - tamanho da lista
print(len(gameList));

#2 - recupar um item da lista pelo indice
print(gameList.index("Resident Evil 4"));

#3 - adicionar item ao final da lista
print(gameList.append("Diablo 3"));
print(gameList);

#4 - ordenar a lista
gameList.sort();
print(gameList);

#5 - copiar os itens de uma lista para outra
gameReset = gameList.copy();
gameReset.remove("Star Wars Jedi Survivor");
print(gameReset);
 
#6 - remove todos os itens da lista
gameList.clear();
print(gameList);