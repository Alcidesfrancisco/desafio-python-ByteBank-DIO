


LIMITE_SAQUES = 3
usuarios = []
NUMERO_AGENCIA = '0001'
contador_conta = 0


#posicional only
def deposita(conta, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    

   
def saca(*, conta):
    global numero_saques, LIMITE_SAQUES

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > conta.saldo

    excedeu_limite = valor > conta.limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque: R$ {valor:.2f}\n"
        conta.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

#posicional = saldo ; keyword = extrato
def ver_extrato(*, conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("==========================================")

def menu(*, conta):
    global LIMITE_SAQUES
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Adicionar Conta
    [l] Listar Contas
    [t] Trocar Conta
    [u] Trocar Usuario

    [q] Sair
=> """
    
    while True:
        opcao = input(menu)

        if opcao == "d":
            deposita(conta)

        elif opcao == "s":
            saca(conta = conta)

        elif opcao == "e":
            ver_extrato(conta = conta)
        elif opcao == 'c':
            cadastrar_conta(conta.usuario)
        elif opcao == 'l':
            listar_contas(conta.usuario)

        elif opcao == "q":
            print("Obrigado por usar ByteBank!! Até logo.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def cadastrar_usuario():
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário: ")
        
        endereco = input("Informe o endereço do usuário: ")
        repete = True        
        while repete:            
            repete = False
            cpf = input("Informe o CPF do usuário: ").replace('.', '').replace('-','')
            for u in usuarios:
                if u.cpf == cpf:
                    print("CPF já cadastrado, por favor tente novamente.")
                    repete = True
                    
        usuario = Usuario(nome = nome, data_nascimento = data_nascimento, cpf=cpf, endereco = endereco)
        print(f"Usuario Cadastrado com sucesso, Bem Vindo ao ByteBank {usuario.nome}")
        usuarios.append(usuario)

def listar_contas(usuario):
    for conta in usuario.contas:
        print(f'Conta: 000{conta.numero}, Saldo: {conta.saldo}')
        print("+++++++++++++++++++++++++++++++++++++++++++++")
    menu(conta = usuario.contas[0])
   
class Usuario():
    def __init__(self, nome, data_nascimento, cpf, endereco): 
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.cpf = cpf
            self.endereco = endereco
            self.saldo = 0
            self.contas = []


class Conta():
    def __init__(self, *,agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
    


numero_saques = 0
def cadastrar_conta(usuario):
    global contador_conta
    contador_conta += 1
    
    conta = Conta(agencia = "000" + NUMERO_AGENCIA, numero = contador_conta, usuario = usuario)
    conta.usuario.contas.append(conta)
    print(f'Conta 000{conta.numero} criada com sucesso!')
    menu(conta=conta)
        
def main():
    if(usuarios):
       cpf = input("Informe seu CPF para login: ")
       for u in usuarios:
           if u.cpf == cpf:
               if u.contas:
                conta = u.contas[0]
                print (f'Existe {len(conta)} conta(s) cadastrada(s) para este Usuário. Conta {conta.numero}, carregada')
                menu(limite_de_saques= LIMITE_SAQUES, conta=conta)

    else:
        usuario = cadastrar_usuario()
        conta = cadastrar_conta(usuario)
        menu(LIMITE_SAQUES, conta = conta)
   
if __name__ == '__main__':
    main()
