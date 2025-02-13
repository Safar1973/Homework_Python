import os
import sys

# Add the project root directory to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from http.HttpHandler import HttpHandler
from database.DBConnection import DBConnection
from security.JWTManger import JWTManger
from security.FormatCheck import FormatCheck

app = Flask(__name__)

# Beispiel-Route für HTTP-Anfragen
@app.route('/api/handle_request', methods=['GET'])
def handle_request():
    handler = HttpHandler()
    response = handler.handle_request()
    return jsonify({"message": response})

# Beispiel-Route für Datenbankverbindung
@app.route('/api/db_status', methods=['GET'])
def db_status():
    db = DBConnection()
    status = db.check_connection()
    return jsonify({"database_status": status})

# Beispiel-Route für JWT-Generierung
@app.route('/api/generate_token', methods=['POST'])
def generate_token():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Beispiel: Überprüfung der Eingabedaten
    if not FormatCheck.validate_username(username) or not FormatCheck.validate_password(password):
        return jsonify({"error": "Invalid username or password format"}), 400

    # Beispiel: Token generieren
    jwt_manager = JWTManger()
    token = jwt_manager.generate_token(username)
    return jsonify({"token": token})

if __name__ == "__main__":
    app.run(debug=True)
