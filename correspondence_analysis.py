import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import prince
import re
from scipy.spatial import distance
from tabulate import tabulate

from config import FINAL_DATA_PATH


def elementary_standardize(value):
    if pd.isna(value):
        return None
    mapping = {
        'Elementary': 'Elementary Students',
        'Elementary 5th-6th Grade': 'Elementary Students',
        'Elementary Grades 1-2': 'Elementary Students',
        'Elementary Grades 3-4': 'Elementary Students',
        'Elementary Students (All)': 'Elementary Students'
    }
    return mapping.get(value, value)


def calculate_100_series(value):
    value = str(value).strip("'")
    match = re.match(r'\d+(\.\d+)?', value)
    if match:
        numeric_value = float(match.group(0))
        return int(numeric_value // 100) * 100
    return None


def adjust_100_series(value):
    overrides = {4000: 400, 8500: 800, 8800: 800, 9800: 900, 5125100: 500}
    return overrides.get(value, value)


def adjust_academic_field(value):
    replacements = {
        'Business Management - Domestic Books': 'Business Management',
        'Chinese Character Learning/Domestic Books': 'Chinese Character Learning',
        'Comics/Domestic Books': 'Comics',
        'General - See More': 'General',
        'Literary Criticism - See More': 'Literary Criticism',
        'Investment/Finance - Domestic Books': 'Investment/Finance',
        'Marxism/Domestic Books': 'Marxism',
        'Parenting/Childcare - Domestic Books': 'Parenting',
        'Pedagogy/Domestic Books': 'Pedagogy',
        'Trends/Future Outlook - Domestic Books': 'Trends/Future Outlook',
        'Writing/Domestic Books': 'Writing'
    }
    return replacements.get(value, value)


def perform_correspondence_analysis(df, row_dim='Interests and Preferences', col_dim='도서관명'):
    print(f"[INFO] Performing CA for: {row_dim} vs {col_dim}")

    # 피벗 테이블 생성
    pivot_df = df.pivot_table(
        index=row_dim,
        columns=col_dim,
        values='대출건수',
        aggfunc='sum',
        fill_value=0
    )

    print("[Pivot Table]")
    print(tabulate(pivot_df, headers='keys', tablefmt='psql'))

    # 도서관명 영어로 번역
    replacements = {
        '관평도서관': 'Gwanpyeong', '구암도서관': 'Guam', '구즉도서관': 'Gujeuk',
        '노은도서관': 'Noeun', '원신흥도서관': 'Wonshinhung', '유성도서관': 'Yuseong', '진잠도서관': 'Jinjam'
    }
    pivot_df.rename(columns=replacements, inplace=True)

    # CA 수행
    ca = prince.CA(n_components=2)
    ca = ca.fit(pivot_df)

    eigenvalues = ca.eigenvalues_
    print("[Eigenvalues]")
    print(eigenvalues)

    total_inertia = sum(eigenvalues)
    explained_inertia = eigenvalues / total_inertia

    row_coords = ca.row_coordinates(pivot_df)
    col_coords = ca.column_coordinates(pivot_df)

    # 각 도서관에서 가까운 관심사 추출 (20%)
    closest_fields = {}
    total_fields = len(row_coords)
    x = max(2, int(total_fields * 0.2))

    for lib in col_coords.index:
        dists = distance.cdist([col_coords.loc[lib]], row_coords, 'euclidean').flatten()
        closest_indices = np.argsort(dists)[:x]
        closest_fields[lib] = row_coords.index[closest_indices]

    # 시각화
    fig, ax = plt.subplots(figsize=(10, 7))

    # 관심사 점 및 라벨
    for lib, fields in closest_fields.items():
        for field in fields:
            ax.scatter(row_coords.loc[field, 0], row_coords.loc[field, 1], color='blue')
            ax.annotate(field, (row_coords.loc[field, 0], row_coords.loc[field, 1]), color='blue')

    # 도서관 점 및 라벨
    ax.scatter(col_coords[0], col_coords[1], color='red')
    for i, txt in enumerate(col_coords.index):
        ax.annotate(txt, (col_coords.iloc[i, 0], col_coords.iloc[i, 1]), color='red')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    plt.title(f'Correspondence Analysis: {row_dim} by Library')
    plt.xlabel(f'Component 1 ({explained_inertia[0]*100:.2f}% explained)')
    plt.ylabel(f'Component 2 ({explained_inertia[1]*100:.2f}% explained)')
    plt.tight_layout()
    plt.show()

    return row_coords, col_coords, explained_inertia, closest_fields
