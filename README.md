# Correspondence-analysis-for-User-Demand

## 1. Summary

This project aimed to derive strategies to improve the accessibility and satisfaction of public library programs in Yuseong-gu, Daejeon. Regional cultural imbalances can lead to the disappearance of local areas, and to address this, public libraries play an important role in meeting the cultural needs of local residents and enhancing the cultural and artistic environment. In this study, a data-driven response analysis was conducted to resolve the mismatch between program supply and demand, through which customized program directions for each library were proposed.

## 2. Goal

The objective was to visually analyze the relationship between library users’ preferred topics and program attributes to identify any mismatches, and to derive a data-driven strategy to meet the cultural needs of the residents in Yuseong-gu, Daejeon.

## 3. Process

### **3-1. Analysis Background**

Public libraries have evolved beyond merely providing information to become multifaceted cultural hubs, playing a vital role in satisfying the cultural needs of local residents and enhancing the overall cultural level of the community. In particular, even though Daejeon City ranks among the highest nationwide in library usage (measured by visitors per branch and number of loans), the number of public library programs and their satisfaction levels remain relatively low. This suggests that public libraries in the Daejeon area are not adequately reflecting the public’s interests and expectations regarding books.

Therefore, this analysis focuses on Daejeon City with the aim of laying the groundwork for alleviating cultural imbalances in local areas by addressing the issues of insufficient and unsatisfactory public library programs.

### **3-2. EDA**

For a more tailored analysis, we plan to continue by selecting Yuseong-gu—the administrative district in Daejeon with the poorest performance in library programs. The reasons for this are as follows.

<img></img>

From a program accessibility perspective, the 2023 National Library Statistics show that Yuseong-gu leads Daejeon with the most public libraries and a top user count.

However, Yuseong-gu suffers from a severe lack of public library programs. Despite having more libraries and higher user counts than Daedeok-gu, it offers fewer programs. Similarly, even though Jung-gu has fewer libraries, the presence of the Daejeon Student Education and Culture Center—which offers many programs—and Hanbat Library, essentially Daejeon’s central library, further highlights that Yuseong-gu ranks low in program offerings despite its strong figures.

<img></img>

In Yuseong-gu, the satisfaction with public library programs is also low. The results of the satisfaction surveys conducted in 2022 and 2023 for Yuseong-gu public libraries reveal that satisfaction with library programs is noticeably lower compared to other areas of the library.

<img>

Furthermore, over half of the libraries in Yuseong-gu show a mismatch between the proportion of programs offered and the proportion of participants, indicating a supply-demand gap. The 2023 Library Statistics classify programs into four types: Culture Programs – Courses, Culture Programs – One-time events, Library and Reading Programs – Courses, and Library and Reading Programs – One-time events. In four of the seven libraries—Gwanpyeong, Gujeok, Noeun, and Jinjam—the ratios of events held to participants differ, suggesting that the program offerings do not meet the residents’ desires, which may contribute to lower satisfaction.

Therefore, this study aims, firstly, to identify the causes of dissatisfaction with Yuseong-gu public library programs, and secondly, to enhance the satisfaction and accessibility of these programs by proposing directions for program implementation and improvement that address the identified issues.

### **3-3. Hypothesis Setting**

In order to improve the satisfaction and accessibility of Yuseong-gu public library programs, this study set two hypotheses to analyze the supply-demand mismatch issue.

**1. The characteristics of library programs may differ from the actual usage requirements of library users.**

  - After deriving the preferred topics and interests of library users, we analyzed whether these align with the program themes.

  - It was hypothesized that if the program content does not match the users’ primary interests, it could lead to a decline in satisfaction.

**2. The library programs may be targeted toward groups other than the library’s main user base.**
   
  - We analyzed the relationship between each library’s primary user base (e.g., age, interests) and the target age group of the programs.

  - It was verified that if there is a mismatch between the main user base and the program audience, accessibility might suffer, and satisfaction levels could be lower.

### **3-4. Data Collection and Preprocessing**

**Book Data Collection**

  - **Target Libraries**

