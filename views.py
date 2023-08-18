
import datetime
from flask import render_template,request,redirect,session
from AkdmiaCSFA import app ,db
from models import Cadastro,Controle,Bioimpedancia,Usuarios,Treino
# rotas das páginas web

@app.route("/")
def inicio():
    return  render_template('inicio.html')


@app.route('/cadastro')
def cadastro():
    return  render_template ('cad.html')

#rota auxiliar do cadastro

@app.route('/cad',methods = ['GET','POST'])
def cad():
    if request.method == "POST":
        CPF = request.form.get("CPF")
        nome =request.form.get("nome")
        endereco=request.form.get("endereco")
        CEP =request.form.get("CEP")
        n_contato =request.form.get("n_contato")
        dia_de_pag =request.form.get("dia_de_pag")
        usuario =request.form.get("usuario")
        senha = request.form.get("senha")

        if CPF and nome and endereco and CEP and n_contato and dia_de_pag and usuario and senha:
            cadastro = Cadastro(CPF, nome, endereco, CEP, n_contato, dia_de_pag, usuario, senha)
            db.session.add(cadastro)
            db.session.commit()

            data = datetime.date.today()

            ctrl = Controle(cadastro=cadastro, data=data, pag=False)
            logg = Controle(usuario = usuario, senha = senha)
            db.session.add(ctrl,logg)
            db.session.commit()


    return redirect("/")

@app.route('/controle')
def controle():
    cads = Cadastro.query.all()
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return render_template("controle.html",cads=cads)

# Rotas de Controle de Acesso

@app.route('/login')
def log():
    return  render_template('login.html')

@app.route('/logout')
def logout():
    session ['usuario_logado'] = None
    return  redirect('/')


# Rota auxiliar do Login

@app.route('/autenticar',methods=['POST',])
def autenticar():

   if request.form['usuario'] in Usuarios:
        users = Usuarios[request.form['usuario']]
        if request.form['senha'] == users.senha:
            session['usuario_logado'] = users.usuario
        return  redirect ('/admlog')

@app.route('/aluno_log')
def allog():
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return  render_template('aluno_log.html')

@app.route('/adm_log')
def admlog():
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return  render_template ('adm_log.html')


@app.route('/add_treinos')
def add_t():
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return  render_template('add.html')

#rota auxiliar treinos
@app.route('/add',methods = ['GET','POST'])
def add():
    if request.method == "POST":
        musculos = request.form.get("musculos")
        exercicios = request.form.get("exercicios")

        if musculos and exercicios:
            T = Treino(musculos,exercicios)
            db.session.add(T)
            db.session.commit()
    return redirect("/treinos")

@app.route('/treinos')
def birl():
    birll = Treino.query.all()
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return  render_template('treinos.html',birll = birll)



@app.route("/me")
def mee():
    # if 'usuario_logado' not in session or session ['usuario_logado'] == None:
    #     return redirect ('/login')
    return  render_template('me.html')