from app.utils.knn import knn_from_input_sentence, knn_result_to_html
from flask import Blueprint, render_template, request
from flask import current_app

search_bp = Blueprint('search', __name__, template_folder='../templates')

@search_bp.route("/search", methods=["GET", "POST"])
def search_page():
    model = current_app.config['model'] 
    data_list = current_app.config['data_list'] 
    V1 = current_app.config['V1'] 
    V2 = current_app.config['V2'] 
    V3 = current_app.config['V3'] 
    Va = current_app.config['Va'] 
    
    print('search_page_load_start')
    
    result = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = knn_from_input_sentence(user_input, model, data_list, V1, V2, V3, Va)
        result = knn_result_to_html(result, data_list)
    return render_template("search.html", result=result)
