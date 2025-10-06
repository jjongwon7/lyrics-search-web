import numpy as np
from flask import current_app, url_for

def knn_from_input_sentence(input_sentence, model, data_list, V1, V2, V3, Va, k=10):
    """
    입력 문장과 가장 유사한 상위 5개 가사 데이터 서치
    
    Args:
      input_sentence (str): 사용자 입력 문장
      k (int, optional): 반환할 유사 곡 개수 
    
    Returns:
      knn_result : [index, max_similarity, mean_similarity, min_similarity] 를 유사도 순으로 정렬
    """
    
    v = model.encode(input_sentence) 
    v_norm = np.linalg.norm(v)
    
    S1 = (V1 @ v) / v_norm
    S2 = (V2 @ v) / v_norm
    S3 = (V3 @ v) / v_norm
    Sa = (Va @ v) / v_norm
    
    S_stack = np.column_stack((S1, S2, S3, Sa))
    S_max  = np.max(S_stack, axis=1)
    S_min  = np.min(S_stack, axis=1)
    S_mean = np.mean(S_stack, axis=1)
    
    knn_idx = np.argsort(S_max)[-k:][::-1]  
    
    knn_result = []
    for idx in knn_idx:
        t_data = data_list[idx]
        s_max, s_mean, s_min = round(float(S_max[idx]), 3), round(float(S_mean[idx]), 3), round(float(S_min[idx]), 3)
        knn_result.append([idx, s_max, s_mean, s_min])
    return knn_result

def knn_result_to_html(knn_result, data_list):
    """
    KNN 결과 리스트를 HTML 형식의 문자열로 변환

    Args:
        knn_result (list): knn_from_input_sentence 함수에서 반환된 유사도 결과 리스트.

    Returns:
        str: (아티스트명 - 곡명 - 가사요약 - 입력과의 유사도)를 concat한 문자열.
    """
    html_str = ''
    for idx, s_max, s_mean, s_min in knn_result:
        t_data = data_list[idx]
        artist_name, song_name = t_data['artist_name'], t_data['song_name']
        song_url = url_for('artist.song_page', artist_name=artist_name, song_name=song_name, idx=idx)

        pre_song_name = t_data['song_name']
        summary_1 = t_data['summary_1'].strip("\n")
        summary_3 = t_data['summary_3'].strip("\n").replace("\n","<br>")

        html_str += f"<b>{t_data['artist_name']} - {pre_song_name}</b>  "
        html_str += f"""<a href="{song_url}">(상세)</a><br>"""
        
        html_str += f"한줄 요약 : <span style='color: black;'>{summary_1}</span><br>"
        html_str += f"상세 요약 : <span style='color: gray;'>{summary_3}</span><br>" 
        html_str += f"입력 문장과의 유사도 : <span style='color: red;'>{s_max}</span><br>"
        html_str += "<br>"
    return html_str

def knn_result_to_json(knn_result, data_list):
    json_list = []
    for idx, s_max, s_mean, s_min in knn_result:
        t_data = data_list[idx]
        artist_name, song_name = t_data['artist_name'], t_data['song_name']
        song_url = url_for('artist.song_page', artist_name=artist_name, song_name=song_name, idx=idx)
        summary_1 = t_data['summary_1'].strip("\n")
        summary_3 = t_data['summary_3'].strip("\n")

        json_list.append({
            "artist_name": artist_name,
            "song_name": song_name,
            "song_url": song_url,
            "summary_1": summary_1,
            "summary_3": summary_3,
            "similarity": round(s_max * 100)
        })
    return json_list
