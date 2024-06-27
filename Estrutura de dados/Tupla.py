<<<<<<< HEAD
#Lista:

frutas = ["laranja", "banana", "uva"] #AQUI ESTÁ COMO SERÁ NORMALMENTE FEITO UMA LISTA COM ITENS DENTRO
print("laranja" in frutas) #VERIFICAR SE A PALAVRA ESTÁ NA LISTA "LARANJA" (in) FALSE OR TRUE
print("laranja" not in frutas) #VERIFICAR SE A PALAVRA NÃO ESTÁ NA LISTA "LARANJA" (not in) FALSE OR TRUE
print(frutas)

frutas = [] #PODE SER DECLARADO UMA LISTA VAZIA
print(frutas)

letras = list("python") #SERÁ SEPARADO CADA LETRA DE PYTHON P Y T H O N
print(letras)

numeros = list(range(10)) #SERÁ CONTATO DO NUMERO 0 ATÉ O NUMERO 10 (LEMBRANDO QUE 0 TBM É UM CONTÁVEL) FAZENDO COM QUE PARE NO NUMERO 9
print(numeros)

carro = ["ferrari", "F8", 4200000, 2020, 2900, "são paulo", True] #SERÁ ENTREGUE TODAS AS INFORMAÇÕES DENTRO DA LISTA NO TERMINAL APENAS PRA MOSTRAR:
print(carro)                                                      #QUE PODE SE COLOCAR NUMEROS INTEIROS E STRINGS DENTRO DE UMA LISTA 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#            [0]      [1]      [2]     [3]
frutas_2= ["maça", "laranja", "uva", "pera"]

frutas_2 [0]
print(frutas_2 [0])  #COLOCAR [0] COLCHETE E UM NUMERO DENTRO FARÁ COM QUE O ITEM DA LISTA SEJA PROCURADO BASEADO NO NUMERO DENTRO DO MESMO = MAÇA

frutas_2 [2]         
print(frutas_2 [2])  #COLOCAR [2] COLCHETE E UM NUMERO DENTRO FARÁ COM QUE O ITEM DA LISTA SEJA PROCURADO BASEADO NO NUMERO DENTRO DO MESMO = UVA

frutas_2 [-1]       
print(frutas_2 [-1]) #COLOCAR [-1] COLCHETE E UM NUMERO DENTRO FARÁ COM QUE O ITEM DA LISTA SEJA PROCURADO BASEADO NO NUMERO DENTRO DO MESMO = PERA

frutas_2 [-3]
print(frutas_2 [-3]) #COLOCAR [-3] COLCHETE E UM NUMERO DENTRO FARÁ COM QUE O ITEM DA LISTA SEJA PROCURADO BASEADO NO NUMERO DENTRO DO MESMO = LARANJA

#QUANDO O VALOR FOR POSITIVO DENTRO DO COLCHETE PROCURA NA LISTA DA ESQUERDA PARA A DIREITA
#QUANDO O VALOR FOR NEGATIVO DENTRO DO COLCHETE PROCURA NA LISTA DA DIREITA  PARA A ESQUERDA

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
#Lista Aninhadas:

Matriz = [

        [1,"a",2],
        ["b",3,4],
        [6,5,"c"]

]
=======
#Tupla: "irma" da lista
#Uma tupla tem um valor inical e segue com esse valor até o final sem alteração
#Em vez usar colchetes[lista] se usa parêntenses para(Tupla)

#Exemplos de tuplas de como podem ser criadas 

frutas = ("laranja", "pera", "uva",)   # O  aparecimento de uma virgula no final da tupla fará com que seja mais facil de ser reconhecida 

letras = tuple("python") # Pode ser utilizado também a palavra "tuple" para ser criar uma tupla

numeros = tuple([1, 2, 3, 4]) # Se for colocado uma lista dentro de uma tupla o  valor ou o item que existir dentro da mesma não haverá modificações até
                              # o final do codigo
                               
pais = ("Brasil",) # Novamente uma virgula no final para deixar mais claro que é uma tupla

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#          [0]       [1]      [2]     [3]
frutas = ("maçã", "laranja", "uva", "pera",) 

frutas[0] #maçã

frutas[2] #uva 

print(frutas[0]) #maçã

print(frutas[2]) #uva

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#          [0]       [1]      [2]     [3]
frutas = ("maçã", "laranja", "uva", "pera",) 

frutas[-1]  #laranja

frutas[-3]  #pera

print(frutas[-1]) #pera

print(frutas[-3]) #laranja

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Tuplas aninhadas: não sofrem alteração até o final do codigo 
#Se usa tupla quando você quer ter a garantia de que o valor contido dentro dela não seja alterado

Matriz = (

        (1,"a",2),
        ("b",3,4),
        (6,5,"c"),

)
>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0

Matriz[0]
Matriz[0][0]
Matriz[0][-1]
Matriz[-1][-1]

<<<<<<< HEAD
print (Matriz [0])       # [1,'a',2]
print (Matriz [0][0])    # 1
print (Matriz [0][-1])   # 2
print (Matriz [-1][-1])  # c

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Fatiamento:

Lista = ["p", "y", "t", "h", "o", "n"]

