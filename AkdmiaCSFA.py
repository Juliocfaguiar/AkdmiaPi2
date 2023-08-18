

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import *

#from flask_login import login_user , login_manager , login_required
# from werkzeug.wrappers.request import Request
# from werkzeug.exceptions import HTTPException, NotFound

# class User:
#     def __init__(self,usuario,senha):
#         self.usuario: usuario
#         self.senha: senha
#
#         usuario1 = User("julioc","nayaraaguiar")
#         usuario2 = User("joel","fortunatoamorim")
#
#         uss == {usuario1.usuario: usuario1, usuario2.usuario: usuario2}

# vincuolo com o banco de dados
app = Flask(__name__)
app.secret_key = 'flokinho'

app.config['SQLALCHEMY_DATABASE_URI'] = \
     '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'clarice',
    servidor = 'localhost',
    database = 'AkdmiaDB'
)
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)