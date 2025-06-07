# 직장인 라이프스타일 기반 스트레스 연관관계 예측


## 👨‍💻 팀원 소개

| 학부                         | 이름   | 학번        | 이메일                      |
|------------------------------|--------|-------------|-----------------------------|
| 전자공학부                   | 이수호 | 2020053909  | dltngh2001@hanyang.ac.kr    |
| 로봇공학과                   | 손영훈 | 2020031276  | top21young@hanyang.ac.kr    |
| 차세대반도체융합공학부        | 박승우 | 2021073863  | seungwo7@hanyang.ac.kr      |
| 바이오신약융합학부 분자의약전공| 신동욱 | 2022016680  | hy2022016680@hanyang.ac.kr  |


## 📌 프로젝트 개요
- 직장인 스트레스 데이터셋을 바탕으로 어떤 요인이 가장 스트레스와 연관이 높은지 분석하고 이를 바탕으로 스트레스 지수를 예측한다.

## 🏷️ 목적
### 직장인 라이프스타일과 스트레스 간의 연관관계 분석
- 본 프로젝트에서는 직장인의 근무 시간, 워라밸 지표(재택 근무 여부, 휴식 시간 확보 정도 등), 업무 강도(프로젝트 수, 마감 빈도 등) 및 생활 습관(운동 빈도, 수면 시간, 식사 패턴 등)과 스트레스 지수 간의 상관관계를 분석.

- 각 라이프스타일 변수와 스트레스 지수 사이의 상관계수를 계산하고, 회귀 분석 및 통계 검정을 통해 어떤 요소가 스트레스에 얼마나 큰 영향을 미치는지 파악할 예정.

- 이를 통해 “주당 50시간 이상 근무 시 스트레스 지수가 유의미하게 상승하는가?” 혹은 “운동 빈도가 높은 그룹은 전반적으로 낮은 스트레스 지수를 보이는가?”와 같은 구체적 인사이트를 도출.

### 라이프스타일에 따른 스트레스 예측
- 앞서 정의한 근무 시간, 워라밸 지표, 업무 강도, 생활 습관 등의 지표를 입력으로 하여, 딥러닝 모델을 활용해 직장인이 느끼는 스트레스 강도를 예측할 수 있을지를 탐구.

- 이를 통해 “이 지표들을 기반으로 개인별 스트레스 강도를 어느 정도 정확도로 예측할 수 있는가?”를 확인하고, 예측 결과가 유의미할 경우 실시간 스트레스 모니터링 시스템 개발의 가능성을 모색함.

## 📁 프로젝트 디렉토리 구조

