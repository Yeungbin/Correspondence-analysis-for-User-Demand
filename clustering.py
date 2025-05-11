import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

from config import KEYWORD_MAPPING_OUTPUT_PATH, ISBN_CLUSTER_OUTPUT_PATH


# -----------------------------------------------------
# 1. 키워드 리스트 → 클러스터링
# -----------------------------------------------------

def tfidf_and_kmeans(keywords, n_clusters=25):
    """TF-IDF → KMeans 클러스터링"""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(keywords)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    kmeans.fit(X)
    labels = kmeans.labels_

    return pd.DataFrame({'Keyword': keywords, 'Cluster': labels})


def expand_clusters(keyword_cluster_df):
    """클러스터별 키워드를 컬럼으로 나누기"""
    clustered = keyword_cluster_df.groupby('Cluster')['Keyword'].apply(list).reset_index()
    max_len = clustered['Keyword'].apply(len).max()
    expanded = pd.DataFrame(clustered['Keyword'].tolist(), index=clustered['Cluster'])
    expanded.columns = [f'Keyword_{i+1}' for i in range(expanded.shape[1])]
    return expanded


# -----------------------------------------------------
# 2. 키워드 → ISBN 매핑
# -----------------------------------------------------

def map_keywords_to_clusters(keyword_list, mapping_df):
    """단일 ISBN 행에 대한 클러스터 추출"""
    clusters = mapping_df[mapping_df['Keyword'].isin(keyword_list)]['Cluster'].unique()
    return ', '.join([f'Cluster {c}' for c in clusters])


def assign_clusters_to_isbns(df_keywords, keyword_cluster_df):
    """모든 ISBN에 대해 클러스터셋을 부여"""
    keyword_columns = df_keywords.columns[1:]
    keywords = df_keywords[keyword_columns].apply(lambda x: x.dropna().tolist(), axis=1)
    df_keywords['Cluster set'] = keywords.apply(lambda x: map_keywords_to_clusters(x, keyword_cluster_df))
    return df_keywords[['ISBN', 'Cluster set']]


# -----------------------------------------------------
# 3. 전체 실행 함수
# -----------------------------------------------------

def run_keyword_clustering(df_keywords_raw, output_dir="data/output", n_clusters=25):
    # 1. 키워드 병합 및 클러스터링
    keywords_series = df_keywords_raw.iloc[:, 1:].apply(lambda x: x.dropna().tolist(), axis=1)
    keywords_flat = [kw for sublist in keywords_series.tolist() for kw in sublist]
    keyword_cluster_df = tfidf_and_kmeans(keywords_flat, n_clusters=n_clusters)

    # 2. 저장: 키워드-클러스터 매핑
    keyword_cluster_df.drop_duplicates().sort_values('Cluster')\
        .to_csv(os.path.join(output_dir, KEYWORD_MAPPING_OUTPUT_PATH), index=False, encoding='utf-8-sig')

    # 3. 저장: 구조화된 클러스터 키워드
    expanded = expand_clusters(keyword_cluster_df)
    expanded.to_csv(os.path.join(output_dir, "Total_keyword_cluster_mapping_restructured.csv"),
                    index=True, encoding='utf-8-sig')

    # 4. ISBN 매핑
    isbn_cluster_df = assign_clusters_to_isbns(df_keywords_raw, keyword_cluster_df)
    isbn_cluster_df.to_csv(os.path.join(output_dir, ISBN_CLUSTER_OUTPUT_PATH), index=False, encoding='utf-8-sig')

    print("[완료] 키워드 클러스터링 및 ISBN 매핑")
    return keyword_cluster_df, expanded, isbn_cluster_df
