import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='clarice'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `AkdmiaDB`;")

cursor.execute("CREATE DATABASE `AkdmiaDB`;")

cursor.execute("USE `AkdmiaDB`;")

# criando tabelas
TABLES = {}
TABLES['Cadastro'] = ('''
      CREATE TABLE `cadastro` (
      `ID_aluno` int(5) AUTO_INCREMENT NOT NULL UNIQUE,
      `CPF` varchar(11) NOT NULL UNIQUE,
      `nome` varchar(150) NOT NULL,
      `endereco` varchar (200) NOT NULL,
      `cep` varchar(8) NOT NULL,
      `n_contato` varchar(11) NOT NULL,
      `dia_de_pag` int NOT NULL,
      `usuario` varchar(20) NOT NULL,
      `senha` varchar(20) NOT NULL,
      PRIMARY KEY (`ID_aluno`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE usuarios (
      ID_log int(5) NOT NULL AUTO_INCREMENT,
      ID_aluno int(5) NOT NULL,
      PRIMARY KEY (ID_log),
      FOREIGN KEY (ID_aluno) REFERENCES cadastro(ID_aluno)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
      '''
      )

TABLES['Controle'] = ('''
      CREATE TABLE controle (
      ID_controle int(5) NOT NULL AUTO_INCREMENT,
      ID_aluno int(5) NOT NULL,
      data date,
      pag binary,
      PRIMARY KEY (ID_controle),
      FOREIGN KEY (ID_aluno) REFERENCES cadastro(ID_aluno)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Bioimpedancia'] = ('''
      CREATE TABLE `bioimpedancia` (
      `ID_bi` int(5) NOT NULL AUTO_INCREMENT,
      PRIMARY KEY(`ID_bi`),
      `peso` varchar (5) NOT NULL,
      `gordura` varchar (5) NOT NULL,
      `massa_magra` varchar (5) NOT NULL,
      `hidratacao` varchar (5) NOT NULL,
      `densidade_ossea` varchar (5) NOT NULL,
      `visseral` int (2) NOT NULL,
      `basal` int (4) NOT NULL,
      ID_aluno int(5) NOT NULL,
      FOREIGN KEY (ID_aluno) REFERENCES cadastro(ID_aluno)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Treino'] = ('''
      CREATE TABLE `treino` (
      `ID_treino` int(5) NOT NULL AUTO_INCREMENT,
      `musculos` varchar (15) NOT NULL,
      `exercicios` varchar (10000) NOT NULL,
      PRIMARY KEY (`ID_treino`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')



for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

#inserindo usuarios
# log_adm_sql = 'INSERT INTO log_adm (usuario, senha) VALUES (%s,%s)'
# usuarios = [
#       ("julioc","nayaraaguiar"),
#       ("joel", "fortunatoamorim")]
#
# cursor.executemany(log_adm_sql, usuarios)
#
# cursor.execute('select * from AkdmiaDB.usuarios')
# print(' -------------  Usuári os:  -------------')
# for user in cursor.fetchall():
#     print(user[1])

#inserindo jogos
# jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
# jogos = [
#      (),
# ]
# cursor.executemany(jogos_sql, jogos)
#
# cursor.execute('select * from AkdmiaDB.usuarios')
# print(' -------------  Jogos:  -------------')
# for jogo in cursor.fetchall():
#    print(jogo[1])

#commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
