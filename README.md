# 직장인 라이프스타일 기반 스트레스 연관관계 예측


## I. 팀원 소개

| 학부                         | 이름   | 학번        | 이메일                      |
|------------------------------|--------|-------------|-----------------------------|
| 전자공학부                   | 이수호 | 2020053909  | dltngh2001@hanyang.ac.kr    |
| 로봇공학과                   | 손영훈 | 2020031276  | top21young@hanyang.ac.kr    |
| 차세대반도체융합공학부        | 박승우 | 2021073863  | seungwo7@hanyang.ac.kr      |
| 바이오신약융합학부 분자의약전공| 신동욱 | 2022016680  | hy2022016680@hanyang.ac.kr  |


## II. 프로젝트 개요
- 직장인 스트레스 데이터셋을 바탕으로 어떤 요인이 가장 스트레스와 연관이 높은지 분석하고 이를 바탕으로 스트레스 지수를 예측한다.

## III. 목적
### 직장인 라이프스타일과 스트레스 간의 연관관계 분석
- 본 프로젝트에서는 직장인의 근무 시간, 워라밸 지표(재택 근무 여부, 휴식 시간 확보 정도 등), 업무 강도(프로젝트 수, 마감 빈도 등) 및 생활 습관(운동 빈도, 수면 시간, 식사 패턴 등)과 스트레스 지수 간의 상관관계를 분석.

- 각 라이프스타일 변수와 스트레스 지수 사이의 상관계수를 계산하고, 회귀 분석 및 통계 검정을 통해 어떤 요소가 스트레스에 얼마나 큰 영향을 미치는지 파악할 예정.

- 이를 통해 “주당 50시간 이상 근무 시 스트레스 지수가 유의미하게 상승하는가?” 혹은 “운동 빈도가 높은 그룹은 전반적으로 낮은 스트레스 지수를 보이는가?”와 같은 구체적 인사이트를 도출.

### 라이프스타일에 따른 스트레스 예측
- 앞서 정의한 근무 시간, 워라밸 지표, 업무 강도, 생활 습관 등의 지표를 입력으로 하여, 딥러닝 모델을 활용해 직장인이 느끼는 스트레스 강도를 예측할 수 있을지를 탐구.

- 이를 통해 “이 지표들을 기반으로 개인별 스트레스 강도를 어느 정도 정확도로 예측할 수 있는가?”를 확인하고, 예측 결과가 유의미할 경우 실시간 스트레스 모니터링 시스템 개발의 가능성을 모색함.

## IV. 프로젝트 파일 구조

