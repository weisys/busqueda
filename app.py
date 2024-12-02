from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Configurar la conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '134679',
    'database': 'busqueda'
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["GET"])
def buscar():
    query = request.args.get("query")  # Obtener el término de búsqueda
    resultados = []

    if query:
        # Conectar a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL con filtro
        sql = "SELECT * FROM tu_tabla WHERE columna LIKE %s"
        cursor.execute(sql, (f"%{query}%",))
        resultados = cursor.fetchall()

        # Cerrar conexión
        cursor.close()
        conn.close()

    return render_template("resultados.html", resultados=resultados, query=query)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
