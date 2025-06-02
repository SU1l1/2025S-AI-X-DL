# 직장인 라이프스타일 기반 스트레스 연관관계 예측

## 👨‍💻 팀원 소개

| 학부                         | 이름   | 학번        | 이메일                      |
|------------------------------|--------|-------------|-----------------------------|
| 전자공학부                   | 이수호 | 2020053909  | dltngh2001@hanyang.ac.kr    |
| 로봇공학과                   | 손영훈 | 2020031276  | top21young@hanyang.ac.kr    |
| 차세대반도체융합공학부        | 박승우 | 2021073863  | seungwo7@hanyang.ac.kr      |
| 바이오신약융합학부 분자의약전공| 신동욱 | 2022016680  | hy2022016680@hanyang.ac.kr  |


## 📌 프로젝트 개요
- 직장인 스트레스 데이터셋을 바탕으로 어떤 요인이 가장 스트레스와 연관이 높은지 분석한다.

## 🏷️ 목적
- 각 피처를 바탕으로 어떠한 요인이 스트레스에 큰영항을 주는지 분석하고
- 스트레스 저감에 효과적인 행동 패턴 도출하여 본

## 🗂️ 데이터셋과 피처구성
- **출처:** (https://www.kaggle.com/datasets/chanchalagorale/employees-stress-level-dataset/data)
| 피처명                               | 설명                       | 예시                                  |
| --------------------------------- | ------------------------ | ----------------------------------- |
| **Employee\_Id**                  | 직원 ID                    | 1001, 1002, ...                     |
| **Avg\_Working\_Hours\_Per\_Day** | 하루 평균 근무 시간              | 8, 9, 10                            |
| **Work\_From**                    | 근무 장소                    | Home(재택), Office(사무실), Hybrid(혼합)   |
| **Work\_Pressure**                | 업무 압박(강도)                | High, Medium, Low                   |
| **Manager\_Support**              | 관리자 지원 수준                | Excellent, Good, Poor               |
| **Sleeping\_Habit**               | 수면 습관                    | Good, Average, Poor                 |
| **Exercise\_Habit**               | 운동 습관                    | Regular, Occasionally, None         |
| **Job\_Satisfaction**             | 직무 만족도                   | High, Medium, Low                   |
| **Work\_Life\_Balance**           | 워라밸(일과 삶의 균형)            | Yes(균형 유지), No(균형 미흡)               |
| **Social\_Person**                | 사교성 정도                   | Yes(활발), No(비활발)                    |
| **Lives\_With\_Family**           | 가족과 동거 여부                | Yes(동거), No(미동거)                    |
| **Working\_State**                | 근무/거주 지역(주 거주지)          | Delhi, Pune, Hyderabad, Karnataka 등 |
| **Stress\_Level**                 | 스트레스 수준 (1\~5 정수, 예측 타겟) | 1, 2, 3, 4, 5                       |


## 🛠️ 사용 기술
- Python (Pandas, Numpy, Scikit-learn, Matplotlib/Seaborn)
- Jupyter Notebook
- (추가 라이브러리: XGBoost, LightGBM, etc.)

## 🏃‍♂️ 프로젝트 구조


## 📝 주요 진행 내용

1. **데이터 전처리**
   - 결측치 처리, 이상치 처리, 데이터 타입 변환 등
2. **탐색적 데이터 분석(EDA)**
   - 변수 분포, 변수 간 상관관계 분석, 시각화
3. **특성 선택 및 엔지니어링**
   - 중요 피처 선정
4. **스트레스 지수 예측 모델링**
   - 회귀/분류 모델 적용 (예: RandomForest, XGBoost 등)
   - 평가 지표(MAE, RMSE, Accuracy 등)
5. **결과 해석**
   - 변수별 중요도, 라이프스타일별 스트레스 영향
6. **인사이트 도출 및 제언**
   - 스트레스 저감을 위한 라이프스타일 가이드

## 📊 예측 대상(타겟)
- 스트레스 지수(연속형/범주형)  
  (예: 1~100점 or Low/Medium/High 등급)

## 🗝️ 기대 효과
- 직장인 스트레스 관리 솔루션 기초 자료 제공
- 데이터 기반 라이프스타일 개선 방안 도출

## 🔗 참고 자료
- [데이터 출처 링크]
- [참고 논문/자료]

## 🚩 실행 방법 (예시)
```bash
# 환경설정
pip install -r requirements.txt

# 노트북 실행
jupyter lab
