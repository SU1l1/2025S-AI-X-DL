import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb

def load_data(path):
    df = pd.read_csv(path)
    df['Stress_Level'] = df['Stress_Level'] - 1  # 라벨을 0~4로 조정
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
    model = xgb.XGBClassifier(
        objective='multi:softmax',
        num_class=5,
        eval_metric='mlogloss',
        use_label_encoder=False,
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)

    acc = accuracy_score(y_val, y_pred)
    print(f"\n✅ Validation Accuracy: {acc:.4f}\n")
    print("📄 Classification Report:")
    print(classification_report(y_val, y_pred, digits=4))

def main():
    csv_path = "train.csv"  # 필요 시 경로 조정
    df = load_data(csv_path)
    X_train, X_val, y_train, y_val = preprocess(df)
    train_and_evaluate(X_train, X_val, y_train, y_val)

if __name__ == "__main__":
    main()
