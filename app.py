from flask import Flask

from routes.auth import auth_bp
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)