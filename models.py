from AkdmiaCSFA import db


# classes com as informações das tabelas criadas no banco de dados
class Cadastro(db.Model):
    __tablename__ = 'cadastro'

    ID_aluno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    CPF = db.Column(db.String(11))
    nome = db.Column(db.String(150),nullable=False)
    endereco = db.Column(db.String(200),nullable=False)
    CEP = db.Column(db.String(8), nullable = False)
    n_contato = db.Column(db.String(11),nullable=False)
    dia_de_pag= db.Column(db.Integer,nullable=False)
    usuario = db.Column(db.String(20),nullable=False)
    senha = db.Column(db.String(20),nullable=False)
    controle = db.relationship('Controle', backref="cadastro")

    def __init__(self, CPF, nome, endereco,CEP,n_contato,dia_de_pag,usuario,senha):
        self.CPF=CPF
        self.nome=nome
        self.endereco=endereco
        self.CEP=CEP
        self.n_contato=n_contato
        self.dia_de_pag=dia_de_pag
        self.usuario=usuario
        self.senha=senha

class Usuarios(db.Model):
    ID_log = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # usuario = db.Column(db.String(20),nullable=False)
    # senha = db.Column(db.String(20),nullable=False)
    ID_aluno = db.Column(db.Integer, db.ForeignKey('cadastro.ID_aluno'))

    def __repr__(self):
        return '<Name %r>' % self.name

class Controle(db.Model):
    ID_controle = db.Column (db.Integer,primary_key=True,autoincrement=True)
    data = db.Column (db.Date,nullable=False)
    pag = db.Column (db.Integer)
    ID_aluno = db.Column (db.Integer, db.ForeignKey('cadastro.ID_aluno'))

    def __repr__(self):
        return '<Name %r>' % self.name

class Bioimpedancia(db.Model):
    ID_bi = db.Column (db.Integer,primary_key=True,autoincrement=True)
    peso = db.Column (db.String(5),nullable=False)
    gordura = db.Column (db.String(5),nullable=False)
    massa_magra = db.Column (db.String(5),nullable=False)
    hidratacao = db.Column (db.String(5),nullable=False)
    densidade_ossea = db.Column (db.String(5),nullable=False)
    visseral = db.Column (db.Integer,nullable=False)
    basal = db.Column (db.Integer,nullable=False)
    ID_aluno = db.Column(db.Integer)

    def __init__(self,id_bi,peso,gordura,massa_magra,hidratacao,densidade_ossea,viseral,basal):
        self.id_bi=id_bi
        self.peso=peso
        self.gordura=gordura
        self.massa_magra=massa_magra
        self.hidratacao=hidratacao
        self.densidade_ossea=densidade_ossea
        self.viseral=viseral
        self.basal=basal

class Treino(db.Model):
     ID_treino = db.Column (db.Integer,primary_key=True,autoincrement=True)
     musculos = db.Column (db.String(15),nullable=False)
     exercicios = db.Column (db.String(10000),nullable=False)

     def __init__(self, musculos, exercicios):
         self.musculos=musculos
         self.exercicios=exercicios