Seven public libraries in Yuseong-gu were selected as the analysis targets: Gwanpyeong Library, Gujeok Library, Noeun Library, Jinjam Library, Guam Library, Wonsinheng Library, and Yuseong Library. These libraries serve as primary cultural activity spaces for residents of Yuseong-gu, and their loan data enabled an analysis of user preferences and interests.

  - **Data Collection Process**

Using the “Library Information Naru” platform, the holdings and loan data for each library were collected. The data were sorted by loan frequency, and the top 20% of books based on loan frequency were classified as “popular books.” This classification helped derive the preferred topics of each library’s main user base.
A total of 226,129 records were collected, with the key attributes being:
    
  - **Book Title**: The title of the book
  - **Library Name**: The library that holds the book
  - **Author**: Information about the book’s author
  - **Publisher**: The publisher of the book
  - **ISBN**: The unique identifier for the book
  - **Subject Classification Number (KDC)**: The subject of the book based on the Korean Decimal Classification
  - **Loan Frequency**: The number of times the book was loaned



**Acquisition of Additional Attributes**

To analyze the attributes of popular books in greater detail, detailed subject classification values for each book were additionally collected from the Aladdin online bookstore. Based on Aladdin’s subject classifications, the book attributes were reclassified into the following four categories:

  - **Academic Field**: The academic subject matter addressed by the book (e.g., social sciences, natural sciences)
  - **Target Audience**: The readership the book is primarily aimed at (e.g., children, adults)
  - **Interests and Preferences**: The topics or themes covered by the book (e.g., history, literature)
  - **Genre**: The genre of the book (e.g., novel, essay)

The data were merged based on ISBN to form the final dataset, and books with insufficient related information, such as out-of-print books, were excluded from the analysis.

**Program Data Collection**

**- Target Libraries**

The analysis was conducted on the same seven public libraries in Yuseong-gu: Gwanpyeong Library, Gujeok Library, Noeun Library, Jinjam Library, Guam Library, Wonsinheng Library, and Yuseong Library.

**- Data Collection Process**

Using the “Monthly Event Announcement” menu on the Yuseong-gu Integrated Library website, all program data implemented in 2023 were collected. The program data include cultural programs, reading and book programs, and event programs provided by each library, and were organized according to the following items:

- **Library Name**: The library where the program was implemented
- **Target Age**: The primary age group targeted by the program (e.g., toddlers, elementary school students, adults)
- **Program Major Category**: The main theme or purpose of the program (e.g., reading education, cultural lectures)
- **Program Subcategory**: The detailed activity content (e.g., book discussions, history lectures)
- **Implementation Period**: The start and end dates of the program
- **Online/Offline Status**: The format in which the program was conducted

A total of 92 program records were secured, providing a foundational dataset for analyzing the relationship between program themes and target age groups.

**Final Dataset Overview**

  - **Role of Book Data**
    - The book data was used to understand the primary interests and preferences of library users.
    - By utilizing the KDC subject classification numbers, we analyzed which fields (e.g., social sciences, technology and science) users at each library are interested in.
    - Additionally, the Aladdin subject classification data was employed to further categorize users’ interests in greater detail.
  - Role of Program Data
    - The program data was used to analyze the attributes of the programs provided by each library.
    - We compared how well the target age groups and themes of each program align with the characteristics of the library user base.
    - We verified whether the number and types of programs are sufficient to meet the demands of the primary user group.
  - Final Dataset Composition and Preparation
    -   To visualize and interpret the analysis results, the book data and program data for each library were mapped together to derive the final outcomes.
    -   Through data cleaning, missing or duplicate data were removed, and the dataset was processed into a form suitable for correspondence analysis to examine relationships between categorical variables.
   
    
### 3-5. Data Analysis

Correspondence Analysis

Correspondence Analysis is a dimensionality reduction technique that visually represents relationships between categorical variables using a contingency table. Each category is plotted as a point, with the distance between points indicating their similarity or difference. This method enables a visual examination of how library users’ preferred topics relate to program attributes, revealing any mismatches, and simplifying complex data to clearly show patterns and correlations.
We employed Correspondence Analysis to visually explore the correlations in categorical data. By using loan frequency as a measure of each library’s usage demands and analyzing attributes of popular books (such as subject classification numbers, academic fields, target audiences, interests, and genres), we identified each library’s usage demands and determined whether a mismatch exists between the programs and user needs.

