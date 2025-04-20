#!/bin/bash

echo "data downloading..."

mkdir -p data
curl -L -o data/emb_list_1.pickle "$EMB_LIST_1_URL"
curl -L -o data/emb_list_2.pickle "$EMB_LIST_2_URL"
curl -L -o data/emb_list_3.pickle "$EMB_LIST_3_URL"
curl -L -o data/emb_list_all.pickle "$EMB_LIST_ALL_URL"
curl -L -o data/knn_result.pickle "$KNN_RESULT_URL"
curl -L -o data/lyrics_summary.csv "$LYRICS_SUMMARY_URL"

echo "download complete!"