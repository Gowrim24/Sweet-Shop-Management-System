from flask import Flask
from extensions import db, bcrypt, jwt
import config

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = config.SECRET_KEY

    # initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # import routes AFTER app creation
    from routes.item_routes import item_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(item_bp, url_prefix="/items")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def home():
        return "Welcome to Sweet Shop Management API"

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
