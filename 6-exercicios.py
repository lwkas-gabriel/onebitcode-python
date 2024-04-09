## Escreva um programa em python que leia um numero e represente o seu antecessor e sucessor, utilziando operadores de atribuição.

number = int(input("Inserir número para descobrir antecessor e sucessor dele: \n"));
sucessor = number + 1;
antecessor = number - 1;
print(f"o sucessor de {number} é {sucessor} e o seu antecessor é {antecessor}");


## Escreva um programa que calcule a média de quatro notas

nota = 0;
nota += float(input("Insira a primeira nota: \n"));
nota += float(input("Insira a segunda nota: \n"));
nota += float(input("Insira a terceira nota: \n"));
nota += float(input("Insira a quarta nota: \n"));

media = nota/4

print(f"A média final das notas é: {media}")