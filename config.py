# ===========================
# 데이터 경로 설정
# ===========================

# 최종 통합된 분석용 CSV
FINAL_DATA_PATH = "data/processed/final_data.csv"

# 공공도서관 통계 데이터 (EDA용)
PUBLIC_STATS_PATH = "data/raw/2024_공공도서관_통계.xlsx"

# 원본 도서관 장서/대출 데이터 폴더
BASE_LIBRARY_PATH = "data/raw/libraries"

# 장서 엑셀 파일명 목록
LIBRARY_FILE_NAMES = [
    '관평도서관 장서 대출목록',
    '구암도서관 장서 대출목록',
    '구즉도서관 장서 대출목록',
    '노은도서관 장서 대출목록',
    '원신흥도서관 장서 대출목록',
    '유성도서관 장서 대출목록',
    '진잠도서관 장서 대출목록'
]

# 장서/대출 파일에서 필요한 열만 추출
COLUMNS_TO_KEEP = ['도서명', '저자', '출판사', 'ISBN', '주제분류번호', '대출건수']

# 대출량 상위 도서 저장 위치
OUTPUT_TOP_BOOK_DIR = "data/processed/top_books"

# 키워드 엑셀 (크롤링 및 분류 기반)
KEYWORD_EXCEL_PATH = "data/raw/상위도서_정보_크롤링.xlsx"
KEYWORD_CATEGORY_PATH = "data/raw/Keywords.xlsx"

# 크롤링 결과 저장
SUBJECT_CLASSIFICATION_OUTPUT_PATH = "data/output/subject_classifications.xlsx"

# 최종 병합된 데이터
FINAL_MERGED_OUTPUT_PATH = "data/output/final_merged_output.xlsx"


# ===========================
# 클러스터링 결과 파일
# ===========================

KEYWORD_MAPPING_OUTPUT_PATH = "Total_keyword_cluster_mapping.csv"
KEYWORD_CLUSTER_RESTRUCTURED_PATH = "Total_keyword_cluster_mapping_restructured.csv"
ISBN_CLUSTER_OUTPUT_PATH = "Total_isbn_cluster_mapping.csv"

# 클러스터 개수 설정
N_CLUSTERS = 25


# ===========================
# 시각화 결과
# ===========================

CA_FIGURE_OUTPUT_PATH = "data/output/ca_plot.png"  
EDA_VISUAL_OUTPUT_DIR = "data/output/eda_charts"
