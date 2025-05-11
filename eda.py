import pandas as pd
import matplotlib.pyplot as plt
import os


def load_and_filter_daejeon_data(file_path):
    data = pd.read_excel(file_path)
    return data[data['지역'] == '대전']


def plot_visitors_by_district(df):
    df['이용자수_도서관방문자수'] = pd.to_numeric(df['이용자수_도서관방문자수'], errors='coerce').fillna(0).astype(int)
    grouped = df.groupby('시군구')['이용자수_도서관방문자수'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(14, 8))
    grouped.plot(kind='bar', x='시군구', ax=ax, width=0.8)
    plt.title('대전 시군구별 이용자 수')
    plt.xlabel('시군구')
    plt.ylabel('이용자 수')
    plt.xticks(rotation=45, ha='right', fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.show()


def plot_library_counts_by_district(df):
    counts = df['시군구'].value_counts().reset_index()
    counts.columns = ['시군구', '도서관 수']
    ordered = ['대덕구', '동구', '서구', '유성구', '중구']
    counts['시군구'] = pd.Categorical(counts['시군구'], categories=ordered, ordered=True)
    counts = counts.sort_values('시군구')

    fig, ax = plt.subplots(figsize=(14, 8))
    counts.plot(kind='bar', x='시군구', y='도서관 수', ax=ax, width=0.8)
    plt.title('대전 시군구별 공공도서관 개수', fontsize=16)
    plt.xlabel('시군구', fontsize=14)
    plt.ylabel('도서관 수', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.show()
    

def plot_total_programs_by_district(df):
    program_cols = [col for col in df.columns if '실시횟수' in col]
    for col in program_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    df['총 프로그램 실시 횟수'] = df[program_cols].sum(axis=1)
    grouped = df.groupby('시군구')['총 프로그램 실시 횟수'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(14, 8))
    grouped.plot(kind='bar', x='시군구', y='총 프로그램 실시 횟수', ax=ax, width=0.8)
    plt.title('대전 시군구별 총 프로그램 실시 횟수 (오프라인 + 온라인)')
    plt.xlabel('시군구')
    plt.ylabel('총 프로그램 실시 횟수')
    plt.xticks(rotation=45, ha='right', fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.show()


def plot_programs_by_library(df):
    df = df[df['시군구'] == '유성구']
    program_cols = [col for col in df.columns if '실시횟수' in col]
    for col in program_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    df['문화프로그램_강좌수_실시횟수'] = df['오프라인_문화프로그램_강좌수_실시횟수'] + df['온라인_문화프로그램_강좌수_실시횟수']
    df['문화프로그램_1회성프로그램_실시횟수'] = df['오프라인_문화프로그램_1회성프로그램_실시횟수'] + df['온라인_문화프로그램_1회성프로그램_실시횟수']
    df['도서관 및 독서 관련 프로그램_강좌수_실시횟수'] = df['오프라인_도서관 및 독서 관련 프로그램_강좌수_실시횟수'] + df['온라인_도서관 및 독서 관련 프로그램_강좌수_실시횟수']
    df['도서관 및 독서 관련 프로그램_1회성프로그램_실시횟수'] = df['오프라인_도서관 및 독서 관련 프로그램_1회성프로그램_실시횟수'] + df['온라인_도서관 및 독서 관련 프로그램_1회성프로그램_실시횟수']

    grouped = df.groupby('도서관명').agg({
        '문화프로그램_강좌수_실시횟수': 'sum',
        '문화프로그램_1회성프로그램_실시횟수': 'sum',
        '도서관 및 독서 관련 프로그램_강좌수_실시횟수': 'sum',
        '도서관 및 독서 관련 프로그램_1회성프로그램_실시횟수': 'sum'
    }).reset_index()

    fig, ax = plt.subplots(figsize=(14, 8))
    grouped.plot(kind='bar', x='도서관명', ax=ax, width=0.8)
    plt.title('유성구 도서관별 프로그램 실시 횟수 (오프라인 + 온라인)')
    plt.xlabel('도서관명')
    plt.ylabel('프로그램 실시 횟수')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
