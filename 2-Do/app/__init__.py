from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from app.config import App_Config
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()
csrf = CSRFProtect()
migrate = Migrate()


def create_app():
    """
    Create a Flask app.
    """
    # Initialize Flask
    app = Flask(__name__)

    # Load configuration from App_Config
    app.config.from_object(App_Config)

    # Allow URLs with or without trailing slashes
    app.url_map.strict_slashes = False

    # Initialize CORS
    CORS(app)

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.auth.routes import auth
    from app.user.routes import user

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(user)

    # Import models
    from app.models.user import User

    with app.app_context():
        # Create database tables
        db.create_all()
        print("Database created successfully")

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("auth.login"))

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("500.html"), 500

    return app
