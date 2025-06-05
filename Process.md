# 진행 중

---

## 👤 이름: 이수호

- **실험 내용 요약**  
  - RandomForest 사용  
  - 범주형 포함한 전체 변수 조합 자동 탐색  
  - One-hot 인코딩 진행  

- **결과**  
  - 정확도: 0.2489  
  - 최적 조합: ['Avg_Working_Hours_Per_Day', 'Sleeping_Habit', 'Work_Life_Balance_Yes', 'Lives_With_Family_Yes']  

- **코멘트 / 인사이트**  
  - Lives_With_Family가 중요한 것처럼 보이지만, Yes 단일값으로 오해 소지 있음  
  - 다음엔 변수 단위 조합 방식으로 리팩터링 예정  

---

## 👤 이름: 박승우

- **실험 내용 요약**  
  - RandomForest 사용  
  - 범주형 포함한 전체 변수 조합 자동 탐색  
  - One-hot 인코딩 진행  

- **결과**  
  - 정확도: 0.2489  
  - 최적 조합: ['Avg_Working_Hours_Per_Day', 'Sleeping_Habit', 'Work_Life_Balance_Yes', 'Lives_With_Family_Yes']  

- **코멘트 / 인사이트**  
  - Lives_With_Family가 중요한 것처럼 보이지만, Yes 단일값으로 오해 소지 있음  
  - 다음엔 변수 단위 조합 방식으로 리팩터링 예정  

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

---

## 👤 이름: 신동욱

- **실험 내용 요약**  
  - RandomForest 사용  
  - 범주형 포함한 전체 변수 조합 자동 탐색  
  - One-hot 인코딩 진행  

- **결과**  
  - 정확도: 0.2489  
  - 최적 조합: ['Avg_Working_Hours_Per_Day', 'Sleeping_Habit', 'Work_Life_Balance_Yes', 'Lives_With_Family_Yes']  

- **코멘트 / 인사이트**  
  - Lives_With_Family가 중요한 것처럼 보이지만, Yes 단일값으로 오해 소지 있음  
  - 다음엔 변수 단위 조합 방식으로 리팩터링 예정  

---
