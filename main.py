import pandas as pd
# Read CSV file
df = pd.read_csv("sample.csv")
# Save original statistics
original_rows = len(df)
duplicate_count = df.duplicated().sum()
missing_count = df.isnull().sum().sum()
# Clean column names
df.columns = df.columns.str.strip().str.lower()
# Remove duplicate rows
df = df.drop_duplicates()
# Clean text columns
text_columns = df.select_dtypes(include="object").columns
for column in text_columns:
    df[column] = df[column].fillna("Unknown")
    df[column] = df[column].str.strip()
# Fill missing numeric values with column median
numeric_columns = df.select_dtypes(include="number").columns
for column in numeric_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].median())
# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)
# Final statistics
final_rows = len(df)
removed_rows = original_rows - final_rows
# Create report
report = f"""
CSV CLEANING REPORT
-------------------
Original rows: {original_rows}
Final rows: {final_rows}
Duplicate rows removed: {removed_rows}
Missing values found: {missing_count}
Output file: cleaned_data.csv
"""
print(report)
with open("cleaning_report.txt", "w") as file:
    file.write(report)
print("Cleaning completed successfully.")