import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import time
import random

# ----------------------------
# 1. 도서 주제 분류 스크래핑
# ----------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    )
}

def scrape_subject_classification(isbn):
    search_url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord={isbn}"

    try:
        search_response = requests.get(search_url, headers=HEADERS)
        search_soup = BeautifulSoup(search_response.text, 'html.parser')

        first_result_link = None
        for link in search_soup.select('a.bo3'):
            href = link.get('href')
            if href and href.startswith('http'):
                first_result_link = href
                break

        if not first_result_link:
            return {'ISBN': isbn, 'Subject Classification': None}

        book_response = requests.get(first_result_link, headers=HEADERS)
        book_soup = BeautifulSoup(book_response.text, 'html.parser')

        category_list = book_soup.select_one('#ulCategory')
        if category_list:
            categories = [li.text.strip() for li in category_list.find_all('li')]
            return {'ISBN': isbn, 'Subject Classification': " > ".join(categories)}
        else:
            return {'ISBN': isbn, 'Subject Classification': None}
    except Exception as e:
        print(f"[Error] ISBN: {isbn} | {e}")
        return {'ISBN': isbn, 'Subject Classification': None}

# ----------------------------
# 2. 병렬 실행 함수
# ----------------------------

def scrape_all_isbns(isbn_list, delay_every=100):
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_isbn = {executor.submit(scrape_subject_classification, isbn): isbn for isbn in isbn_list}
        for i, future in enumerate(as_completed(future_to_isbn)):
            result = future.result()
            results.append(result)

            if (i + 1) % 10 == 0:
                print(f"{i + 1}번째 ISBN 처리 완료.")

            if (i + 1) % delay_every == 0:
                print("잠시 대기 중...")
                time.sleep(0.5 + random.random())  # 0.5 ~ 1.5초 지연

    return pd.DataFrame(results)

# ----------------------------
# 3. 저장 함수
# ----------------------------

def save_scraped_results(df, output_path="subject_classifications.xlsx"):
    df.to_excel(output_path, index=False)
    print(f"[저장 완료] {output_path}")
