import pandas as pd


def replace_academic_keywords(text):
    replacements = {
        '문화': '문화/예술',
        '예술': '문화/예술',
        '수학': '수학/과학',
        '과학': '수학/과학',
        '사회': '사회/역사/철학',
        '역사': '사회/역사/철학',
        '철학': '사회/역사/철학',
    }
    for old, new in replacements.items():
        if old in str(text):
            text = text.replace(old, new)
    return text


def replace_target_audience_keywords(text):
    replacements = {
        '1~2학년': '초등 1~2학년',
        '3~4학년': '초등 3~4학년',
        '5~6학년': '초등 5~6학년',
        '초등': '초등학생(전체)',
        '초등학생': '초등학생(전체)',
        '유아': '유아'
    }
    for old, new in replacements.items():
        if old in str(text):
            text = text.replace(old, new)
    return text


def replace_book_genre_keywords(text):
    replacements = {
        '희곡': '소설/시/희곡',
        '문학': '문학',
        '그림책': '그림책',
        '추리': '추리/미스터리',
        '미스터리': '추리/미스터리',
    }
    for old, new in replacements.items():
        if old in str(text):
            text = text.replace(old, new)
    return text

# ----------------------------
# 2. 텍스트 정제 유틸
# ----------------------------

def remove_duplicates(text):
    if pd.isna(text):
        return text
    words = text.split(', ')
    return ', '.join(sorted(set(words), key=words.index))


def keep_first_word(text):
    return text.split(', ')[0] if pd.notnull(text) else text


def keep_priority_keyword(text):
    priorities = ['학년', '세', '초등', '어린이']
    words = text.split(', ')
    for priority in priorities:
        for word in words:
            if priority in word:
                return word
    return words[0] if words else ''


def find_valid_term(text):
    check_keywords = ['세', '년', '월', '봄', '여름', '가을', '겨울', '학년']
    terms = [term.strip() for term in text.split(',')]
    for term in terms:
        if not any(keyword in term for keyword in check_keywords) and not any(char.isdigit() for char in term):
            return term
    return terms[0]  # 예외적으로 첫 번째 단어 반환
