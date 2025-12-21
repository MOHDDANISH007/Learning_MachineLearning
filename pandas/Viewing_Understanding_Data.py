import pandas as pd

# Load data from CSV file into a DataFrame
df = pd.read_csv("sales_data.csv")

# =============================================================================
# BASIC DATA VIEWING METHODS
# =============================================================================

# 1. VIEW FIRST FEW ROWS
# df.head() shows the first 5 rows by default
# This helps you quickly see what your data looks like
print("=" * 50)
print("FIRST 5 ROWS OF DATA:")
print("=" * 50)
print(df.head(5))

print("\n" + "=" * 50)
print("LAST 5 ROWS OF DATA:")
print("=" * 50)
# 2. VIEW LAST FEW ROWS
# df.tail() shows the last 5 rows by default
# Useful to see the end of your dataset
print(df.tail(5))

print("\n" + "=" * 50)
print("DATASET INFORMATION:")
print("=" * 50)
# 3. GET DATASET OVERVIEW
# df.info() provides a comprehensive summary including:
# - Column names and their data types
# - Number of non-null (non-empty) values in each column
# - Memory usage of the dataset
# - Total number of rows and columns
print(df.info())

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY:")
print("=" * 50)
# 4. GET STATISTICAL SUMMARY
# df.describe() calculates statistics for numerical columns:


# Create sample data to demonstrate df.describe()
# This dictionary contains employee information with different data types
sample_data = {
    "Name": ['Ram', 'Shahid', 'Ali', 'Kashif', 'Ayesha', 'Zainab', 'Ammar', 'Danish', 'Iqra'],
    "Age": [20, 25, 30, 35, 40, 45, 50, 55, 60],
    "Gender": ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    "Salary": [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'Dallas', 'San Diego'],
    "Country": ['United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States'],
    "Education": ['Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor'],
    "Marital_Status": ['Single', 'Married', 'Single', 'Married', 'Single', 'Single', 'Single', 'Single', 'Single'],
    "Children": [0, 1, 0, 2, 0, 1, 0, 0, 0],
    "Company": ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ']
}

# Convert dictionary to DataFrame for demonstration
df_sample = pd.DataFrame(sample_data)

# df.describe() shows statistics like:
# - count: number of non-null values
# - mean: average value
# - std: standard deviation (how spread out the data is)
# - min/max: smallest and largest values
# - 25%, 50%, 75%: quartiles (data distribution)
print(df_sample.describe())

print("\n" + "=" * 50)
print("DATA TYPES OF EACH COLUMN:")
print("=" * 50)
# 5. CHECK DATA TYPES
# df.dtypes shows what type of data each column contains:
# - object: text/string data
# - int64: whole numbers
# - float64: decimal numbers
# - datetime64: dates and times
print(df.dtypes)

print("\n" + "=" * 50)
print("INDEX INFORMATION:")
print("=" * 50)
# 6. VIEW INDEX INFORMATION
# df.index shows the row labels/numbers
# By default, pandas uses numbers starting from 0
print(f"Index range: {df.index}")
print(f"Number of rows: {len(df.index)}")

print("\n" + "=" * 50)
print("RANDOM SAMPLE OF DATA:")
print("=" * 50)
# 7. VIEW RANDOM ROWS
# df.sample(n) picks n random rows from your dataset
# This is useful for getting a quick, unbiased look at your data
print(df.sample(5))
# 8. shape and columns
print(f"Shape of Dataframe: {df.shape}")
print(f"Columns of Dataframe: {df.columns}")
