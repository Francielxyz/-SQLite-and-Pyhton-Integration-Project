import getpass
import os
# Criar a tabala do login do usuario
def criar_tabela_usuario(conexao):

    cursor = conexao.cursor()

    sql = """
       CREATE TABLE IF NOT EXISTS login_usuario (
           id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
           usu_nome TEXT NOT NULL,
           usu_sobrenome TEXT NOT NULL,
           usu_login TEXT UNIQUE NOT NULL,
           usu_senha TEXT NOT NULL
       );"""

    cursor.execute(sql)

# Inserir dados no login do usuario
def inserir_usuario(conexao):
    cursor = conexao.cursor()
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")

    # Comparar se o login já existe
    while(True):
        login = input("Login: ")
        sql = """ SELECT usu_login FROM login_usuario WHERE usu_login = '{}' """.format(login)
        cursor.execute(sql)
        verificacao = cursor.fetchall()

        if (verificacao != []):
            print("Este login já existe. Tente outro!")

        else:
            # Fazer a confirmação de senha e números de carcteres
            while(True):
                senha = getpass.getpass("Senha: ")
                if(len(senha) >= 6):
                    senha2 = getpass.getpass("Confirmar senha: ")
                    if(senha == senha2):
                        sql = """INSERT INTO login_usuario (usu_nome, usu_sobrenome, usu_login, usu_senha) VALUES
                        ('{}','{}','{}','{}');""".format(nome, sobrenome, login, senha)
                        cursor.execute(sql)
                        conexao.commit()
                        break
                    else:
                        print("Senha incorreta! Tente Novamente")
                else:
                    print("Senha deve ter no mínimo 6 catacteres")
            break

# Atualizar campos do usuário
def atualizar_cadastro(conexao, id_usu):
    cursor = conexao.cursor()
    atualizar_id = id_usu
    while(True):
        opcao = input("O que você desejar alterar?\n1 - Nome\n2 - Sobrenome\n3 - Login\n4 - Senha\n5 - Voltar\nR: ")

        if(opcao == "1"):
            os.system('cls' if os.name == 'nt' else 'clear')
            novo_valor = input("Qual é o novo Nome? ")
            sql = """ UPDATE login_usuario SET usu_nome = '{}' WHERE rowid = {} """.format(novo_valor, atualizar_id)
            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "2"):
            os.system('cls' if os.name == 'nt' else 'clear')
            novo_valor = input("Qual é o novo Sobrenome? ")
            sql = """ UPDATE login_usuario SET usu_sobrenome = '{}' WHERE rowid = {} """.format(novo_valor, atualizar_id)
            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "3"):
            os.system('cls' if os.name == 'nt' else 'clear')
            novo_valor = input("Qual é o novo Login? ")
            sql = """ UPDATE login_usuario SET usu_login = '{}' WHERE rowid = {} """.format(novo_valor, atualizar_id)
            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "4"):
            os.system('cls' if os.name == 'nt' else 'clear')
            novo_valor = getpass.getpass("Qual é a nova Senha? ")
            sql = """ UPDATE login_usuario SET usu_senha = '{}' WHERE rowid = {} """.format(novo_valor, atualizar_id)
            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "5"):
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("* * * Opção Inválida * * *.\n* * *Por Favor, Tente Outra!!!* * *\n")
# Excluir o usuario
def exluir_usuario(conexao, iduser):
    cursor = conexao.cursor()
    excluir_id = iduser
    while(True):
        confirmar = input("Tem Certeza que Deseja Excluir seu Usuário do Sistema?\n \n(1) = Sim \n(2) = Não \nR = ")
        if(confirmar == "1"):
            sql = """DELETE FROM login_usuario WHERE rowid = {} ; """.format(excluir_id)
            cursor.execute(sql)
            conexao.commit()
            break
        elif(confirmar == "2"):
            print("Uuário não excluído")
            break
        else:
            print("Opção Inválida")

# Listar todos os usuarios
def listar_usuario(conexao, id_usuario):
    cursor = conexao.cursor()
    sql = "SELECT rowid, * FROM  login_usuario WHERE id_usuario = {};".format(id_usuario)

    cursor.execute(sql)
    lista = cursor.fetchall()
    for u in lista:
        print("""
        ID de Usuário: {}
        Nome: {}
        Sobrenome: {}
        Login: {}""".format(u[1], u[2], u[3], u[4]))
