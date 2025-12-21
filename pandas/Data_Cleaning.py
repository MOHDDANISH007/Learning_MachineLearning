import pandas as pd
import numpy as np
from datetime import datetime, date

# =============================================================================
# PANDAS DATA CLEANING TUTORIAL - STEP BY STEP
# =============================================================================

# Create sample employee dataset with common data problems
# This data has missing values, duplicates, and inconsistent formatting
employee_data = {
    'Name': [
        'John Smith', 'jane doe', 'MIKE JOHNSON', 'sarah wilson', 'David Brown',
        'Lisa Garcia', 'robert taylor', 'EMMA DAVIS', 'james miller', 'Maria Rodriguez',
        '', 'Chris Anderson', 'jessica white', 'DANIEL THOMAS', 'Amanda Clark',
        'Michael Lee', 'jennifer hall', 'KEVIN WRIGHT', 'laura green', 'Steven Adams',
        'John Smith'  # This is a duplicate entry
    ],
    'Age': [
        28, 35, 42, 29, 38,
        31, 45, 27, 52, 33,
        np.nan, 41, 26, 39, 44,  # np.nan represents missing value
        36, 30, 48, 34, 37, 28
    ],
    'Salary': [
        50000, 65000, 80000, 55000, 70000,
        60000, 85000, 52000, 90000, 58000,
        75000, np.nan, 48000, 72000, 67000,  # np.nan represents missing value
        63000, 51000, 88000, 56000, 74000, 50000
    ],
    'Designation': [
        'Software Engineer', 'data analyst', 'PROJECT MANAGER', 'software engineer', 'Senior Developer',
        'Data Scientist', 'project manager', 'SOFTWARE ENGINEER', 'senior developer', 'Data Analyst',
        'Marketing Manager', 'Software Engineer', 'data scientist', 'PROJECT MANAGER', 'Marketing Manager',
        'Senior Developer', 'data analyst', 'SOFTWARE ENGINEER', 'Data Scientist', 'Project Manager', 'Software Engineer'
    ],
    'Date_of_Birth': [
        '1995-03-15', '1988-07-22', '1981-11-08', '1994-09-12', '1985-05-30',
        '1992-12-03', '1978-08-17', '1996-04-25', '1971-01-14', '1990-10-07',
        # Empty string = missing value
        '', '1982-06-19', '1997-02-28', '1984-09-05', '1979-12-11',
        '1987-03-22', '1993-11-16', '1975-07-04', '1989-08-29', '1986-05-13', '1995-03-15'
    ],
    'Department': [
        'IT', 'Analytics', 'Management', 'IT', 'IT',
        'Analytics', 'Management', 'IT', 'IT', 'Analytics',
        'Marketing', 'IT', 'Analytics', 'Management', 'Marketing',
        'IT', 'Analytics', 'IT', 'Analytics', 'Management', 'IT'
    ]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(employee_data)

print("=" * 60)
print("ORIGINAL DATASET (WITH PROBLEMS):")
print("=" * 60)
print(df)
print()

# =============================================================================
# STEP 1: HANDLE EMPTY STRINGS AND MISSING VALUES
# =============================================================================

# Convert empty strings ('') to NaN (Not a Number) for consistent handling
# This makes it easier to identify and work with missing data
df.replace('', np.nan, inplace=True)

print("=" * 60)
print("STEP 1: CHECKING FOR MISSING VALUES")
print("=" * 60)
# Check how many missing values are in each column
# .isna() finds missing values, .sum() counts them
print(f"Missing Values in each column:\n{df.isna().sum()}\n")

# Fill missing numeric values with the average (mean) of that column
# This is a common strategy for handling missing numbers
print("Filling missing Age and Salary with average values...")
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("✅ Missing numeric values replaced with average values.\n")
print("Dataset after filling numeric missing values:")
print(df)
print()


# =============================================================================
# STEP 2: HANDLE MISSING TEXT VALUES
# =============================================================================

print("=" * 60)
print("STEP 2: FILLING MISSING TEXT VALUES")
print("=" * 60)

# Fill missing names with the most common name (mode)
# .mode()[0] gets the most frequently occurring value
df['Name'].fillna(df['Name'].mode()[0], inplace=True)

print("✅ Missing values in 'Name' column filled with most common name.\n")
print("Dataset after filling missing names:")
print(df)
print()

# =============================================================================
# STEP 3: DATA FILTERING AND ANALYSIS
# =============================================================================

print("=" * 60)
print("STEP 3: FILTERING DATA FOR ANALYSIS")
print("=" * 60)

# Select specific columns for analysis
# This creates a subset with only Name, Age, and Salary columns
specificData = df[['Name', 'Age', 'Salary']]

# Use query to find employees meeting certain conditions
# Find employees who are either over 50 OR have salary less than 50000
print("Employees over 50 years old OR with salary less than $50,000:")
print(f"{specificData.query('Age > 50 or Salary < 50000')}\n")

# Remove any remaining rows that still have missing values
# .dropna() removes entire rows that contain any NaN values
clean_df = df.dropna()
print("Dataset after removing any remaining missing data:")
print(clean_df)
print()


# =============================================================================
# STEP 4: IDENTIFY AND REMOVE DUPLICATE ROWS
# =============================================================================

print("=" * 60)
print("STEP 4: HANDLING DUPLICATE ROWS")
print("=" * 60)

# Check for duplicate rows in the dataset
# .duplicated() returns True/False for each row (True = duplicate)
print("Checking for duplicate rows...")
print(f"Duplicate status for each row:\n{df.duplicated()}\n")

# Find the index positions of duplicate rows
print("Index positions of duplicate rows:")
print(f"{df[df.duplicated() == True].index}\n")

# Show the actual duplicate row data
print("The duplicate row data:")
print(f"{df[df.duplicated() == True].values}\n")

# Remove duplicate rows from the dataset
# .drop_duplicates() keeps the first occurrence and removes the rest
df.drop_duplicates(inplace=True)
print("✅ Duplicate rows have been removed.")
print("\nDataset after removing duplicates:")
print(f"{df}")
print()


# =============================================================================
# STEP 5: VERIFY DATA COMPLETENESS
# =============================================================================

print("=" * 60)
print("STEP 5: CHECKING DATA COMPLETENESS")
print("=" * 60)

# Check for non-missing values in each column
# .notna() returns True for non-missing values, .sum() counts them
print("Count of non-missing values in each column:")
print(f"{df.notna().sum()}\n")

# Fill any remaining missing Date of Birth values with the most common date
print("Filling missing Date of Birth values...")
df['Date_of_Birth'].fillna(df['Date_of_Birth'].mode()[0], inplace=True)

print("✅ Missing values in 'Date_of_Birth' column filled with most common date.\n")
print("Final dataset with all missing values handled:")
print(df)
print()

print("Final count of non-missing values:")
print(f"{df.notna().sum()}\n")


# =============================================================================
# STEP 6: ADDING NEW COLUMNS
# =============================================================================

print("=" * 60)
print("STEP 6: ADDING CALCULATED COLUMNS")
print("=" * 60)

# Method 1: Add column at the end (commented out)
# df["Bonus"] = df['Salary'] * 0.1

# Method 2: Insert column at a specific position
# .insert(position, column_name, values)
# Position 3 means it will be the 4th column (0-indexed)
print("Adding a Bonus column (10% of salary) at position 3...")
df.insert(3, "Bonus", df['Salary'] * 0.1)

print("✅ New 'Bonus' column added successfully!")
print("Dataset with new Bonus column:")
print(f"{df}")
print()


# =============================================================================
# STEP 7: UPDATING DATA VALUES
# =============================================================================

print("=" * 60)
print("STEP 7: UPDATING EXISTING DATA")
print("=" * 60)

# Update a single cell value
# Syntax: df.loc[row_index, "column_name"] = new_value
print("Updating the name in row 0...")
df.loc[0, "Name"] = "Mohammad Danish"

print("✅ Single row updated successfully!")
print("Dataset after updating one name:")
print(f"{df}")
print()

# Update multiple rows at once
# Update ages for rows 0 through 4 (first 5 employees)
print("Updating ages for first 5 employees to 24...")
df.loc[0:4, "Age"] = 24

print("✅ Multiple rows updated successfully!")
print("Dataset after updating multiple ages:")
print(f"{df}")
print()

# =============================================================================
# STEP 8: REMOVING COLUMNS AND ROWS
# =============================================================================

print("=" * 60)
print("STEP 8: REMOVING UNWANTED DATA")
print("=" * 60)

# Remove specific columns from the dataset
# axis=1 means we're dropping columns (axis=0 would be rows)
print("Removing 'Date_of_Birth' and 'Bonus' columns...")
df.drop(["Date_of_Birth", "Bonus"], axis=1, inplace=True)

print("✅ Columns deleted successfully!")
print("Dataset after removing columns:")
print(f"{df}")
print()

# Remove specific rows from the dataset
# Remove the first 4 rows (index 0 through 3)
# axis=0 means we're dropping rows
print("Removing first 4 rows from the dataset...")
df.drop(df.index[0:4], axis=0, inplace=True)

print("✅ Rows deleted successfully!")
print("Final cleaned dataset:")
print(f"{df}")
print()

print("=" * 60)
print("DATA CLEANING COMPLETE! 🎉")
print("=" * 60)
print("Summary of operations performed:")
print("✅ Handled missing values")
print("✅ Removed duplicate rows")
print("✅ Added calculated columns")
print("✅ Updated existing data")
print("✅ Removed unwanted columns and rows")
print("✅ Dataset is now clean and ready for analysis!")
