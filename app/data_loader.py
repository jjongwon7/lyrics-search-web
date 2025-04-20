import numpy as np 
import pickle
import pandas as pd 
from collections import defaultdict
import re
import os
from sentence_transformers import SentenceTransformer

'''
load preprocessed data
- lyrics summary data
- pre-embeded lyrics summary data
- pre-computed knn results
- pre-trained language model (hugging face)
'''
# 1. load lyrics summary data
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def preprocess_song_name(song_name):
    return song_name.split("(")[0].lower().strip(' ')

def load_data():
    lyrics_summary_file_path = os.path.join(root_path, 'data', 'lyrics_summary.csv')
    lyrics_summary_df = pd.read_csv(lyrics_summary_file_path)
    
    # 2. load pre-embeded lyrics summary data
    with open(f"{root_path}/data/emb_list_1.pickle", 'rb') as f:
        emb_list_1 = pickle.load(f)
    with open(f"{root_path}/data/emb_list_2.pickle", 'rb') as f:
        emb_list_2 = pickle.load(f)
    with open(f"{root_path}/data/emb_list_3.pickle", 'rb') as f:
        emb_list_3 = pickle.load(f)
    with open(f"{root_path}/data/emb_list_all.pickle", 'rb') as f:
        emb_list_all = pickle.load(f)
    
    # 3. load pre-computed knn_result data
    with open(f"{root_path}/data/knn_result.pickle", 'rb') as f:
        knn_result = pickle.load(f)
    
    # 4. load pretrained language model
    model = SentenceTransformer("bespin-global/klue-sroberta-base-continue-learning-by-mnr") 
    
    '''
    preprocessing
        - V1, V2, V3, Va
        - data_list
        - artist_indices 
    '''
    # normalize lyrics summary embeddings
    V1 = np.array(emb_list_1).astype(np.float32)
    V1 /= np.linalg.norm(V1, axis=1, keepdims=True)
    
    V2 = np.array(emb_list_2).astype(np.float32)
    V2 /= np.linalg.norm(V2, axis=1, keepdims=True)
    
    V3 = np.array(emb_list_3).astype(np.float32)
    V3 /= np.linalg.norm(V3, axis=1, keepdims=True)
    
    Va = np.array(emb_list_all).astype(np.float32)
    Va /= np.linalg.norm(Va, axis=1, keepdims=True)
    
    # transform dataframe to list & drop duplicates (by preprocessed songname)
    lyrics_summary_df = lyrics_summary_df.rename(columns={'song_name': 'raw_song_name'})
    lyrics_summary_df['song_name'] = lyrics_summary_df['raw_song_name'].apply(preprocess_song_name)
    
    artist_song_names = defaultdict(set) 
    data_list = [] 
    for i, row in lyrics_summary_df.iterrows():
      artist_name, song_name = row['artist_name'], row['song_name']
      if song_name in artist_song_names[artist_name]: 
          continue
      artist_song_names[artist_name].add(song_name)
      data_list.append(row)
    
    # aggregate data indices by artist
    artist_indices = defaultdict(list)
    for i, data in enumerate(data_list):
        artist_name = data['artist_name']
        song_name   = re.sub(r'\u200b', '', data['song_name'])
        artist_indices[artist_name].append(i)
    artist_indices = dict(artist_indices)

    return model, data_list, artist_indices, V1, V2, V3, Va, knn_result