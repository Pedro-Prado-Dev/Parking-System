from flask import Flask
from app.routes import bp as main_bp  # Importa o blueprint

app = Flask(__name__)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