![프로젝트구조](https://github.com/user-attachments/assets/32bbfef0-977c-4f77-9e2e-e722351eff16)


### 파일 설명

- **train.csv**  
  - Kaggle에서 수집된 스트레스 관련 데이터셋
  - 전처리 후 분석 및 모델링에 사용됨.

- **stress_predict_rf.py**  
  - XGBOOST 기반의 예측 모델 학습 결과 저장 파일
  - 중요 피처 2개를 기반으로 학습된 모델


### 데이터셋과 피처구성

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


## V. 사용 라이브러리

| **라이브러리** | **기능** |
| :-- | :-- |
| **pandas** | 데이터 조작 및 분석 |
| **sklearn.model_selection** | 데이터 분할 |
| **sklearn.metrics** | 모델 성능 평가 |
| **Matplotlib** | 데이터 시각화 |
| **RandomForest** | 다수의 결정 트리를 통한 머신러닝|
| **XGBoost** | 그래디언트 부스팅 머신러닝 |

## VI. RandomForest 알고리즘을 사용한 스트레스 지수 예측

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

수치형 변수는 `StandardScaler`로 정규화하고, 범주형 변수는 `OneHotEncoder`로 원-핫 인코딩 진행. `ColumnTransformer`를 사용해 두 가지 전처리를 병렬로 적용함.

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

- ColumnTransformer를 활용한 전처리
- 수치형 변수: StandardScaler 적용
- 범주형 변수: OneHotEncoder (drop='first') 적용
- Pipeline으로 전처리와 모델 통합
- RandomForest 200개 트리 사용

---
### 결과: 
#### 20.83 %의 정확도는 무작위로 답을 찍을 경우 정답일 확률이 20 %인 점을 감안하면, 심각하게 낮은 수치임.
#### 이에 따라 본 팀은, 알고리즘과 전처리, Feature Engineering 관점에서 코드를 수정하여 정확도 향상을 시도해보기로 함.

## VII. 정확도 향상

## 1) **머신러닝 알고리즘 변경**
   
#### 실험한 모델 및 특징 요약

| 모델              | 주요 특징 요약                                           |
|-------------------|-----------------------------------------------------------|
| LogisticRegression | 선형 모델, 빠르고 간단. `class_weight='balanced'` 적용 |
| RandomForest       | 비선형 모델, 변수 중요도 파악 용이                      |
| CatBoost           | 빠르고 튜닝 내성 강함, 범주형 자동 처리 가능            |
| XGBoost            | 정밀한 예측, 부스팅 계열 대표 모델                      |
| MLPClassifier      | 신경망 기반, 비선형 학습 가능                           |
| SVM                | 결정 경계 기반, 소규모에 적합                           |
| LDA                | 선형 분리 기반, 해석력 우수                              |

---

### 모델별 결과

#### Logistic Regression  
**Accuracy:** `0.18`  
<summary>📋 Classification Report</summary>

              precision    recall  f1-score   support

           0       0.17      0.11      0.13       122
           1       0.18      0.26      0.22       119
           2       0.22      0.02      0.03       118
           3       0.17      0.23      0.20       120
           4       0.19      0.29      0.23       121

    accuracy                           0.18       600
    macro avg      0.19      0.18      0.16       600
    weighted avg   0.19      0.18      0.16       600


<summary>🔢 Confusion Matrix</summary>

      6 35 11 37 33
      3 33 11 43 29
     11 30  6 27 44
      7 35 12 30 36
      9 44  2 33 33

---

#### Random Forest  
**Accuracy:** `0.195`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support
           0       0.25      0.29      0.27       122
           1       0.12      0.12      0.12       119
           2       0.21      0.21      0.21       118
           3       0.17      0.16      0.17       120
           4       0.21      0.20      0.20       121

    accuracy                           0.20       600
    macro avg      0.19      0.19      0.19       600
    weighted avg   0.19      0.20      0.19       600

<summary>🔢 Confusion Matrix</summary>

     35 29 19 21 18
     32 14 25 20 28
     26 23 25 21 23
     21 26 31 19 23
     25 26 17 29 24

---

#### CatBoost  
**Accuracy:** `0.1983333`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support

           0       0.25      0.27      0.26       122
           1       0.17      0.16      0.16       119
           2       0.22      0.19      0.21       118
           3       0.16      0.15      0.16       120
           4       0.18      0.21      0.20       121

    accuracy                           0.20       600
    macro avg      0.20      0.20      0.20       600
    weighted avg   0.20      0.20      0.20       600

<summary>🔢 Confusion Matrix</summary>

     33 19 21 21 28
     26 19 22 23 29
     29 25 23 20 21
     21 24 20 18 37
     21 26 20 28 26

---

#### XGBoost  
**Accuracy:** `0.2366666`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support

           0       0.32      0.35      0.33       122
           1       0.19      0.19      0.19       119
           2       0.25      0.25      0.25       118
           3       0.18      0.16      0.17       120
           4       0.23      0.23      0.23       121

    accuracy                           0.24       600
    macro avg      0.23      0.24      0.23       600
    weighted avg   0.23      0.24      0.24       600


<summary>🔢 Confusion Matrix</summary>

     43 18 17 19 25
     29 23 20 22 25
     20 26 29 22 21
     26 27 25 19 23
     17 29 23 24 28

---

#### MLPClassifier  
**Accuracy:** `0.17`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support

           0       0.20      0.18      0.19       122
           1       0.17      0.15      0.16       119
           2       0.24      0.24      0.24       118
           3       0.12      0.12      0.12       120
           4       0.13      0.16      0.15       121

    accuracy                           0.17       600
    macro avg      0.17      0.17      0.17       600
    weighted avg   0.17      0.17      0.17       600

<summary>🔢 Confusion Matrix</summary>

     22 20 23 30 27
     18 18 19 19 45
     25 20 28 28 17
     26 22 24 15 33
     21 23 23 35 19

---

#### SVM  
**Accuracy:** `0.1683333`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support

           0       0.19      0.17      0.18       122
           1       0.21      0.21      0.21       119
           2       0.18      0.13      0.15       118
           3       0.13      0.14      0.14       120
           4       0.15      0.19      0.17       121

    accuracy                           0.17       600
    macro avg      0.17      0.17      0.17       600
    weighted avg   0.17      0.17      0.17       600

<summary>🔢 Confusion Matrix</summary>

     22 20 23 30 27
     18 18 19 19 45
     25 20 28 28 17
     26 22 24 15 33
     21 23 23 35 19

---

#### LDA  
**Accuracy:** `0.18166666`  
<summary>📋 Classification Report</summary>

               precision    recall  f1-score   support

           0       0.17      0.11      0.13       122
           1       0.18      0.26      0.22       119
           2       0.22      0.02      0.03       118
           3       0.17      0.23      0.20       120
           4       0.19      0.29      0.23       121

    accuracy                           0.18       600
    macro avg      0.19      0.18      0.16       600
    weighted avg   0.19      0.18      0.16       600

<summary>🔢 Confusion Matrix</summary>

     13 34  4 38 33
     16 31  1 37 34
     18 29  2 25 44
     21 33  0 28 38
     10 42  2 32 35

---

#### 모델별 실험 요약

| 모델               | Accuracy | Macro F1 |
|--------------------|----------|----------|
| LogisticRegression | 0.18     | 0.16     |    
| RandomForest       | 0.20     | 0.19     |       
| CatBoost           | 0.20     | 0.20     |        
| XGBoost            | **0.24** | **0.23** |             
| MLPClassifier      | 0.17     | 0.17     |         
| SVM                | 0.17     | 0.17     |    
| LDA                | 0.18     | 0.16     |      

- **최고 성능 모델:** XGBoost (Accuracy: 0.2367, Macro F1: 0.23)  
- **분석:** 예측 난이도가 높아 전반적으로 정확도의 향상 폭이 미미하나, XGBoost 알고리즘의 정확도가 가장 높게 나왔음.

## 2) **다양한 전처리 적용**

### 적용된 전처리 기법 및 특징 요약

| 접근 방법 | 주요 특징 요약 |
| :-- | :-- |
| 기본 RandomForest | 원-핫 인코딩 + StandardScaler + class_weight='balanced' |
| 클래스 불균형 | SMOTE + 부트스트래핑 + 클래스 가중치 조정 |
| 고급 전처리 | 이상치 처리(IQR) + 빈도 기반 인코딩 + 상호정보량 특성 선택 |
| 전처리 최소화 | 스케일링 제거 + 간단한 레이블 인코딩 + 하이퍼파라미터 최적화 |
| 모델 앙상블 | 3개 모델 조합 + 소프트 투팅 + 교차 검증 |
| 전처리 극최소화 | 절대 최소 전처리 + 기본 RandomForest |


---

### 전처리 방법별 결과

#### 기본 랜덤포레스트

**Accuracy:** `0.21`

**설명:**

- 원-핫 인코딩 (Work_From, Working_State)
- Yes/No → 1/0 변환
- StandardScaler 적용
- class_weight='balanced'

---

#### 클래스 불균형

**Accuracy:** `0.19`

**설명:**

- SMOTE 적용으로 클래스 균형 맞춤
- 부트스트래핑으로 데이터 증강
- 클래스 가중치 수동 조정
---

#### 고급 전처리 기법

**Accuracy:** `0.21`

**설명:**

- IQR 방법으로 이상치 처리
- 빈도 기반 + 레이블 인코딩
- 상호정보량 기반 특성 선택
- ADASYN, SMOTEENN 등 고급 샘플링

---

#### 전처리 최소화

**Accuracy:** `0.21`

**설명:**

- 스케일링 완전 제거
- 간단한 레이블 인코딩만 사용
- 하이퍼파라미터 그리드 서치
- 복잡한 샘플링 기법 제거

---

#### 모델 앙상블

**Accuracy:** `0.18`

**설명:**

- RandomForest 2개 + ExtraTrees 1개
- 소프트 투팅 앙상블
- 5-fold 교차 검증
- 순서 기반 인코딩

---

#### 전처리 극최소화

**Accuracy:** `0.20`

**주요 기법:**

- 절대 최소한의 전처리
- 기본 RandomForestClassifier 설정
- class_weight 옵션만 조정
- 복잡한 기법 모두 제거

---

#### 전처리 기법별 실험 요약

| 접근 방법            | Accuracy | 주요 특징 요약                                   |
|---------------------|----------|--------------------------------------------------|
| 기본 랜덤포레스트     | 0.21     | 원-핫 인코딩, 스케일링, class_weight='balanced'    |
| 클래스 불균형    | 0.19     | SMOTE, 클래스 가중치 조정, 부트스트랩             |
| 고급 전처리      | 0.21     | IQR 이상치 제거, 상호정보량 기반 특성 선택        |
| 전처리 최소화      | 0.21     | 레이블 인코딩만 적용, 하이퍼파라미터 튜닝          |
| 모델 앙상블         | 0.18     | RandomForest+ExtraTrees 조합, 소프트 보팅        |
| 전처리 극최소화        | 0.20     | 최소한의 전처리와 기본 설정 유지                 |

- **최고 성능 :** 기본 랜덤포레스트 (Accuracy: 0.21)  
- **분석:** 간단한 레이블 인코딩, 스케일링 제거, class_weight='balanced' 정도의 단순한 전처리가 가장 효과적임.

## 3) **Feature Engineering**

### 피처 조합 목록 및 가설

---

#### 업무환경 관련

- **Avg_Working_Hours_Per_Day + Work_Pressure**  
  → *“근무 시간이 길고 업무 강도도 높을 때 스트레스는 더 커질 수 있다”*

- **Work_From + Work_Life_Balance**  
  → *“재택근무와 워라밸이 서로 어떤 영향을 미치는가?”*

- **Work_From + Lives_With_Family**  
  → *“재택근무 시 가족과 함께 사는가에 따라 스트레스에 미치는 영향이 다를 수 있음”*

---

#### 생활습관 관련

- **Sleeping_Habit + Exercise_Habit**  
  → *“수면 + 운동 습관이 좋은 경우 스트레스가 낮을 수 있음”*

- **Sleeping_Habit + Work_Pressure**  
  → *“업무 스트레스가 수면에 영향을 미치고, 반대로도 영향 가능”*

- **Exercise_Habit + Work_Life_Balance**  
  → *“운동을 한다는 건 워라밸이 잘 유지되고 있다는 신호일 수 있음”*

---

#### 심리/지원 관련

- **Manager_Support + Job_Satisfaction**  
  → *“관리자 지원이 만족도에 영향을 미치고, 결국 스트레스를 낮추는 방향으로 작용할 수 있음”*

- **Job_Satisfaction + Work_Pressure**  
  → *“스트레스가 높을수록 직무 만족도가 낮을 수 있다”*

---

#### 성격/주거 관련

- **Social_Person + Lives_With_Family**  
  → *“사교성이 높고 가족과 함께 사는 사람이 스트레스를 덜 받을 수도 있음”*

- **Social_Person + Work_From**  
  → *“사교적인 사람이 재택근무일 경우 외로움을 더 많이 느낄 수 있다 → 스트레스 증가 가능성”*

---

#### 지역 기반

- **Working_State + Work_From**  
  → *“지역별 재택/사무실 출근 비율이 다르므로, 이 조합으로 지역별 스트레스 차이 파악 가능”*

- **Working_State + Stress_Level** *(검증용)*  
  → *“지도 기반 스트레스 분포 등도 나중에 분석할 수 있음”*


다음과 같이 연관된 피처 쌍들을 기반으로 학습을 진행.

#### 피처 조합 기반 실험 결과 요약

| 피처 조합                                                      | Accuracy | Macro F1 | 특징 요약                                |
|---------------------------------------------------------------|----------|----------|------------------------------------------|
| Avg_Working_Hours + Work_Pressure                              | 0.2017   | 0.2018   | 업무량과 압박의 상관관계                 |
| Work_From + Work_Life_Balance                                  | 0.2050   | 0.1729   | 특정 클래스(2) 예측 실패                 |
| Sleeping_Habit + Exercise_Habit                                | 0.2083   | 0.2067   | 전반적으로 균형 잡힌 성능                 |
| Manager_Support + Job_Satisfaction                             | 0.1900   | 0.1852   | 정서적 지원과 만족도의 상호작용          |
| Job_Satisfaction + Work_Pressure                               | 0.1950   | 0.1843   | 스트레스와 만족도의 역관계 일부 포착      |
| Social_Person + Lives_With_Family                              | 0.1700   | 0.1627   | 사회성 및 주거환경만으로는 한계           |
| Avg_Working_Hours + Job_Satisfaction                           | 0.2067   | 0.2062   | 업무시간과 만족도의 조합                 |
| Avg_Working_Hours + Work_Life_Balance                          | 0.2150   | 0.2133   | 워라밸과 업무량 조합, 안정적 성능         |
| Avg_Working_Hours + Work_From                                  | 0.2033   | 0.1997   | 재택/출근 여부에 따른 업무량 영향 분석    |
| Avg_Working_Hours + Work_Life_Balance + Job_Satisfaction       | 0.2117   | 0.2103   | 업무·정서 복합 조합                       |
| **Avg_Working_Hours + Sleeping_Habit**                        | **0.2333** | **0.2321** | **🔥 현재 최고 성능 조합**   |

- **최고 성능 :** Avg_Working_Hours + Sleeping_Habit 이 두 개의 feature만을 가지고 예측한 결과가 가장 높은 정확도를 보였음 (Accuracy: 0.23).  
- **분석:** 과도한 업무량 스트레스와 수면 회복력 간 상호작용이 스트레스 지수를 예측하는 데에 도움을 주는 것으로 예상됨.

## 최종 예측
- 위의 결과에 따라, 알고리즘은 XGBoost, 전처리를 적용하지 않고 XGBoost의 기본 수치형 변수를 사용하며, 평균 근무 시간과 수면 습관의 두 가지 feature만을 가지고 예측을 시도해보기로 하였음.
→ XGBoost + 2 Feature 만을 사용하여 예측.


https://github.com/user-attachments/assets/8e688ef0-750c-40e8-adc4-39845c077924



- 그 결과, 예측 정확도를 25.5% 까지 증가시킬 수 있었음.



## VIII. 결론 및 시사점

### XGBoost가 RandomForest보다 높은 정확도를 보였던 이유?

- Random forest는 bagging 기반 앙상블로 여러 개의 결정 트리를 생성해 각 결과를 투표 또는 평균하여 최종 결과를 도출. 각 트리는 부분 데이터와 부분 feature만 사용해 훈련하여 분산을 감소시킴.
  
- XGBoost는 boosting 기반 앙상블로 새로운 트리를 추가하여 이전 트리의 오차를 학습하는 과정을 통해 성능을 향상시킴. 예측이 잘못된 샘플에 더 많은 가중치를 부여해 개선함. 손실함수를 줄이는 방식으로 점점 더 정확한 모델을 완성함.
  
- XGBoost가 Random Forest보다 더 적합한 상황은
  1) 모델 성능(정확도)를 극대화해야 하는 경우
  2) 데이터가 복잡하거나 불균형한 경우(변수 간 상호작용이 많고, 선형성이 없는 복잡한 데이터)임.

   이는 XGBoost가 Gradient Boosting 방식을 따라, 각 단계에서 이전 모델의 오차를 줄이기 위한 새로운 트리를 생성하므로 비선형적인 관계나 변수 간 상호작용을 반복적으로 학습하며 보완할 수 있도록 하기 때문임. 또한     XGBoost는 트리 모델임에도 불구하고 L1, L2 정규화 항을 포함함. 이를 통해 모델의 복잡도를 수학적으로 제한하여 과적합을 억제하는 데 탁월함.

