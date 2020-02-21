#영화 추천 알고리즘 : 내가 재밌게 본 영화와 다른 사용자들의 평가간의 상관관계
#영화 입력시 다른 사람들 평가의 상관관계로 영화 추천
#영화 데이터셋 사용(45000개 영화 27만명의 유져가 평가한 2천 6백만개의 평가)
import numpy as np #행렬 연산 패키지
import pandas as pd #데이터 분산 패키지
import json

meta = pd.read_csv('C:/Users/i/Desktop/movie_recommendation_engine-master/the-movies-dataset/movies_metadata.csv')
meta.head() #데이터 프레임 첫 5줄 출력

#장르, 영화ID, 영화제목, 언어 추출
meta = meta[['id', 'original_title', 'genres']]
meta = meta.rename(columns={'id':'movieId'}) #id -> movieId 로 이름 바꾸기 (편리)
meta.head()

ratings = pd.read_csv('C:/Users/i/Desktop/movie_recommendation_engine-master/the-movies-dataset/ratings_small.csv')
#작은 파일 사용
ratings = ratings[['userId', 'movieId', 'rating']]
ratings.head()

ratings.describe() #데이터 간략한 정보 출력

#문자열을 숫자로 가공
meta.movieId = pd.to_numeric(meta.movieId, errors='coerce')
ratings.movieId = pd.to_numeric(ratings.movieId, errors='coerce')

#장르 배열 형태로 가공
def parse_genres(genres_str):
    genres = json.loads(genres_str.replace('\'', '"'))
    genres_list = []
    for g in genres:
        genres_list.append(g['name'])
    return genres_list #장르 리스트

meta['genres'] = meta['genres'].apply(parse_genres) #행마다 값 적용
meta.head()

data = pd.merge(ratings, meta, on='movieId', how='inner') #사용자 평가, 영화 합병->영화ID기준
#영화에 대한 평가 한줄로 나열
data.head()

#피벗테이블 생성
matrix = data.pivot_table(index='userId', columns='original_title', values='rating')
matrix.head(20)

#피어슨 상관관계 :
GENRE_WEIGHT = 0.1

def pearsonR(s1, s2):
    s1_c = s1 - s1.mean() #영화-영화평균 값
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))
#큰수 =상관관계가 높음 / 작은수 =상관관계가 낮음

#추천함수
def recommend(input_movie, matrix, n, similar_genre=True):
    input_genres = meta[meta['original_title'] == input_movie]['genres'].iloc(0)[0]
    result = []
    for title in matrix.columns: #영화 순서 루프
        if title == input_movie: #입력한 영화와 같은 영화 건너 뜀
            continue
        # rating comparison
        cor = pearsonR(matrix[input_movie], matrix[title])
        # genre comparison
        if similar_genre and len(input_genres) > 0:
            temp_genres = meta[meta['original_title'] == title]['genres'].iloc(0)[0]
            same_count = np.sum(np.isin(input_genres, temp_genres)) #영화 자료와 인풋으로 넣은 영화 장 비교
                #np.isin() : 배열 비교, 똑같은 요소 시 true 반
            cor += (GENRE_WEIGHT * same_count) #장르 가중치 증가
        if np.isnan(cor):
            continue
        else:
            result.append((title, '{:.2f}'.format(cor), temp_genres))
    result.sort(key=lambda r: r[1], reverse=True) #rating높은 순 정렬
    return result[:n] #n개 만큼 반환

movie_name=input("재밌게 본 영화 제목 입력 : ")
#여기에 사용자가 입력한 영화 없으면 다시 입력해라 등등 뜨게 하면 될듯 +a
recommend_result = recommend(movie_name, matrix, 10, similar_genre=True)
pd.DataFrame(recommend_result, columns = ['Title', 'Correlation', 'Genre'])
