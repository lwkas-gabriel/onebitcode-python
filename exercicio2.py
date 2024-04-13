""" 
1. Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

2. Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
"""

#1 
gameName = "Fifa 23"
char = gameName[0].lower();
new_name = gameName.replace(char, "#");
new_name = char + new_name[1:];
print(new_name);

#2
st1 = 'cab'
st2 = 'zyx'

new_st1 = st2[:2] + st1[2:];
new_st2 = st1[:2] + st2[2:];

print(new_st1);
print(new_st2);