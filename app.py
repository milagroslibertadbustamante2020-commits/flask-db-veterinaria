from flask import Flask, render_template, request, redirect, url_for
from database import conectar, crear_tablas

app = Flask(__name__)
crear_tablas()

@app.route("/")
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mascotas")
    mascotas = cursor.fetchall()
    conn.close()
    return render_template("index.html", mascotas=mascotas)

@app.route("/agregar_mascota", methods=["POST"])
def agregar_mascota():
    nombre = request.form.get("nombre")
    especie = request.form.get("especie")
    fecha = request.form.get("fecha_nacimiento")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mascotas (nombre, especie, fecha_nacimiento) VALUES (?, ?, ?)",
                   (nombre, especie, fecha))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)