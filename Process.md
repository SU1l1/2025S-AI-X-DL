# 진행 중

---

## 👤 이름: 이수호

### 🔧 공통 실험 설정

- 사용한 입력 변수 (범주형 + 수치형):
`Work_Life_Balance, Lives_With_Family, Work_From, Working_State, Avg_Working_Hours_Per_Day, Manager_Support, Sleeping_Habit, Job_Satisfaction, Work_Pressure, Social_Person, Exercise_Habit`
- 대상 레이블: `Stress_Level (1~5)`
- 데이터 분할: `train_test_split(test_size=0.2, stratify=y, random_state=42)`
- 전처리: 다양한 방법 시도 (원-핫 인코딩, 레이블 인코딩, 스케일링 등)

---

### 🧪 실험한 전처리 기법 및 특징 요약

| 접근 방법 | 주요 특징 요약 |
| :-- | :-- |
| 기본 랜덤포레스트 | 원-핫 인코딩 + StandardScaler + class_weight='balanced' |
| 클래스 불균형 해결 | SMOTE + 부트스트래핑 + 클래스 가중치 조정 |
| 고급 전처리 기법 | 이상치 처리(IQR) + 빈도 기반 인코딩 + 상호정보량 특성 선택 |
| 최소 전처리 접근 | 스케일링 제거 + 간단한 레이블 인코딩 + 하이퍼파라미터 최적화 |
| 앙상블 모델 | 3개 모델 조합 + 소프트 투팅 + 교차 검증 |
| 극단적 단순화 | 절대 최소 전처리 + 기본 RandomForest |


---

### 📊 전처리 방법별 결과

### 🔹 기본 랜덤포레스트

**Accuracy:** `0.21`
**주요 기법:**

- 원-핫 인코딩 (Work_From, Working_State)
- Yes/No → 1/0 변환
- StandardScaler 적용
- class_weight='balanced'

**특징:** 초기 베이스라인으로 가장 안정적인 성능

---

### 🔄 클래스 불균형 해결

**Accuracy:** `0.19`
**주요 기법:**

- SMOTE 적용으로 클래스 균형 맞춤
- 부트스트래핑으로 데이터 증강
- 클래스 가중치 수동 조정

**특징:** 복잡한 샘플링 기법이 오히려 성능 저하 유발

---

### 🔬 고급 전처리 기법

**Accuracy:** `0.21`
**주요 기법:**

- IQR 방법으로 이상치 처리
- 빈도 기반 + 레이블 인코딩
- 상호정보량 기반 특성 선택
- ADASYN, SMOTEENN 등 고급 샘플링

**특징:** 복잡한 전처리로 기본 성능 수준 복귀

---

### 🎯 최소 전처리 접근

**Accuracy:** `0.21`
**주요 기법:**

- 스케일링 완전 제거
- 간단한 레이블 인코딩만 사용
- 하이퍼파라미터 그리드 서치
- 복잡한 샘플링 기법 제거

**특징:** 단순화를 통한 안정적 성능 유지

---

### 🎭 앙상블 모델

**Accuracy:** `0.18`
**주요 기법:**

- RandomForest 2개 + ExtraTrees 1개
- 소프트 투팅 앙상블
- 5-fold 교차 검증
- 순서 기반 인코딩

**특징:** 과도한 복잡성으로 인한 최악의 성능

---

### 🔥 극단적 단순화

**Accuracy:** `0.20`
**주요 기법:**

- 절대 최소한의 전처리
- 기본 RandomForestClassifier 설정
- class_weight 옵션만 조정
- 복잡한 기법 모두 제거

**특징:** 단순함의 힘, 하지만 여전히 21% 미달

---

### 📈 성능 변화 패턴

```
21% → 19% → 21% → 21% → 18% → 20%
```


### 🎯 핵심 발견사항

**✅ 효과적이었던 기법:**

- 최소한의 전처리 (스케일링 제거)
- 간단한 레이블 인코딩
- class_weight='balanced' 옵션
- 기본 하이퍼파라미터 사용

**❌ 역효과를 낸 기법:**

- SMOTE/ADASYN 등 복잡한 샘플링
- 과도한 앙상블 기법
- StandardScaler (랜덤포레스트에 불필요)
- 이상치 처리 및 특성 선택

**🔍 결론:**

- **21%가 현실적 성능 상한선**
- 랜덤포레스트는 단순한 전처리가 최적
- 복잡한 기법일수록 성능 저하
- 데이터 자체의 예측 가능성 한계 존재

<div style="text-align: center">⁂</div>
---

