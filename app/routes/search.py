from flask import Blueprint, render_template, request
from app.utils.knn import knn_from_input_sentence, knn_result_to_html

search_bp = Blueprint('search', __name__, template_folder='../templates')

@search_bp.route("/search", methods=["GET", "POST"])
def search_page():
    print('search_page_load_start')
    
    result = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = knn_from_input_sentence(user_input)
        result = knn_result_to_html(result)
    return render_template("search.html", result=result)
