from app.utils.knn import knn_from_input_sentence, knn_result_to_html, knn_result_to_json
from flask import Blueprint, render_template, request, jsonify
from flask import current_app
from flask_cors import CORS

search_bp = Blueprint('search', __name__, template_folder='../templates')
CORS(search_bp)

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
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = knn_from_input_sentence(user_input, model, data_list, V1, V2, V3, Va)
        result = knn_result_to_html(result, data_list)

    return render_template("search.html", result=result, input_sentence=user_input)


@search_bp.route("/api/search", methods=["POST"])
def search_page_restapi():
    model = current_app.config['model']
    data_list = current_app.config['data_list']
    V1 = current_app.config['V1']
    V2 = current_app.config['V2']
    V3 = current_app.config['V3']
    Va = current_app.config['Va']

    print('search_page_restAPI_load_start')

    data = request.get_json()
    if not data or "user_input" not in data:
        return jsonify({
            "status": "fail",
            "message": "Missing 'user_input' in request body"
        }), 400

    user_input = data["user_input"]

    try:
        result = knn_from_input_sentence(user_input, model, data_list, V1, V2, V3, Va)
        result = knn_result_to_json(result, data_list)

        return jsonify({
            "status": "success",
            "data": result,
            "message": "추천 성공"
        }), 200

    except Exception as e:
        current_app.logger.error(f"추천 중 오류 발생: {e}")
        return jsonify({
            "status": "error",
            "message": "Internal server error"
        }), 500