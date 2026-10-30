from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = load_breast_cancer()

# Separate features and target
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Features shape:", X.shape)
print("Target shape:", y.shape)
print("Target names:", data.target_names)

print("\nFirst five rows:")
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("\nTraining set shape:", X_train.shape)
print("Test set shape:", X_test.shape)
print("Training set target shape:", y_train.shape)
print("Test set target shape:", y_test.shape)

model = make_pipeline(
  StandardScaler(),
  LogisticRegression(max_iter=1000, random_state=42)
)

# Learn from the training data
model.fit(X_train, y_train)

print("Model trained successfully!")

predictions = model.predict(X_test)

print("Actual labels:    ", y_test[10:20])
print("Predicted labels: ", predictions[10:20])

probabilities = model.predict_proba(X_test)
print("Predicted probabilities for the first 10 test samples:")
print(probabilities[:10])