#일단randomforest로 되어있는데 수정예정
# stress_predict_rf.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data(path):
    df = pd.read_csv(path)
    df['Stress_Level'] = df['Stress_Level'] - 1  # 레이블을 0~4로 맞춤
    return df

def preprocess(df):
    selected_feats = ['Avg_Working_Hours_Per_Day', 'Sleeping_Habit']
    target_col = 'Stress_Level'

    X = df[selected_feats].values
    y = df[target_col].values

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    return X_train_scaled, X_val_scaled, y_train, y_val

def train_and_evaluate(X_train, X_val, y_train, y_val):
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)

    acc = accuracy_score(y_val, y_pred)
    print(f"\n✅ Validation Accuracy: {acc:.4f}\n")
    print("📄 Classification Report:")
    print(classification_report(y_val, y_pred, digits=4))

def main():
    # 경로 수정: VS Code에서 데이터 경로가 현재 파일 기준 상대 경로일 수 있음
    csv_path = "train.csv"  # 예: 같은 폴더에 있을 경우
    df = load_data(csv_path)
    X_train, X_val, y_train, y_val = preprocess(df)
    train_and_evaluate(X_train, X_val, y_train, y_val)

if __name__ == "__main__":
    main()
