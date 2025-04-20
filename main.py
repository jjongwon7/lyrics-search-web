from app.utils.knn import knn_from_input_sentence, knn_result_to_html
from app.data_loader import data_list, model
from app import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)

