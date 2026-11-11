from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Sistema de Gestion de Servicios Academicos",
        "estado": "Funcionando correctamente"
    })

@app.get("/estudiantes")
def estudiantes():
    return jsonify({
        "estudiantes": [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "Maria"}
        ]
    })

@app.get("/salud")
def salud():
    return jsonify({"estado": "OK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
