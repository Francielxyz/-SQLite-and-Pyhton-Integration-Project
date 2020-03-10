import empresa
import usuario
import os

#Criar tabela do trabalho
def criar_trabalho_cliente(conexao):
    cursor = conexao.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS trabalho (
    id_trabalho INTEGER PRIMARY KEY AUTOINCREMENT,
    usu_cargo TEXT NOT NULL,
    usu_horas_trabalho_semanal INTEGER NOT NULL,
    usu_salario DECIMAL(7,2) NOT NULL,
    data_admissao DATE NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_empresa INTEGER NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_empresa) REFERENCES empresa (id_empresa)
    );"""
    cursor.execute(sql)

#Inserir dados no trabalho do cliente
def inserir_trabalho_cliente(conexao):
    cursor =  conexao.cursor()
    sql = "SELECT id_usuario FROM login_usuario "
    cursor.execute(sql)

    select = cursor.fetchall()
    maior = 0
    for lin in range(0, len(select)):

        if(select[lin][0] > maior):
            maior = select[lin][0]

    id_usuario  = maior
    cargo       = input("Qual é o seu cargo? ")
    hrs         = input("Quantas horas você trabalha por semana? ")
    #Trocar Vígula por ponto
    while(True):
        sal = input("Qual é o seu Salário? ")
        sal = list(sal)
        valor = ""
        try:
            for l in range(0, len(sal)):
                if(sal[l] == ","):
                    sal[l] = sal[l].replace(",", ".")
                valor += sal[l]

            salario = float(valor)
            break
        except:
            print("Valor Incorreto")

    while(True):
        dia_admissao = input("Qual é o dia de contratação? ")
        if(len(dia_admissao) == 1):
            dia_admissao = '0' + dia_admissao

        if(dia_admissao.isdecimal() and int(dia_admissao) <= 31 and int(dia_admissao) >= 1):
            break
        else:
            print("Dia Errado")

    while(True):
        mes_admissao = input("Qual é o mês(número) de contratação? ")
        if(len(mes_admissao) == 1):
            mes_admissao = '0' + mes_admissao

        if(mes_admissao.isdecimal() and int(mes_admissao) <= 12 and int(mes_admissao) >= 1):
            break
        else:
            print("Mês Errado")

    while(True):
        ano_admissao = input("Qual é o ano que foi contração? ")
        if(len(ano_admissao) == 1):
            ano_admissao = '0' + ano_admissao

        if(ano_admissao.isdecimal() and int(ano_admissao) > 1000 and int(ano_admissao) < 3000):
            break
        else:
            print("Ano Errado")

    admissao = dia_admissao + '-' + mes_admissao + '-' + ano_admissao


    os.system('cls' if os.name == 'nt' else 'clear')
    empresa.buscar_empresa(conexao)
    print("\nAGORA VAMOS ADICIONAR A EMPRESA QUE VOCÊ TRABALHA")

    while(True):
        x = input("Adcionar uma Empresa Nova = 1 \nEscolher uma Empresa já Adicionada = 2\nR: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if(x == "1"):
            empresa.inserir_empresa(conexao)
            os.system('cls' if os.name == 'nt' else 'clear')

            empresa.buscar_empresa(conexao)
            while(True):
                try:
                    id_empresa  = int(input("Qual é o CÓDIGO da Empresa que Trabalha? "))

                    sql = '''INSERT INTO trabalho (usu_cargo, usu_horas_trabalho_semanal, usu_salario, data_admissao,
                    id_empresa, id_usuario) VALUES  ('{}', '{}', '{}', '{}', {}, {})'''.format(cargo, hrs, salario, admissao, id_empresa, id_usuario)

                    cursor.execute(sql)
                    conexao.commit()
                    break

                except:
                    print("Opção Invalida")


        elif(x == "2"):
            empresa.buscar_empresa(conexao)
            while(True):
                try:
                    id_empresa  = int(input("Qual é o CÓDIGO da Empresa que Trabalha? "))

                    sql = '''INSERT INTO trabalho (usu_cargo, usu_horas_trabalho_semanal, usu_salario, data_admissao,
                    id_empresa, id_usuario) VALUES  ('{}', '{}', '{}', '{}', {}, {})'''.format(cargo, hrs, salario, admissao, id_empresa, id_usuario)

                    cursor.execute(sql)
                    conexao.commit()
                    break

                except:
                    print("Opção Invalida")

        break
# Atualizar dados na empresa
def atualizar_trabalho_cliente(conexao, id_trabalho):
    cursor = conexao.cursor()

    atualizar_id = id_trabalho
    while(True):
        opcao = input("""