## 👤 이름: 박승우

### 🔧 공통 실험 설정

- 사용한 입력 변수 (수치형):  
  `Avg_Working_Hours_Per_Day, Manager_Support, Sleeping_Habit, Job_Satisfaction, Work_Pressure, Social_Person, Exercise_Habit`
- 대상 레이블: `Stress_Level (1~5 → 0~4)`
- 데이터 분할: `train_test_split(test_size=0.2, stratify=y, random_state=42)`
- 스케일링: `StandardScaler` (필요한 모델에만 적용)

---

### 🧪 실험한 모델 및 특징 요약

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

### 📊 모델별 결과

### 🔹 Logistic Regression  
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

### 🌲 Random Forest  
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

### 🐱 CatBoost  
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

### 🚀 XGBoost  
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

### 🧠 MLPClassifier  
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

### 🌀 SVM  
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

### 🔬 LDA  
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

## 👤 이름: 손영훈

## 피처 조합 기반 학습 실험

## 📊 2개씩 피처 조합 목록 및 가설

---

### 📌 업무환경 관련

- **Avg_Working_Hours_Per_Day + Work_Pressure**  
  → *“근무 시간이 길고 업무 강도도 높을 때 스트레스는 더 커질 수 있다”*

- **Work_From + Work_Life_Balance**  
  → *“재택근무와 워라밸이 서로 어떤 영향을 미치는가?”*

- **Work_From + Lives_With_Family**  
  → *“재택근무 시 가족과 함께 사는가에 따라 스트레스에 미치는 영향이 다를 수 있음”*

---

### 📌 생활습관 관련

- **Sleeping_Habit + Exercise_Habit**  
  → *“수면 + 운동 습관이 좋은 경우 스트레스가 낮을 수 있음”*

- **Sleeping_Habit + Work_Pressure**  
  → *“업무 스트레스가 수면에 영향을 미치고, 반대로도 영향 가능”*

- **Exercise_Habit + Work_Life_Balance**  
  → *“운동을 한다는 건 워라밸이 잘 유지되고 있다는 신호일 수 있음”*

---

### 📌 심리/지원 관련

- **Manager_Support + Job_Satisfaction**  
  → *“관리자 지원이 만족도에 영향을 미치고, 결국 스트레스를 낮추는 방향으로 작용할 수 있음”*

- **Job_Satisfaction + Work_Pressure**  
  → *“스트레스가 높을수록 직무 만족도가 낮을 수 있다”*

---

### 📌 성격/주거 관련

- **Social_Person + Lives_With_Family**  
  → *“사교성이 높고 가족과 함께 사는 사람이 스트레스를 덜 받을 수도 있음”*

- **Social_Person + Work_From**  
  → *“사교적인 사람이 재택근무일 경우 외로움을 더 많이 느낄 수 있다 → 스트레스 증가 가능성”*

---

### 📌 지역 기반

- **Working_State + Work_From**  
  → *“지역별 재택/사무실 출근 비율이 다르므로, 이 조합으로 지역별 스트레스 차이 파악 가능”*

- **Working_State + Stress_Level** *(검증용)*  
  → *“지도 기반 스트레스 분포 등도 나중에 분석할 수 있음”*


다음과 같이 연관된 피처 쌍들을 기반으로 학습을 진행하였다.

### 🔁 학습 흐름

1. 각 피처 쌍을 **One-Hot Encoding + Scaling** 으로 전처리  
2. **Random Forest** 모델을 사용하여 학습 수행  
3. **Validation Accuracy 및 Classification Report** 기반 성능 비교  
4. **유의미한 조합 중심으로 확장**  
   - 예: 3개 피처 조합, 피처 간 상호작용 항 추가 등

### Avg_Working_Hours_Per_Day + Work_Pressure 로 학습한 결과:

✅ **결과 요약**

| 항목                       | 값                                                             |
|--------------------------|----------------------------------------------------------------|
| **Validation Accuracy**  | 0.2017 (≈ 랜덤 추정보다 약간 높음)                              |
| **Best 클래스 (Recall 기준)** | 클래스 2 (f1-score ≈ 0.2387)                                   |
| **Worst 클래스**            | 클래스 1 (f1-score ≈ 0.1393)                                   |
| **분포 및 예측**              | 전체적으로 균형 잡힌 precision/recall 분포이나 성능은 낮은 편 |

### Work_From + Work_Life_Balance 학습 결과

✅ **결과 요약**

