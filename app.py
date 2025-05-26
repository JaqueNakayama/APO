from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calcular_idade(data_nasc):
    nascimento = datetime.strptime(data_nasc, "%Y-%m-%d")
    hoje = datetime.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form.get("nome")
    data_nascimento = request.form.get("data_nascimento")
    idade = calcular_idade(data_nascimento)
    experiencias = request.form.getlist("experiencia[]")
    sobre_mim = request.form.get("sobre_mim")
    habilidades_raw = request.form.get("habilidades")
    habilidades = [h.strip() for h in habilidades_raw.split(",")] if habilidades_raw else []

    return render_template("resultado.html", nome=nome, data_nascimento=data_nascimento,
                           idade=idade, experiencias=experiencias,
                           sobre_mim=sobre_mim, habilidades=habilidades)

if __name__ == "__main__":
    app.run(debug=True)
