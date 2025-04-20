from app import create_app
app = create_app()

# from app.utils.knn import knn_from_input_sentence, knn_result_to_html
with app.app_context():
    from app.utils.knn import knn_from_input_sentence, knn_result_to_html
    from app.data_loader import load_data
    load_data(app)

if __name__ == "__main__":
    app.run(debug=True)

