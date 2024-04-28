#Strings:

nome = "GuIlHeRme"

print(nome.upper()) #Todas as letras maiusculas .upper
print(nome.lower()) #Todas as letras minusculas .lower
print(nome.title()) #TITULO "primeira letra maiuscula resto minuscula" .title

texto = "   Olá mundo!    "

print(texto)
print(texto.strip()) #Retira o espaçamento da string .strip
print(texto.rstrip()) #Retira o espaçamento da string do lado Direito .rstrip
print(texto.lstrip()) #Retira o espaçamento da string do lado ESQUERDO .lstrip

Menu = "Python"

print ("####" + Menu + "####")
print (Menu.center(14))
print (Menu.center(14, "#"))
print ("-".join(Menu)) #Coloca oq tiver em aspas duplas no meio das letras "".join
print()

#---------------------------------------------------------------------------------------------------#
idade = 28
profissao = "programador"
linguagem = "python"

#nome = input("Digite o nome do jogador: ")
#print(f"Nome: {nome} Idade: {idade} profissao: {profissao} linguagem: {linguagem}")

#---------------------------------------------------------------------------------------------------#

# nome = "Guilherme Arthur de Carvalho"

# print(nome[0])
# print(nome[0:9:1])
# print(nome[-1])
# print(nome[:9]) # Ate o nove
# print(nome[10:])
# print(nome[10:16])
# print(nome[10:16:2])
# print(nome[:])
# print(nome[::-1])

#---------------------------------------------------------------------------------------------------#
nome = "Raissa"

mensagem = f"""
Ola meu nome e {nome},
Eu estou aprendendo Python
"""

print(mensagem)

mensagem2 = f'''
    Ola meu nome e {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos
'''
print(mensagem2)

print(
    """
    =============== MENU ===============
    
    1 - Depositar
    2 - Sacar
    0 - Sair
    
    ====================================
    """
)