![aixproject](https://github.com/user-attachments/assets/e9660967-eccd-4a41-ac86-eebd07b82a2b)


### 📄 파일 설명

- **train.csv**  
  - Kaggle에서 수집된 스트레스 관련 데이터셋
  - 전처리 후 분석 및 모델링에 사용됨.

- **rf_top_model.pkl**  
  - Random Forest 기반의 예측 모델 학습 결과 저장 파일
  - 중요 피처 3개를 기반으로 학습된 모델

- **stress_analysis.ipynb**  
  - Google Colab에서 실행되는 메인 노트북 파일
  - 데이터 전처리, EDA, 모델 학습, 평가, 시각화 등이 포함됨.


### 📂 데이터셋과 피처구성

- **출처:** [Kaggle: employees-stress-level-dataset](https://www.kaggle.com/datasets/chanchalagorale/employees-stress-level-dataset/data)

| 피처명                    | 설명                                 | 예시                                            |
|---------------------------|--------------------------------------|-------------------------------------------------|
| Employee_Id               | 직원 ID                              | 1001, 1002, ...                                 |
| Avg_Working_Hours_Per_Day | 하루 평균 근무 시간                   | 8, 9, 10                                        |
| Work_From                 | 근무 장소                            | Home(재택), Office(사무실), Hybrid(혼합)         |
| Work_Pressure             | 업무 압박(강도)                      | High, Medium, Low                               |
| Manager_Support           | 관리자 지원 수준                     | Excellent, Good, Poor                           |
| Sleeping_Habit            | 수면 습관                            | Good, Average, Poor                             |
| Exercise_Habit            | 운동 습관                            | Regular, Occasionally, None                     |
| Job_Satisfaction          | 직무 만족도                          | High, Medium, Low                               |
| Work_Life_Balance         | 워라밸(일과 삶의 균형)               | Yes(균형 유지), No(균형 미흡)                   |
| Social_Person             | 사교성 정도                          | Yes(활발), No(비활발)                           |
| Lives_With_Family         | 가족과 동거 여부                     | Yes(동거), No(미동거)                           |
| Working_State             | 근무/거주 지역(주 거주지)           | Delhi, Pune, Hyderabad, Karnataka 등            |
| Stress_Level              | 스트레스 수준 (1~5 정수, 예측 타겟)  | 1, 2, 3, 4, 5                                   |

- 클래스 불균형 확인
  
![클래스불균형](https://github.com/user-attachments/assets/81f899cd-7875-41fe-87bf-d7b2fc5bd701)

결과: 1~5 레벨이 거의 동일한 빈도로 분포하고 있어서 클래스 불균형 우려는 적음.

- 선형 상관관계 히트맵
  
![상관관계 히트맵](https://github.com/user-attachments/assets/b8760d8b-f76c-4d94-a148-3fc48a98dba7)


결과: Sleeping_Habit 과 Exercise_Habit Feature가 Stress_Level에 대해 타 Feature 대비 높은 연관성이 나타남.


## 🛠️ 사용 기술
- Python (Pandas, Numpy, Scikit-learn, Matplotlib/Seaborn)
- (추가 라이브러리: XGBoost, LightGBM, etc.)

## 📝 RandomForest 알고리즘을 사용하여 스트레스 지수 예측

### 학습/검증 데이터 분리

모델의 일반화 성능을 평가하기 위해 데이터를 학습용과 검증용으로 분리함. 클래스 불균형을 고려해 `stratify` 옵션을 사용함.

```python
X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```


---

### 전처리 파이프라인 구성

수치형 변수는 `StandardScaler`로 정규화하고, 범주형 변수는 `OneHotEncoder`로 원-핫 인코딩 진행. `ColumnTransformer`를 사용해 두 가지 전처리를 병렬로 적용함함.

```python
numeric_cols = [
    'Avg_Working_Hours_Per_Day','Work_Pressure','Manager_Support',
    'Sleeping_Habit','Exercise_Habit','Job_Satisfaction','Social_Person'
]
categorical_cols = [
    'Work_From','Work_Life_Balance','Lives_With_Family','Working_State'
]

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop='first', sparse_output=False)

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_cols),
    ('cat', categorical_transformer, categorical_cols)
])
```


---

### 모델 파이프라인 구성 및 학습

전처리와 랜덤 포레스트 분류기를 하나의 파이프라인으로 묶어 학습함. 랜덤 포레스트는 200개의 트리를 사용하며, 병렬 처리를 위해 `n_jobs=-1`로 설정함.

```python
clf = Pipeline([
    ('preproc', preprocessor),
    ('rf', RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    ))
])

clf.fit(X_train, y_train)
```


---

### 모델 평가

검증 데이터에 대해 예측을 수행하고 정확도와 분류 리포트를 출력.

```python
y_pred = clf.predict(X_val)
print(f"Validation Accuracy: {accuracy_score(y_val, y_pred):.4f}\n")
print("Classification Report:")
print(classification_report(y_val, y_pred))
```


---

###  RandomForest 모델을 이용한 예측 결과
**Accuracy:** `0.2083`  
<summary>📋 Classification Report</summary>

              precision    recall  f1-score   support

           1       0.23      0.23      0.23       122
           2       0.24      0.25      0.25       119
           3       0.20      0.18      0.19       118
           4       0.17      0.17      0.17       120
           5       0.20      0.21      0.21       121

    accuracy                           0.21       600
    macro avg       0.21     0.21      0.21       600
    weighted avg    0.21     0.21      0.21       600
 
<summary>🔢 Confusion Matrix</summary>

     28 18 26 23 27
     17 30 22 25 25
     28 24 21 21 24
     28 25 19 20 28
     23 26 19 27 26

**주요 기법:**

- ColumnTransformer를 활용한 체계적 전처리
- 수치형 변수: StandardScaler 적용
- 범주형 변수: OneHotEncoder (drop='first') 적용
- Pipeline으로 전처리와 모델 통합
- RandomForest 200개 트리 사용

**결과:** 20.83 %의 정확도는 무작위로 답을 찍을 경우 20 %의 확률인 점을 감안하면 심각하게 낮은 수치임. 이에 따라 


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

## 🔗 참고 자료
- [데이터 출처 링크]
- [참고 논문/자료]

## 🚩 실행 방법 
```bash
# 환경설정
pip install -r requirements.txt
