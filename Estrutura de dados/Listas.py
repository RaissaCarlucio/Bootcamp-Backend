# Declarando lista:
frutas = ["laranja", "maca", "uva", "pera", "melancia"]
print(frutas)
print(frutas[0])
print(frutas[-1])
print(frutas[2:])
print(frutas[:2])
print(frutas[::])  # Vai mostrar tudo
print(frutas[::-1])  # vai printar de tras pra frente
print(frutas[0:3:2]) # De 0 ate 3, pulando de 2 em 2

print("\n")

for fruta in frutas:
    print(fruta, end=" ")
    
print("\n")

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")  # Declarando as frutas junto com seus indices
    
print("\n")

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz)
print(matriz[0])  # Vai aparecer somente a primeira linha
print(matriz[0][0])  # Print linha 0, coluna 0
print(matriz[0][-1])

print("\n")

numeros = [1, 30, 21, 2, 9, 65, 34]
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end = " ")

print("\n")

# Adicionando valores na lista:
lista = []
lista.append(1)     
lista.append("Raissa")
lista.append("Adrian")
lista.extend(["Jose"])
lista.remove("Raissa")

print(lista)  

lista.reverse()

print("Lista invertida:  ",lista)

lista.clear() # Limpando a lista

print(lista)

# Tenho tambem a funcao lista.copy(), so vou copiar a lista

print("\n")

cores = ["vermelho", "azul", "verde", "azul", "Rosa"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2 (Contar quantos azul tem)
print(cores.count("verde"))  # 1

print(cores.index("Rosa")) # Posicao da cor Rosa

print("\n")

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp,  Remove e retorna o último elemento da lista
print(linguagens)
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

print("\n")


# Ordenando em ordem crescente: 
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)
print("Tamanho da lista: ", len(linguagens))  # Tamanho da lista
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Ordenando em ordem decrescente: 
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Ordenando de acordo com a menor string para a maior
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# Ordenando de acordo com a maior string para a menor
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

print("\n")

nova_lista = sorted(linguagens)
print(nova_lista)
# Se você quer ordenar a lista original, você usa sort(). 
# Se quiser manter a lista original intacta e obter uma nova lista ordenada, você usa sorted().