# Linear Regression Template with Preprocessing
# ---------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("your_dataset.csv")
print("Dataset Head:\n", df.head(), "\n")

# -----------------------------
# 2. Check missing values
# -----------------------------
print("Missing Values:\n", df.isnull().sum(), "\n")

# Drop rows with missing values (simple handling)
df = df.dropna()

# -----------------------------
# 3. Encode categorical columns
# -----------------------------
# Automatically detect object-type columns and encode them
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# -----------------------------
# 4. Define Features (X) and Target (y)
# -----------------------------
# Replace 'target_column' with the column you want to predict
target_column = 'Price'  # <-- change this in exam
X = df.drop(target_column, axis=1)
y = df[target_column]

# -----------------------------
# 5. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6. Train Linear Regression Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 7. Predict on Test Set
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 8. Show Results
# -----------------------------
print("Test Data:\n", X_test)
print("\nActual Values:\n", y_test.values)
print("\nPredicted Values:\n", y_pred)

# -----------------------------
# 9. Predict for New Data (optional)
# -----------------------------
# Example: replace with actual new input values
# new_data = pd.DataFrame({'Feature1':[value1], 'Feature2':[value2]})
# predicted = model.predict(new_data)
# print("Predicted Values for new data:\n", predicted)