| 항목                   | 값                                                              |
|----------------------|-----------------------------------------------------------------|
| **Validation Accuracy** | 0.2050                                                         |
| **가장 높은 Recall**     | 클래스 3 (≈ 0.48)                                               |
| **가장 낮은 성능**       | 클래스 2 – 예측 불가 (f1 = 0)                                   |
| **경고**                | ⚠️ 클래스 2는 예측 자체가 되지 않음 → Precision / Recall = 0.0 → 모델이 해당 클래스를 한 번도 선택하지 않음 |

### Sleeping_Habit + Exercise_Habit 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                               |
|-------------------------|------------------------------------------------------------------|
| **Validation Accuracy**  | 0.2083                                                           |
| **전체 평균 f1-score (macro)** | 0.2067                                                        |
| **예측이 가장 잘 된 클래스**   | 클래스 0 (f1 ≈ 0.2264), 클래스 2 (f1 ≈ 0.2128)                   |
| **불균형 현상**               | 없음 – 모든 클래스에 대해 일정한 예측 시도 및 결과 도출           |

### Manager_Support + Job_Satisfaction 학습 결과

✅ **결과 요약**

| 항목                      | 값                                           |
|-------------------------|----------------------------------------------|
| **Validation Accuracy**  | 0.1900                                       |
| **평균 f1-score (macro)** | 0.1852                                       |
| **가장 높은 f1-score**     | 클래스 0, 클래스 4                           |
| **예측 쏠림**               | 없음 (모든 클래스에 대해 균등하게 예측 시도) |

### Job_Satisfaction + Work_Pressure 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                   |
|-------------------------|------------------------------------------------------|
| **Validation Accuracy**  | 0.1950                                               |
| **평균 f1-score**     | 0.1843                                               |
| **가장 잘 예측된 클래스**   | 클래스 4 (f1 ≈ 0.267)                                 |
| **예측 어려운 클래스**     | 클래스 1 (f1 ≈ 0.111)                                 |
| **정확도 / 분포**           | 보통 수준 – 일부 클래스에서 낮은 recall 발생            |

### Social_Person + Lives_With_Family 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                         |
|-------------------------|------------------------------------------------------------|
| **Validation Accuracy**  | 0.1700                                                     |
| **macro F1-score**       | 0.1627                                                     |
| **가장 잘 예측된 클래스**   | 클래스 4 (f1 ≈ 0.208)                                       |
| **가장 낮은 성능 클래스**   | 클래스 3 (f1 ≈ 0.089)                                       |
| **전체 예측 분포**           | 불균형하며 전반적으로 성능 낮음                            |

## 📊 전체 조합 성능 비교 (요약 테이블)

| 조합                                | Accuracy | macro F1 | 특징                        |
|-----------------------------------|----------|----------|---------------------------|
| Avg_Working_Hours + Work_Pressure | 0.2017   | 0.2018   | 무난                      |
| Work_From + Work_Life_Balance      | 0.2050   | 0.1729   | 클래스 2 예측 실패          |
| Sleeping_Habit + Exercise_Habit    | 0.2083   | 0.2067   | 가장 균형 잡힘 👍            |
| Manager_Support + Job_Satisfaction | 0.1900   | 0.1852   | 고르게 예측, 성능 낮음      |
| Job_Satisfaction + Work_Pressure   | 0.1950   | 0.1843   | 클래스 4 예측 괜찮음        |
| Social_Person + Lives_With_Family  | 0.1700   | 0.1627   | 정서적 변수만으로는 한계    |


**이후 Avg_Working_Hours_Per_Day를 바탕으로 진행**

### Avg_Working_Hours_Per_Day + Job_Satisfaction 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                      |
|-------------------------|---------------------------------------------------------|
| **Validation Accuracy**  | 0.2067                                                  |
| **Macro F1-score**       | 0.2062                                                  |
| **Weighted F1-score**    | 0.2062                                                  |
| **Best 클래스 (f1)**       | 클래스 2 (f1 ≈ 0.2326)                                   |
| **모든 클래스 예측됨**      | ✅ 예 — 클래스 불균형 없이 고르게 예측됨                  |

### Avg_Working_Hours_Per_Day + Work_Life_Balance 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                               |
|-------------------------|------------------------------------------------------------------|
| **Validation Accuracy**  | 0.2150 ✅ (현재까지 최고)                                          |
| **Macro F1-score**       | 0.2133                                                           |
| **Precision/Recall 분포** | 매우 균형 잡힘                                                    |
| **가장 높은 F1-score**     | 클래스 0, 1, 2 (모두 f1 ≈ 0.22–0.25 사이)                         |
| **가장 낮은 성능 클래스**   | 클래스 3 (f1 ≈ 0.1791) — 심각하지 않을 정도의 낮은 성능               |

