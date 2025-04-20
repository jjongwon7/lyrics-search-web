#!/bin/bash
pip install gdown

echo "data downloading..."
mkdir -p data
gdown --id "$FILE_ID_EMB_1" -O data/emb_list_1.pickle
gdown --id "$FILE_ID_EMB_2" -O data/emb_list_2.pickle
gdown --id "$FILE_ID_EMB_3" -O data/emb_list_3.pickle
gdown --id "$FILE_ID_EMB_ALL" -O data/emb_list_all.pickle
gdown --id "$FILE_ID_KNN_RESULT" -O data/knn_result.pickle
gdown --id "$FILE_ID_LYRICS_SUMMARY" -O data/lyrics_summary.csv
echo "download complete!"