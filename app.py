from flask import Flask, render_template, request, jsonify
# Importamos tus funciones de converter.py
from converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius, 
    km_to_miles, miles_to_km, 
    kg_to_pounds, pounds_to_kg
)
from database import get_engine, get_session, init_db, Conversion

app = Flask(__name__)
engine = get_engine()
init_db(engine)

# Diccionario para mapear las opciones de la web con tus funciones
CONVERSIONES = {
    "celsius_to_fahrenheit": ("temperatura", celsius_to_fahrenheit),
    "fahrenheit_to_celsius": ("temperatura", fahrenheit_to_celsius),
    "km_to_miles":           ("distancia",   km_to_miles),
    "miles_to_km":           ("distancia",   miles_to_km),
    "kg_to_pounds":          ("peso",        kg_to_pounds),
    "pounds_to_kg":          ("peso",        pounds_to_kg),
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convertir", methods=["POST"])
def convertir():
    data = request.get_json()
    funcion = data.get("funcion")
    try:
        valor = float(data.get("valor"))
    except (TypeError, ValueError):
        return jsonify({"error": "Valor inválido"}), 400

    if funcion not in CONVERSIONES:
        return jsonify({"error": "Conversión no encontrada"}), 400

    tipo, fn = CONVERSIONES[funcion]
    resultado = fn(valor)

    # Guardar en la base de datos
    session = get_session(engine)
    session.add(Conversion(
        tipo=tipo, funcion=funcion,
        valor_entrada=valor, valor_salida=resultado
    ))
    session.commit()
    session.close()

    return jsonify({"resultado": resultado})

@app.route("/historial")
def historial():
    session = get_session(engine)
    items = session.query(Conversion).order_by(Conversion.id.desc()).limit(10).all()
    session.close()
    data = [
        {"tipo": c.tipo, "funcion": c.funcion, 
         "entrada": c.valor_entrada, "salida": c.valor_salida}
        for c in items
    ]
    return jsonify(data)

if __name__ == "__main__":
    # Usamos estas opciones para evitar que se cierre en Windows
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)