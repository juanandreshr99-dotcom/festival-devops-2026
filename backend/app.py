from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido al Festival DevOps Music Fest"})

@app.route('/artistas')
def artistas():
    artistas = [
        {"nombre": "DJ Docker", "genero": "Electronic"},
        {"nombre": "Los Commits", "genero": "Rock"},
        {"nombre": "Git Flow Band", "genero": "Jazz"}
    ]
    return jsonify(artistas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)