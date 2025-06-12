# stress_predict_rf.py

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. 데이터 불러오기 (현재 디렉토리에 있는 파일 사용)
df = pd.read_csv("train.csv")

# 2. 사용할 feature와 target 선택
X = df[['Avg_Working_Hours_Per_Day', 'Sleeping_Habit']]
y = df['Stress_Level']

# 3. target 라벨 인코딩 (1~5 → 0~4)
y_encoded = y - 1

# 4. 학습/검증 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# 5. 모델 정의 및 학습
model = xgb.XGBClassifier(
    objective='multi:softmax',
    num_class=5,
    eval_metric='mlogloss',
    use_label_encoder=False
)
model.fit(X_train, y_train)

# 6. 예측 및 평가
y_pred_encoded = model.predict(X_test)
y_pred = y_pred_encoded + 1  # 다시 1~5로 복원
y_test_orig = y_test + 1

print("✅ Accuracy:", accuracy_score(y_test_orig, y_pred))
print("\n📋 Classification Report:")
print(classification_report(y_test_orig, y_pred))

# 7. Feature Importance 시각화
xgb.plot_importance(model, height=0.5)
plt.title("XGBoost Feature Importance (2 features only)")
plt.tight_layout()
plt.show()
