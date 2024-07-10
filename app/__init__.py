from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import routes here to avoid circular import issues
        from . import routes
        routes.init_app(app)

    return app
