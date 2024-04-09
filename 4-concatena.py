name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"));
price = float(input("Digite o preço do jogo: \n"));
planIncluded = bool(input("Está incluso no serviço mensal?: \n"));


print("### Dados do Jogo ###");
print("=====================");
print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} 
      \nPreço: {price} \nEstá incluso no serviço? {planIncluded}")