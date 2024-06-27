# Funcao e um bloco de codigo identificado por nome e pode receber uma lista de parametros.
# Esses parametros podem ou nao ter valores padroes.

def exibir_mensagem():
    print("Ola mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Raissa")
exibir_mensagem_3() # Se eu nao passar nada, ele adota o nome Anonimo
exibir_mensagem_3(nome="Adrian")      

#-------------------------------------------------------------------------------

# Return = retorna a resposta da funcao desejada

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

# Usamos o print pois na funcao temos o return. Se nao tivesse, ja printava direto.
print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

#-------------------------------------------------------------------------------

# Metodos para retornar as funcoes

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Posso passar os parametros assim: 
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Se eu inverter a ordem la na funcao, da erro

#-------------------------------------------------------------------------------

# *Args e **Kwargs
# O metodo recebe os valores como tupla e dicionario

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!", # Arg
    autor="Tim Peters", # Kwarg
    ano=1999,
)

#-------------------------------------------------------------------------------

# Parametros somente por posicao

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel) # 

# Apos a barra, eu tenho que necessariamente passar como marca =; motor =;/ por parametro
# Antes da barra, os parametros estao sendo passados somente por posicao normal. 
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Invalido, nao funciona, pois todos estao sendo passados como modelo =, etc.
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

#-------------------------------------------------------------------------------

# Parametros somente por nome
# Ao usar o *, todos tem que ser por parametro
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # valido
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#-------------------------------------------------------------------------------

# Hibrido

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

#-------------------------------------------------------------------------------

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20


#-------------------------------------------------------------------------------

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
<<<<<<< HEAD
=======

>>>>>>> 20d5ce7d680c9d4fdfae5edb9b9e30348e5f43b0
