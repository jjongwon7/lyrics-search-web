from flask import Blueprint, render_template, Flask
from flask import current_app

artist_bp = Blueprint('artist', __name__, template_folder='../templates')

@artist_bp.route("/artists")
def artist_list():
    artist_indices = current_app.config['artist_indices'] 
    return render_template("artists.html", artists=list(artist_indices.keys()))

@artist_bp.route("/artist/<artist_name>")
def artist_page(artist_name):
    data_list = current_app.config['data_list'] 
    artist_indices = current_app.config['artist_indices'] 
    if artist_name not in artist_indices:
        return "Artist not found!", 404
    indices = artist_indices[artist_name]
    song_name_list = [data_list[i]['song_name'] for i in indices]
    artist_data = list(zip(indices, song_name_list))

    print(artist_name)
    print(artist_data)
    return render_template("artist.html", artist=artist_name, artist_data=artist_data)

@artist_bp.route("/artist/<artist_name>/song/<song_name>/<idx>")
def song_page(artist_name, song_name, idx):
    data_list = current_app.config['data_list'] 
    knn_result = current_app.config['knn_result']
    idx = int(idx)
    data = data_list[idx]

    knn_songs = []
    for i, max_sim, mean_sim, min_sim in knn_result[idx]:
        t_data = data_list[i]
        knn_songs.append([i, t_data['artist_name'], t_data['song_name'], t_data['summary_1'], max_sim])
    
    return render_template("song.html", artist=artist_name, song=song_name, summary=data['summary_1'], knn_songs=knn_songs)
