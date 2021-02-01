# Permite acceder a las variables de entorno
import os
# Es flask osea
from flask import Flask, send_from_directory, render_template


def create_app():
    app = Flask(__name__)
    # Configuraremos las variables
    app.config.from_mapping(
        # Creamos una cookie
        SECRET_KEY          =   "hgjkjh32iuhfaiu3",
        DATABASE            =   os.environ.get("FLASK_DATABASE"),
        DATABASE_HOST       =   os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_USER       =   os.environ.get("FLASK_DATABASE_USER"),
        DATABASE_PASSWORD   =   os.environ.get("FLASK_DATABASE_PASSWORD"),
        STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route("/favicon.ico")
    def hola():
        return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico")

    @app.route("/static/<path:filename>")
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC_FOLDER"], filename)

    return app
