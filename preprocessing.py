import pandas as pd

# Read the dataset
df = pd.read_csv("biodieselyield.csv")

# Preview the first few rows of the dataset
print("Initial Data Preview:")
print(df.head())

# --- Data Preprocessing Steps ---

# 1. Remove duplicate rows, if any
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# For numerical columns: fill missing values with the column mean
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# For categorical columns: fill missing values with the most frequent value (mode)
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 3. Encode categorical variables (optional, using one-hot encoding)
df = pd.get_dummies(df, drop_first=True)

# 4. Save the preprocessed dataset to a new CSV file
df.to_csv("biodieselyield_preprocessed.csv", index=False)

print("Preprocessing completed. Preprocessed dataset saved as 'biodieselyield_preprocessed.csv'.")