### Avg_Working_Hours_Per_Day + Work_From 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                             |
|-------------------------|----------------------------------------------------------------|
| **Validation Accuracy**  | 0.2033                                                         |
| **Macro F1-score**       | 0.1997                                                         |
| **가장 잘 예측된 클래스**   | 클래스 0 (f1 ≈ 0.2418), 클래스 3 (f1 ≈ 0.2259)                   |
| **예측이 가장 어려운 클래스** | 클래스 2 (f1 ≈ 0.1262)                                          |



### Avg_Working_Hours_Per_Day + Work_Life_Balance + Job_Satisfaction 학습 결과

✅ **결과 요약**

| 항목                      | 값                                                              |
|--------------------------|-----------------------------------------------------------------|
| **Validation Accuracy**   | 0.2117                                                          |
| **Macro F1-score**        | 0.2103                                                          |
| **Best 클래스 (f1)**       | 클래스 0 (0.2353), 클래스 4 (0.2151)                              |
| **모든 클래스 예측됨**      | ✅ 쏠림 없음, 전체 예측 균형적                                      |

### Avg_Working_Hours_Per_Day + Sleeping_Habit 학습 결과

✅ **성능 요약**

| 지표                     | 값                      |
|------------------------|-------------------------|
| **Validation Accuracy** | ✅ 0.2333 ← ★ 최고       |
| **Macro F1-score**      | ✅ 0.2321 ← ★ 최고       |
| **Best 클래스 (f1)**     | 클래스 3 (0.2892)        |
| **모든 클래스 예측됨**    | ✅ 고르게 예측 (쏠림 없음) |

---

🔍 **분석 요점**

1. **업무량 + 수면습관의 조합은 매우 유의미**
   - 하루 근무 시간이 길고 수면이 부족할 경우 스트레스 상승 가능성
   - 수면이 잘 유지되면 긴 근무시간도 일정 부분 완충 가능
   - → *스트레스의 물리적 원인과 회복력 간의 관계를 잘 포착한 조합*

2. **클래스 3 (중간 스트레스 수준) 예측 우수**
   - f1-score ≈ 0.2892
   - → *스트레스가 가장 일반적으로 분포한 영역을 효과적으로 분류*

3. **기존 최고 조합 대비 성능 우수**
   - 아래는 상위 조합들 간의 비교 요약:

| 조합                                                     | Accuracy | Macro F1 | 특징                      |
|--------------------------------------------------------|----------|----------|---------------------------|
| ✅ Avg_Working_Hours + Sleeping_Habit                  | 0.2333   | 0.2321   | 🔥 현재 최고 성능 조합     |
| Avg_Working_Hours + Work_Life_Balance                  | 0.2150   | 0.2133   | 워라밸 조합               |
| Avg_Working_Hours + Work_Life_Balance + Job_Satisfaction | 0.2117   | 0.2103   | 정서/업무 복합 조합       |


---

## 👤 이름: 신동욱

- **실험 내용 요약**  
1. 2 or 3가지 feature를 이용하여 xgboost로 학습하여 정확도 확인
2. stress level을 1-5를 3가지 또는 2가지로 줄여 학습하여 정확도 확인

- **결과**
1.
| Feature 조합 | Accuracy |
|--------------|----------|
| Avg_Working_Hours_Per_Day, Sleeping_Habit | **0.255** |
| Avg_Working_Hours_Per_Day | 0.231 |
| Avg_Working_Hours_Per_Day, Social_Person | 0.211 |
| Avg_Working_Hours_Per_Day, Sleeping_Habit, Social_Person | 0.210 |
| Avg_Working_Hours_Per_Day, Exercise_Habit, Work_Pressure, Sleeping_Habit, Social_Person, Job_Satisfaction, Manager_Support | 0.185 |
| Avg_Working_Hours_Per_Day, Sleeping_Habit, Work_Pressure, Exercise_Habit, Manager_Support, Job_Satisfaction, Social_Person | 0.183 |

2.
| 재분류 기준 | 설명 | Accuracy |
|--------------|------|----------|
| 3단계 분류 | 0: Stress ≤ 2<br>1: Stress = 3<br>2: Stress ≥ 4 | 0.420 |
| 2단계 분류 | 0: Stress ≤ 3<br>1: Stress ≥ 4 | 0.568 |


- **코멘트 / 인사이트**  

---