- **Stress Level을 1~5점으로 예측하는 것에 있어서 이는 정량, 정성 데이터가 혼합된 변수들이 예측하는 심리적 지표이며 변수 간 상호작용이 존재할 수 있고 비선형 분포를 따르기 때문에 개별 트리가 독립적으로 학습되는 Random Forest보다 이전 모델의 오차를 학습하며 변수 간 비선형 결합을 반복적으로 보완하는 XGBoost를 이용하는 것이 더 적합하기 때문에, XBGoost가 약간이나마 더 높은 정확도를 보인 것으로 예상됨.**

### 결과 및 고찰

- 본 팀은 직장인 라이프스타일 기반 스트레스 지수 예측 주제에 대해, 최초 RandomForest 알고리즘으로 예측을 수행한 결과였던 20.83% 의 정확도에서 알고리즘, 데이터 전처리, 피처 엔지니어링의 관점으로 다양한 시도를 하여 정확도를 25.5%로 향상시키는 성과를 보였음.
  
- train.csv에 포함된 요인들 만으로는 스트레스 수치를 정량적으로 예측하기 어려우며, 모델의 예측력을 높이기 위해서는 정성적 설문 지표와 같은 추가적인 요인이 필요할 것으로 보임.
  
- 비록 모델의 예측 정확도가 25.5% 였음에도 불구하고, 수면 습관과 평균 근무 시간은 직장인의 스트레스에 유의미한 영향을 주는 것으로 판단됨.

## IX. VIDEO
-





## X. 팀원 기여도
-

## XI. 참고 자료
- [데이터 출처 링크]
- [참고 논문/자료]
