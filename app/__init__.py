# from flask import Flask
from flask import Flask, request, jsonify, render_template
from .data_loader import load_data

def create_app():
    app = Flask(__name__, template_folder='../templates')

    model, data_list, artist_indices, V1, V2, V3, Va, knn_result = load_data()

    app.config['model'] = model
    app.config['data_list'] = data_list
    app.config['artist_indices'] = artist_indices
    app.config['V1'] = V1
    app.config['V2'] = V2
    app.config['V3'] = V3
    app.config['Va'] = Va
    app.config['knn_result'] = knn_result
    
    from .routes.home import home_bp
    from .routes.artist import artist_bp
    from .routes.search import search_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(artist_bp)
    app.register_blueprint(search_bp)

    return app