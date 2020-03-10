# Criat Tabela da Empresa
def criar_empresa(conexao):
    cursor = conexao.cursor()

    sql =  """
        CREATE TABLE IF NOT EXISTS empresa (
        id_empresa INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_empresa TEXT NOT NULL,
        rua_empresa TEXT NOT NULL,
        num_endereco_empresa INTEGER NOT NULL,
        bairro_empresa TEXT NOT NULL,
        telefone_empresa TEXT NOT NULL,
        cidade_empresa TEXT NOT NULL,
        estado_empresa TEXT NOT NULL
        )"""

    cursor.execute(sql)

#Adicionar dados na tabela empresa
def inserir_empresa(conexao):
    cursor = conexao.cursor()
    nome_empresa         = input("Nome da empresa: ")
    rua_empresa          = input(".....ENDEREÇO DA EMPRESA.....\nNome da Rua: ")
    num_endereco_empresa = input("Número: ")
    bairro_empresa       = input("Bairro: ")
    telefone_empresa     = input("Telefone ou Celular da empresa (ex: 1111-1111): ")
    cidade_empresa       = input("Cidade da empresa: ")
    estado_empresa       = input("Estado da empresa: ")

    sql = """INSERT INTO empresa (nome_empresa, rua_empresa, num_endereco_empresa, bairro_empresa,
    telefone_empresa, cidade_empresa, estado_empresa) VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}')
    """.format(nome_empresa, rua_empresa, num_endereco_empresa, bairro_empresa,
    telefone_empresa, cidade_empresa, estado_empresa)

    cursor.execute(sql)
    conexao.commit()

# Para listar as empresa já adicionadas
def listar_empresa(conexao, id_usuario):
    cursor = conexao.cursor()
    sql = "SELECT * FROM empresa inner JOIN trabalho  where empresa.id_empresa = trabalho.id_empresa AND trabalho.id_usuario = {};".format(id_usuario)
    cursor.execute(sql)

    lista = cursor.fetchall()
    for u in lista:
        print("""
        Codigo da empresa que Você Trabalha: {}
        Nome da Empresa: {}
        Rua: {}
        Número: {}
        Bairro: {}
        Telefone de Contato: {}
        Cidade: {}
        Estado: {}""".format(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]))

#Só para buscar empresa na hora de add trabalho
def buscar_empresa(conexao):
    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM EMPRESA;"
    cursor.execute(sql)
    lista = cursor.fetchall()
    for u in lista:
        print("""
        Codigo da empresa: {}
        Nome da Empresa: {}
        Rua: {}
        Número: {}
        bairro: {}
        Telefone: {}
        Cidade: {}
        Estado: {}""".format(u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8]))

#Para excluir um cadastro feito
# def excluir_empresa(conexao):
#     cursor = conexao.cursor()
#     id_empresa = int(input("Qual Id de empresa desejar excluir? "))
#     opcao      = int(input("Tem certeza que quer excluir o cadastro? \n1 = Sim \n2 = Não \nR: "))
#
#     if(opcao == 1):
#         sql = "DELETE FROM empresa WHERE rowid = {}".format(id_empresa)
#         cursor.execute(sql)
#         cursor.commit
#
#     else:
#         print("Registro não excluído")
#
#Atualizar campos da tabela empresa
def atualizar_empresa(conexao):
     cursor = conexao.cursor()
     atualizar_id = int(input("Qual Id deseja alaterar? "))
     opcao    = int(input("""
                 Qual é a opção a ser mudada
                 1 = Nome empresa
                 2 = Rua empresa
                 3 = Número da empresa
                 4 = Bairro da empresa
                 5 = Telefone da empresa
                 6 = Cidade da empresa
                 7 = Estado da empresa
                 R = """))
     novo_valor  = input("Qual é o valor a ser colocado? ")
     if (opcao == 1):
         sql = """ UPDATE empresa SET nome_empresa = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 2):
         sql = """ UPDATE empresa SET rua_empresa = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 3):
         sql = """ UPDATE empresa SET num_endereco_empresa = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 41):
         sql = """ UPDATE empresa SET bairro_empresa = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 5):
         sql = """ UPDATE empresa SET telefone_empresa = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 6):
         sql = """ UPDATE empresa SET  = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()

     elif(opcao == 7):
         sql = """ UPDATE empresa SET  = '{}' WHERE rowid = {} ;
         """.format(novo_valor, atualizar_id)

         cursor.execute(sql)
         conexao.commit()
