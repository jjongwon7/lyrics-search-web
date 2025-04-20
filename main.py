from app import create_app
app = create_app()
from app.utils.knn import knn_from_input_sentence, knn_result_to_html

if __name__ == "__main__":
    app.run(debug=True)