## 4.Result

### 4-1. Mismatch Case Analysis

The analysis revealed significant differences in the alignment between program supply and demand at Gwanpyeong Library and Yuseong Library.

1. **Gwanpyeong Library**: It was observed that the user interest topics—such as history (KDC 900 range) and literature (KDC 800 range)—differ significantly from the program topics actually offered. The programs focus on areas like technology and science, philosophy, and art, which fail to reflect the demands of the users.
2. **Yuseong Library**: In contrast, Yuseong Library demonstrated a high correlation between user interest topics and program topics, resulting in high satisfaction. Programs addressing social sciences (KDC 300 range) and technology and science (KDC 500 range) effectively met user demands.

Based on these mismatch case analysis results, the study verified two hypotheses and derived directions for improvement.

### 4-2. Hypothesis Verification

The data analysis confirmed that both hypotheses set in this study are valid.


각 공공도서관 – 주제분류번호(KDC) 대응분석 결과

**Hypothesis 1: The characteristics of library programs differ from the actual usage requirements of library users. **Correspondence analysis between the “library name” category and the subject classification number (KDC) category was used to verify whether there was a mismatch between user interest topics and program topics.

- **Yuseong Library**: Yuseong Library, which had high satisfaction levels, offered programs in areas such as social sciences (KDC 300 range) and technology and science (KDC 500 range)—for example, courses on coding, the metaverse, and virtual reality—that were strongly aligned with user interests.
- **Gwanpyeong Library**: Gwanpyeong Library, with lower satisfaction, showed a significant mismatch between the user interest topics (history in the KDC 900 range, natural sciences in the KDC 400 range) and the provided program topics (technology and science, philosophy, art), leading to a decline in satisfaction.

각 공공도서관 – 이용대상 대응분석 결과

**Hypothesis2 : The library programs are targeted toward groups other than the actual library users.**
Correspondence analysis between the “library name” category and the target audience category was performed to verify the alignment between the main user base and the program target audience.

- Yuseong Library: Analysis indicated that Yuseong Library’s main user groups were elementary school students and adults, and it predominantly offered programs targeting these age groups, which corresponded with high satisfaction.
- Gwanpyeong Library: Although the primary user base at Gwanpyeong Library included adults and children (preschoolers and elementary students), there was a notable deficiency in programs targeted at adults. This mismatch between the primary user base and the program target age groups can be interpreted as a contributing factor to lower satisfaction.


### 4-3. Program Improvement Directions by Library

Based on the results of the hypothesis verification, program improvement directions for each library have been proposed.

**Gwanpyeong Library**

- **Increase Programs for Adult**s: It is necessary to raise the proportion of programs designed for adults, who constitute the main user group, and to additionally introduce programs related to childcare and education.
- **Launch Programs Reflecting User Interests**: Programs covering history (KDC 900 range) and natural sciences (KDC 400 range) should be increased to strengthen the connection with user interests.
  
**Gujeok Library**

- **Add Programs for Preschool Children**: Since only programs targeting elementary students are currently offered, it is necessary to introduce programs for preschool children to better meet the demands of the main user group.

**Noeun Library**

- **Increase Programs for Children**: Programs reflecting the interests of children (including preschoolers and elementary students), such as literature and educational books, need to be strengthened.
- **Plan Literature-Centered Programs**: Programs aimed at the overall user base should focus on literature, particularly family and children’s literature.
  
**Jinjam Library**

- **Increase Math/Science-Focused Programs**: Programs should be planned around math and science, which are the main interests, and additional programs targeting various age groups should be developed.
- **Provide Age-Specific Tailored Programs**: The proportion of programs aimed at children and elementary students should be expanded to satisfy user demands.

### 4-4. Implications

The findings of this study suggest that tailoring the direction of public library programs regionally can contribute to alleviating cultural imbalances in local areas. This methodology is applicable to public libraries in other regions and can be used to enhance regional cultural development and increase resident satisfaction.

