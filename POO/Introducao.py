# O que e POO:Paradigma de programacao (Um estilo de programacao)
# Paradigmas: Imperativo ou procedural; Funcional; Orientado a eventos e a objetos.
# Orientado a objetos: estrutura o codigo abstraindo problemas em objetos do mundo real

# Classe: define as caracteristicas e comportamentos de um objeto, porem nao conseguimos usar diretamente.
# Objeto: Podemos usar diretamente

# -------------------------------------------------------------------------

# __ini__ = funcao chamada de construtor, sempre executada quando uma nova instancia da classe e criada.
# __del__ = Eu to usando um objeto e depois nao preciso mais dele, utilizado para economizar memoria

class Cachorro: # Classe
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")
    
cao_1 = Cachorro("Chappie", "amarelo", False)
cao_2 = Cachorro("Adrian", "branco e preto")

cao_1.latir() # Chamando a funcao


print(cao_1.nome, cao_1.cor, cao_1.acordado) # Chamando os self
print(cao_2.acordado)

# -------------------------------------------------------------------------
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    #def __str__(self):
    #    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def __str__(self):
        return f"Biblioteca: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2) # Printando o str
b2.correr()
print("")
# -------------------------------------------------------------------------

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c # Chamando a funcao para deletar a instancia C antes do codigo terminar, pode ser chamado a qualquer momento do codigo

criar_cachorro()
print(c)
               
        
        