Qual é a opção a ser mudada
1 - Cargo
2 - Horas de trabalho
3 - Salario
4 - Voltar
R - """)
        if(opcao == "1"):
            novo_valor  = input("Qual é o seu novo Cargo? ")
            sql = """ UPDATE trabalho SET usu_cargo = '{}' WHERE rowid = {} ;""".format(novo_valor, atualizar_id)
            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "2"):
            novo_valor  = input("Qual é a sua Carga Horária Nova? ")
            sql = """ UPDATE trabalho SET usu_horas_trabalho_semanal = '{}' WHERE rowid = {} ;""".format(novo_valor, atualizar_id)

            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "3"):
            novo_valor  = input("Qual é o seu novo Salário? ")
            sql = """ UPDATE trabalho SET usu_salario = '{}' WHERE rowid = {} ;""".format(novo_valor, atualizar_id)

            cursor.execute(sql)
            conexao.commit()

        elif(opcao == "4"):
            break
        else:
            print("Opção Incorreta")
#Excluir dados de trabalho completo
def excluir_trabalho_cliente(conexao, id_trabalho):
    cursor  = conexao.cursor()
    excluir_id_tr = id_trabalho
    while(True):
        certeza = input("Tem certeza que deseja excluir seu trabalho? \n1 - Sim \n2 - Não\nR = ")
        if (certeza == "1"):
            sql = "DELETE FROM trabalho WHERE rowid = {} ;".format(excluir_id_tr)
            os.system('cls' if os.name == 'nt' else 'clear')
            cursor.execute(sql)
            conexao.commit()
            break
        elif(certeza == "2"):
            print("Usuário Não Excluído")
            break
        else:
            print("Opção Incorreta")

def excluir_trabalho_e_usuario(conexao, id_trabalho):
    cursor  = conexao.cursor()
    excluir_id_tr = id_trabalho
    sql = "DELETE FROM trabalho WHERE rowid = {} ;".format(excluir_id_tr)
    cursor.execute(sql)
    conexao.commit()

#Para listar o trabalho do cliente
def listar_trabalho_cliente(conexao, id_trabalho):
    cursor = conexao.cursor()
    # sql = "SELECT rowid, * FROM trabalho WHERE id_trabalho = {};".format(id_trabalho)
    sql = "SELECT * From trabalho INNER JOIN login_usuario WHERE trabalho.id_usuario = login_usuario.id_usuario AND trabalho.id_usuario = {}".format(id_trabalho)
    # SELECT * From trabalho INNER JOIN login_usuario WHERE trabalho.id_usuario = login_usuario.id_usuario AND trabalho.id_usuario =
    cursor.execute(sql)
    listar = cursor.fetchall()

    for u in listar:
        print("""
        Nome: {}
        Você Trabalha Como: {}
        Você Trabalha: {} hrs Semanais
        Você recebe: R$ {} por Mês
        Você Foi Contratado em: {}""".format(u[8], u[1], u[2], u[3], u[4]))

# def inserir_new_servico(conexao, id_trabalho):
#     cursor =  conexao.cursor()
#     id_user = id_trabalho
#     sql = "SELECT rowid, * FROM trabalho WHERE id_trabalho = {};".format(id_user)
#
#     cargo       = input("Qual é o seu cargo? ")
#     hrs         = input("Quantas horas você trabalha por semana? ")
#     salario     = input("Qual é o seu salário? ")
#     admissao    = input("Qual é a sua data de admissão? ")
#
#     id_usuario  = maior
#
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("AGORA VAMOS ADICIONAR A EMPRESA QUE VOCÊ TRABALHA")
#     x = input("Adcionar um empresa = 1 \nEscolher uma empresa já adcionada = 2\nR: ")
#     os.system('cls' if os.name == 'nt' else 'clear')
#
#     if(x == "1"):
#         empresa.inserir_empresa(conexao)
#         os.system('cls' if os.name == 'nt' else 'clear')
#
#     empresa.buscar_empresa(conexao)
#     id_empresa  = int(input("Qual é o Id da empresa que trabalha? "))
#
#     sql = '''INSERT INTO trabalho (usu_cargo, usu_horas_trabalho_semanal, usu_salario, data_admissao,
#     id_empresa, id_usuario) VALUES  ('{}', '{}', '{}', '{}', {}, {})'''.format(cargo, hrs, salario, admissao, id_empresa, id_usuario)
#
#     cursor.execute(sql)
#     conexao.commit()
