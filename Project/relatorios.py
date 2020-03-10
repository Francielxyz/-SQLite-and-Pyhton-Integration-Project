import sqlite3
import usuario
import trabalho
import empresa
import os
conexao = sqlite3.connect('banco.sqlite')

def senhaMaster(conexao):
    cursor = conexao.cursor()

    sql_del = "DELETE FROM senha; "
    cursor.execute(sql_del)
    conexao.commit()

    sql ="""
    CREATE TABLE IF NOT EXISTS senha (senha_master TEXT NOT NULL)
    """
    cursor.execute(sql)

def addsenha(conexao):
    cursor = conexao.cursor()
    senha = "ruam"
    sql = "INSERT INTO senha (senha_master) VALUES ('{}');".format(senha)
    cursor.execute(sql)
    conexao.commit()
    print("Conectado ao Banco de dados")

def relarorio(conexao):
    txt = "python.txt"
    while(True):
        x = input("Você deseja mostrar o Relatório?\n1 - SIM\n2 - NÃO\nR: ")
        #CRIAR O RELATÓRIO
        if(x == "1"):
            cursor = conexao.cursor()
            sql = """
            SELECT trabalho.id_empresa, empresa.nome_empresa, SUM(trabalho.usu_salario) FROM trabalho
            LEFT JOIN empresa ON empresa.id_empresa = trabalho.id_empresa
            GROUP BY trabalho.id_empresa
            """
            cursor.execute(sql)
            verificacao = cursor.fetchall()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nEMPRESA E PAGAMENTO DE FUNCIONARIOS\n")

            for u in verificacao:
                print("{} - R$ {:.2f} Sálario Total Pago aos Funcionários. ".format(u[1],u[2]))

            break
        elif(x == "2"):
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção Inválida")

    while(True):
        y = input("\n\nTransferir dados para um arquivo txt?\n1 - Sim\n2 - Não\nR: ")
        #TRANSFERINDOS OS ARQUIVOS PARA UM TXT
        if(y == "1"):
            os.system('cls' if os.name == 'nt' else 'clear')
            arq = open(txt, "w")


            for u in verificacao:
                arq.write('Empresa {} - R$ {:.2f} Pagamento aos Funcionarios.\n'.format(u[1], u[2]))
            arq.close()
            break

        elif(y == "2"):
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção Inválida")


conexao.close()

#
# def copiar(abrir, copiar):
#     existente = open(abrir, "r")
#     novo = open(copiar, "w")
#
#     conteudo= existente.readlines()
#     for i in range(0, len(conteudo)):
#         texto = conteudo[i]
#
#         novo.write(texto)
#
#     existente.close()
#     novo.close()
#
# txt = "arq.txt"
# new_txt = "arq2.txt"
#
# criar(txt)
# copiar(txt, new_txt)


# sql = """
# SELECT login_usuario.usu_nome, empresa.nome_empresa, trabalho.usu_salario FROM trabalho
# LEFT JOIN login_usuario ON login_usuario.id_usuario = trabalho.id_usuario
# LEFT JOIN empresa ON trabalho.id_empresa = empresa.id_empresa;
# """

# cursor = conexao.cursor()
# sql = """
# SELECT trabalho.id_empresa, empresa.nome_empresa, SUM(trabalho.usu_salario) FROM trabalho
# LEFT JOIN empresa ON empresa.id_empresa = trabalho.id_empresa
# GROUP BY trabalho.id_empresa
# """
# cursor.execute(sql)
# verificacao = cursor.fetchall()
# for l in range(0, len(verificacao)):
#
#     for c in range(0, len(verificacao[l])):
#         print("{}".format(verificacao[l][c]), end=" ")
#     print()
#
# conexao.close()
# SELECT trabalho.id_empresa, empresa.nome_empresa, SUM(trabalho.usu_salario) FROM trabalho
# LEFT JOIN empresa ON empresa.id_empresa = trabalho.id_empresa
# GROUP BY trabalho.id_empresa
