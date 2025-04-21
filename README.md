# 🎵Lyrics Explorer

## About the Project 
#### (EN)
Enter your current feelings or thoughts to find similar lyrics,
or explore songs with lyrics similar to those of your favorite artists.
About 20,000 songs from 250 artists are available. (As of 2025.04.20)

#### (KR)
현재의 기분이나 생각을 입력하고 유사한 가사를 찾고,
좋아하는 아티스트의 노래 가사와 유사한 다른 곡들을 찾아보세요
약 250 아티스트의 20,000개의 곡이 준비되어있습니다. (2025.04.20 기준)

## Web Demo 
URL : https://lyrics-search-web.onrender.com/
![image](https://github.com/user-attachments/assets/9e511168-8005-41e6-938f-f987c52946f7)


## Features in Development
1. Add Song urls (youtube, spotify)
2. Add User Request function to add new artists
3. Lyric similarity enhancement using non-lyrical elements (ex. audio-features, user comments)

## Tech Stack
- **Backend**: Python, Flask
- **ML/NLP**: Sentence-BERT, FAISS (KNN)
- **Frontend**: HTML, CSS

## Project Structure
lyrics_page/
├── main.py
├── app/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── routes/
│   └── utils/
├── templates/
├── static/
└── data/

## Author
Yeonji Lee – Data Scientist / NLP & Music Analytics Enthusiast
