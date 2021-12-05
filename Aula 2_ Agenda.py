
from os import close

def insere():
    resposta = ""
    while (resposta != "nao"):
        print("deseja inserir algo a agenda?")
        resposta = input("sua resposta: ")
        if resposta == "sim":
            nome = input("digite o nome da pessoa a ser inserida: ")
            telefone = input("numero de telefone: ")
            rua = input("rua da pessoa: ")
            nascimento = input("ano de nascimento: ")
            dados = (nome+': ( telefone: '+ telefone +'\  rua: '+ rua +'\  ano de nascimento:  '+ nascimento +')' )
            print(dados)
            agenda = open('Arq_Agenda.txt','a')
            agenda.writelines(dados)
            agenda.write('\n')
        else:
            resposta = "nao"
            print("saindo")
def busca():
    resposta = ""
    while (resposta != "nao"):
        print("deseja ler alguma ficha?")
        resposta = input("sua resposta: ")
        if resposta == "sim":
            agenda = open('Arq_Agenda.txt','r')
            leitor = agenda.readlines()
            nome = input('A ficha de quem deseja ver? ')
            confirm = 0
            for i in (leitor):
                if nome in i:
                    print('\n',i,'\n')
                    confirm = 1
            if confirm != 1:
                print('\na ficha de '+nome+' nao foi encontrada\n')
        else:
            resposta = "nao"
            print("saindo")    
def remove():
    resposta = ""
    while (resposta != "nao"):
        print("deseja remover alguma ficha?")
        resposta = input("sua resposta: ")
        if resposta == "sim":
            nome = input("A ficha de quem deseja remover? ")
            agenda = open('Arq_Agenda.txt','r')
            leitor = agenda.readlines()
            confirm = 0
            for i in (leitor):
                if nome in i:
                    confirm = 1
                    x = i
            if confirm != 1:
                agenda.close()
                print('\na ficha de '+nome+' nao foi encontrada\n')
                break
            if confirm == 1:
                removedor = leitor.remove(x)
                agenda = open('Arq_Agenda.txt','w+')
                agenda.writelines(leitor)
                agenda.close   
        else:
            resposta = "nao"
            print("saindo")

def edita():
    resposta = ""
    while (resposta != "nao"):
        print("deseja editar?")
        resposta = input("sua resposta: ")
        if resposta == "sim":
            nome = input("deseja editar a ficha de quem? ")
            agenda = open("Arq_Agenda.txt","r")
            a = agenda.readlines()
            confirm = 0
            for i in (a):
                if nome in i:
                    print('\n',i,'\n')
                    confirm = 1
                    x = i
                    agenda.close()
            if confirm != 1:
                agenda.close()
                print('\na ficha de '+nome+' nao foi encontrada\n')
                break
            if confirm == 1:
                print('removendo a ficha para alteraçao')
                remove()
                y = x.index(':')
                edit = x[y:]
                print('A mudança deve ser escrita na forma: ')
                print(' ( telefone: \  rua: \  ano de nascimento:  )')
                mudanca = input("escreva a nova ficha: ")
                x = x.replace(edit,mudanca)
                agenda = open("Arq_Agenda.txt","a")
                agenda.writelines(x)
                agenda.close()
        else:
            resposta = "nao"
            print("saindo")

def contabiliza():
    agenda = open('Arq_Agenda.txt','r')
    leitor = agenda.readlines()
    print('\n',len(leitor),'fichas registradas\n')

    
# Loop da agenda 
#aqui vcs vão coletar elementos da agenda e os comandos que eu quero fazer

comando = ""

while (comando != "FIM"):
    print("Bem vindo à agenda de LP")
    comando = input("Digite o comando que vc deseja: inserir/buscar/remover/editar/contar ")
    if comando == "inserir":
        insere()
    elif comando == "buscar":
        busca()
    elif comando == "remover":
        remove()
    elif comando == "editar":
        edita()
    elif comando == "contar":
        contabiliza()
    else:
        comando = "FIM"
        print("Saindo do programa")