# from flask import Flask
from flask import Flask, request, jsonify, render_template

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    from .routes.home import home_bp
    from .routes.artist import artist_bp
    from .routes.search import search_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(artist_bp)
    app.register_blueprint(search_bp)

    return app