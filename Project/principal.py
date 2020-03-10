"""PERGUNTAS
NÃO CONSIGO FAZER UM RELATÓRIO DESCENTE AO SER PRINTADO
"""
import sqlite3
import usuario
import trabalho
import empresa
import os
import relatorios
import getpass


conexao = sqlite3.connect('banco.sqlite')
autenticado = False

"Criação de Todas as Tabelas"
usuario.criar_tabela_usuario(conexao)
empresa.criar_empresa(conexao)
trabalho.criar_trabalho_cliente(conexao)
relatorios.senhaMaster(conexao)
relatorios.addsenha(conexao)


os.system('cls' if os.name == 'nt' else 'clear')
print("\n* * * * * * * CADASTRO DE SERVIÇO * * * * * * * \n")
while(True):
    x = input("1 - REGISTRAR \n2 - FAZER O LOGIN \n3 - SENHA MASTER\n4 - SAIR DO MENU\nOpção: ")
    # Caso de alguma opção errada
    if(x != "1" and x != "2" and x != "3" and x != "4"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\tOpção Digitada é Inválida, TENTE OUTRA!!")

    #Sair do progrma
    elif(x == "4"):
        break

    # Registro ao Banco de dados
    elif(x == "1"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("* * * CRIANDO LOGIN * * *")
        usuario.inserir_usuario(conexao)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("* * * AGORA VOCÊ PRECISA REGISTRAR SEUS DADOS DE SERVIÇO * * *")
        trabalho.inserir_trabalho_cliente(conexao)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Fazer Login ao Banco de Dados
    elif(x == "2"):
        os.system('cls' if os.name == 'nt' else 'clear')
        cursor = conexao.cursor()
        login = input("Login: ")
        senha = getpass.getpass("Senha: ")

        sql = """SELECT usu_login, usu_senha, id_usuario FROM login_usuario
        WHERE (usu_login = "{}" and usu_senha = "{}")""".format(login, senha)

        cursor.execute(sql)
        verificacao = cursor.fetchall()

        if(len(verificacao) == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("USUÁRIO OU SENHA INCORRETA.\nPOR FAVOR, TENTE OUTRO\n")

        # Verifica se o Login e Senha estão corretos
        elif(verificacao[0][0] == login and verificacao[0][1] == senha):

            os.system('cls' if os.name == 'nt' else 'clear')

            # Guarda o ID do usuário logado
            autenticado = verificacao[0][2]

            # sql = "SELECT * FROM trabalho WHere id_usuario = {}".format(autenticado)
            # cursor.execute(sql)
            # conexao.commit()
            #
            #
            # ver_trabalho = cursor.fetchall()
            # print (ver_trabalho)
            # if not ver_trabalho:
            #     while(True):
            #         x = input("Deseja Adicionar um novo Trabalho?\n1 - Sim\n2 - Não\nR: ")
            #         if(x == "1"):
            #             trabalho.inserir_trabalho_cliente(conexao)
            #             break
            #         elif(x == "2"):
            #             print("Seu Login não possuir nenhum Trabalho")
            #             break
            #         else:
            #             print("Opção Inválida!!!")

            while(True):
                print(verificacao)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("* * * USUÁRIO ACESSADO COM SUCESSO * * *\n")
                x = input("1 - Para Atualizar Campo\n2 - Para Excluir seu Usuário ou Serviço\n3 - Listar Seus dados\n4 - Sair\nR: ")
                if(x != "1" and x != "2" and x != "3" and x != "4"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Opção Inválida! Por Favor, Selecione Apenas as opções Abaixo!")

                # Para Sair do Banco
                elif(x == "4"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                # Para atualizar campos
                elif(x == "1"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while(True):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y = input("1 - Atualizar dados de seu Usuário\n2 - Atualziar dados do seu Serviço\n3 - Voltar\nR: ")
                        if(x != "1" and x != "2" and x != "3"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Opção Inválida! Por Favor, Selecione Apenas as opções Abaixo!")

                        elif(y == "3"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        # Atualizar dados do Usuário
                        elif(y == "1"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            usuario.atualizar_cadastro(conexao, autenticado)

                        # Atualizar dados do trabalho
                        elif(y == "2"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            trabalho.atualizar_trabalho_cliente(conexao, autenticado)

                # Para Excluir seu usuário
                elif(x == "2"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while(True):
                        z = input("1 - Excluir Usuário\n2 - Exluir Serviço\n3 - Voltar\nR: ")
                        if(z == "3"):
                            break
                        elif(z == "1"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            trabalho.excluir_trabalho_e_usuario(conexao, autenticado)
                            usuario.exluir_usuario(conexao, autenticado)
                            break
                        elif(z == "2"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            trabalho.excluir_trabalho_cliente(conexao, autenticado)


                # Para Listar seus dados
                elif(x == "3"):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while(True):
                        x = input("\n1 - Para listar seus dados de Login\n2 - Para listar dados de seu serviço\n3 - Para listar a empresa que você trabalha\n4 - Voltar\nR: ")
                        if (x == "4"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break

                        # Print dados de login
                        elif(x == "1"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            usuario.listar_usuario(conexao, autenticado)

                        # Print Serviço que trabalha
                        elif(x == "2"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            trabalho.listar_trabalho_cliente(conexao, autenticado)

                        # Print empresa que trabalha
                        elif(x == "3"):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            empresa.listar_empresa(conexao, autenticado)

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Opção INCORRETA! Digite Apenas uma das opções")

    #Para acessar e fazer relatório
    elif(x == "3"):
        os.system('cls' if os.name == 'nt' else 'clear')
        cursor = conexao.cursor()

        senhaM = getpass.getpass("Digite a Senha Master: ")

        sql = """SELECT senha_master FROM senha WHERE (senha_master = "{}")""".format(senhaM)

        cursor.execute(sql)
        verificacao = cursor.fetchall()
        #verificacao de senha master
        if(len(verificacao) == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("* * * ACESSO NEGADO! * * *\nVOCÊ NÃO TEM ACESSO AOS RELATÓRIOS\n")

        #acessando os Relatorios
        elif(verificacao[0][0] == senhaM):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("* * * BEM VINDO ADMINISTRADOR! * * *\n")
            relatorios.relarorio(conexao)
            break

conexao.close()
