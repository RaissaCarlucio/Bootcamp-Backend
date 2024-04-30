# Projeto de sistema bancario DIO:

print("""
    BEM VINDO AO NOSSO SITEMA BANCARIO! 
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
""")

saldo = 0
numero_saques = 0
extrato = ""

while True:
    x = int(input("Digite o numero: "))
    
    if x == 1:
        print("Saldo atual: ", saldo)
        
        valor = int(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Numero informado invalido!")
            
    elif x == 2:
        print("Voce possui um saldo de: ", saldo)
        y = int(input("Digite o valor que deseja sacar: "))
        
        if y > saldo:
            print("Voce nao tem saldo suficiente")
            
        elif y >= 500:
            print("Voce nao pode sacar esse valor, seu limite e de R$ 500 por saque!")

        elif numero_saques >= 3:
            print("Voce ja excedeu o numero de saques hoje!")
            
        elif y > 0:
            saldo = saldo - y
            extrato += f"Saque: R${y:.2f}\n"    
            numero_saques = numero_saques + 1
            
        else:
            print("Operacao invalida!")   
                     
    elif x == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif x == 4:
        break
    else:
        print("Numero incorreto, digite novamente")                       