Lista[2:]
Lista[:2]
Lista[1:3]
Lista[0:3:2]
Lista[::]
Lista[::-1]

print (Lista[2:])
print (Lista[:2])
print (Lista[1:3])
print (Lista[0:3:2])
print (Lista[::])
print (Lista[::-1])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Iterar lista:

carros = ["gol", "celta", "palio",]
=======
print(Matriz [0])       # (1, 'a' ,2)
print(Matriz [0][0])    # 1
print(Matriz [0][-1])   # 2
print(Matriz [-1][-1])  # c

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Fatiamento:

tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:]    # 2 ponto inicial, O  segundo valor n foi declarado fazendo com que irá até o final da lista
tupla[:2]    # sem inicio, ponto de parada 2
tupla[1:3]   # ponto inicial 1, ponto de parada 3
tupla[0:3:2] # 0 ponto inicial, 3 ponto de parada, 2 pulando os itens de 2 a 2 (lembrando que sempre pegara a primeira letra)
tupla[::]    # Quando não tive especificações pegará do inicio ao fim
tupla[::-1]  # Do inicio ao fim porém da direita para a esquerda

print(tupla[2:])      #('t', 'h', 'o', 'n')
print(tupla[:2])      #('p', 'y')
print(tupla[1:3])     #('y', 't')
print(tupla[0:3:2])   #('p', 't')
print(tupla[::])      #('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1])    #('n', 'o', 'h', 't', 'y', 'p')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Iterar tupla:

carros = ("gol", "celta", "palio",)
>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0

for carro in carros:
    print(carro)

<<<<<<< HEAD

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Filtro:

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] # se o numero for 1 mostra os numeros impares 

print(pares)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .append para se adicionar qualquer coisa a lista


lista = []

lista.append(1)
lista.append("python")       
lista.append([40, 30, 20])  #usar o comando .append faz com que passe 1 item por vez pra dentro da lista

print (lista) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .clear utilizado para limpar a lista

lista = [1, 'python', [40, 30, 20]]

print (lista)

lista.clear()

print (lista)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .copy utilizado para copiar coisas na lista

lista = [1, 'python', [40, 30, 20]]

l2 = lista.copy
    
print(lista) # [1, 'python', [40, 30, 20]]

print(id(l2)), id(lista)

print(l2)
print(lista)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .count utilizado para contagem de vezes que uma palavra aparece na lista

cores = ["vermelho", "azul", "verde", "azul"]
=======
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .count utilizado para contagem de vezes que uma palavra aparece em uma tupla ou lista

cores = ("vermelho", "azul", "verde", "azul",)
>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0

cores.count("vermelho") #1
cores.count("azul")     #2
cores.count("verde")    #1

print(cores.count("vermelho")) 
print(cores.count("azul"))
print(cores.count("verde"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

<<<<<<< HEAD
# .extend Esse comando  serve para unir duas listas diferente do .append que adiciona 1 item na lista por vez

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"]) #se tiver um item com o mesmo nome duas vezes a nova lista que surgir terá 2 itens do mesmo nome 

print(linguagens)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .index Ele passa a posição do item que você procura na lista (apenas o primeiro que ele encontrar) se tiver dois repetidos ele  não irá contar o proximo
              # [0]     [1]    [2]   [3]      [4]
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java")
linguagens.index("python")
=======
# .index Ele passa a posição do item que você procura na tupla (apenas o primeiro que ele encontrar) se tiver dois repetidos ele  não irá contar o proximo
              # [0]     [1]    [2]   [3]      [4]
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java")   #3
linguagens.index("python") #0
>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0

print(linguagens.index("java"))
print(linguagens.index("python"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

<<<<<<< HEAD
# .pop remove o ultimo item da lista e se for tirado print mostra o item que foi retirado a diferença entres as listas

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)


print(linguagens.pop(0))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .remove   Ele remove o item da lista que estiver escrito no parenteses porem remove apenas o primeiro que ele encontrar na lista se houver mais tem de 
# remover um a um (Pode ser utilizado o .count para ajudar a saber quantos itens iguais existem na lista)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .reverse Utilizado para "espelhar" a sua lista 

linguagens = ["python", "js", "c", "java", "csharp"] # ['csharp', 'java', 'c', 'js', 'python'] <------- resultado usando .reverse

linguagens.reverse()

print(linguagens)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#.sort Utilizado para trocar os itens de decrescente para crescente ou vice versa

linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort() #["c", "csharp", "java", "js", "python"] <---------- resultado usando .sort

linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort(reverse=True) #["python", "js", "java", "csharp", "c"] 

linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort(key=lambda x: len (x)) #["c", "js", "java", "python", "csharp"] <--------- lista na ordem crescente em letras 

linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort(key=lambda x: len(x), reverse=True) #["python", "csharp", "java", "js", "c"] <-------- maior para o menor reverse

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# len usado para saber o tamanho da lista 

linguagens = ["python", "js", "c", "java", "csharp"]    
len (linguagens) #5     
 
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
=======
# len usado para saber o tamanho da tupla ou lista.

linguagens = ("python", "js", "c", "java", "csharp",)  
len (linguagens) #5 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0
