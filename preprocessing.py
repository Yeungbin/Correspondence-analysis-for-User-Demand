import os
import pandas as pd
import numpy as np

from config import BASE_LIBRARY_PATH, LIBRARY_FILE_NAMES, COLUMNS_TO_KEEP, OUTPUT_TOP_BOOK_DIR


def load_library_data(file_path):
    """엑셀 파일에서 필요한 열만 로드"""
    return pd.read_excel(file_path, usecols=COLUMNS_TO_KEEP, engine='openpyxl')


def extract_top_20_percent(data):
    """대출건수 기준 상위 20% 도서 추출"""
    threshold = np.percentile(data['대출건수'], 80)
    return data[data['대출건수'] >= threshold]


def save_top_books(library_name, top_books_df):
    """상위 도서 데이터를 CSV로 저장"""
    filename = f"{library_name}_상위_20%.csv"
    path = os.path.join(OUTPUT_TOP_BOOK_DIR, filename)
    top_books_df.to_csv(path, index=False, encoding='utf-8-sig')
    print(f"[저장 완료] {path}")


def process_all_libraries():
    """모든 도서관 엑셀 파일을 처리하여 상위 도서 CSV로 저장"""
    for library_name in LIBRARY_FILE_NAMES:
        file_path = os.path.join(BASE_LIBRARY_PATH, f"{library_name}.xlsx")
        if not os.path.exists(file_path):
            print(f"[파일 없음] {file_path}")
            continue
        try:
            data = load_library_data(file_path)
            top_books = extract_top_20_percent(data)
            save_top_books(library_name, top_books)
        except Exception as e:
            print(f"[에러] {library_name}: {e}")
