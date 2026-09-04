from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/clientes")
def clientes():
    return "Página de clientes"


@app.route("/proveedores")
def proveedores():
    return "Página de proveedores"


@app.route("/login")
def login():
    return "Página de login"


if __name__ == "__main__":
    app.run(debug=True)