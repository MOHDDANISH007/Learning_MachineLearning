import pandas as pd

# =============================================================================
# PANDAS DATA SELECTION AND FILTERING TUTORIAL
# =============================================================================

# Create sample student data for demonstration
# This dictionary contains information about students, their marks, cities, etc.
student_data = {
    'Name': [
        'Mohammad', 'Kashif', 'Ali', 'Hammad', 'Nina',
        'Aisha', 'Ravi', 'Sonia', 'David', 'Farhan',
        'Priya', 'Arjun', 'Sana', 'Rohit', 'Zara'
    ],
    'Marks': [
        85, 72, 90, 60, 95,
        78, 88, 67, 82, 91,
        76, 84, 69, 93, 87
    ],
    'City': [
        'Delhi', 'Lucknow', 'Delhi', 'Mumbai', 'Delhi',
        'Pune', 'Delhi', 'Chennai', 'Bangalore', 'Delhi',
        'Hyderabad', 'Kolkata', 'Jaipur', 'Delhi', 'Surat'
    ],
    'Subject': [
        'Math', 'Science', 'Math', 'English', 'Science',
        'English', 'Math', 'Science', 'English', 'Science',
        'Math', 'Science', 'English', 'Math', 'Science'
    ],
    'Gender': [
        'Male', 'Male', 'Male', 'Male', 'Female',
        'Female', 'Male', 'Female', 'Male', 'Male',
        'Female', 'Male', 'Female', 'Male', 'Female'
    ]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(student_data)

print("=" * 60)
print("COMPLETE DATASET:")
print("=" * 60)
print(f"{df}\n")

# =============================================================================
# 1. COLUMN SELECTION
# =============================================================================

print("=" * 60)
print("1. SELECTING COLUMNS:")
print("=" * 60)

# Select a single column using column name in square brackets
# This returns a pandas Series (1-dimensional data)
print("Single column selection - 'Name':")
print(f"{df['Name']}\n")

# Select multiple columns using a list of column names
# This returns a pandas DataFrame (2-dimensional data)
print("Multiple column selection - 'Name' and 'Marks':")
print(f"{df[['Name', 'Marks']]}\n")

# =============================================================================
# 2. ROW SELECTION USING .loc (LABEL-BASED)
# =============================================================================

print("=" * 60)
print("2. ROW SELECTION USING .loc:")
print("=" * 60)

# .loc uses row labels/index to select data
# Select a single row by its index (row 2 = 3rd student)
print("Single row selection - Row index 2 (3rd student):")
print(f"{df.loc[2]}\n")

# Select multiple specific rows using a list of indices
print("Multiple specific rows - Rows 2 and 5:")
print(f"{df.loc[[2, 5]]}\n")

# Select a range of rows using slice notation (inclusive of both ends)
print("Row range selection - Rows 2 to 5:")
print(f"{df.loc[2:5]}\n")

# Select specific rows AND specific columns
print("Specific rows (2-5) and specific columns (Name, Marks, City):")
print(f"{df.loc[2:5, ['Name', 'Marks', 'City']]}\n")

# =============================================================================
# 3. ROW SELECTION USING .iloc (POSITION-BASED)
# =============================================================================

print("=" * 60)
print("3. ROW SELECTION USING .iloc:")
print("=" * 60)

# .iloc uses integer positions (like array indices) to select data
# Select rows 0-2 (first 3 rows) and columns 0-1 (first 2 columns)
print("Position-based selection - First 3 rows, first 2 columns:")
print(f"{df.iloc[0:3, 0:2]}\n")

# Select all rows but only first 3 columns
print("All rows, first 3 columns:")
print(f"{df.iloc[:, 0:3]}\n")

# =============================================================================
# 4. FILTERING DATA USING .query() METHOD
# =============================================================================

print("=" * 60)
print("4. FILTERING WITH .query():")
print("=" * 60)

# .query() allows you to filter data using string expressions
# Find students with marks greater than 80
print("Students with marks > 80:")
print(f"{df.query('Marks > 80')}\n")

# Multiple conditions using 'and' operator
print("Students from Delhi with marks > 80:")
print(f"{df.query('Marks > 80 and City == \"Delhi\"')}\n")

# Multiple conditions with different operators
print("Students from Delhi studying Math with marks > 80:")
print(f"{df.query('Marks > 80 and City == \"Delhi\" and Subject == \"Math\"')}\n")


# =============================================================================
# 5. BOOLEAN FILTERING (CONDITION-BASED FILTERING)
# =============================================================================

print("=" * 60)
print("5. BOOLEAN FILTERING:")
print("=" * 60)

# Create a subset of data for demonstration
sample_data = df.iloc[0:5, :]  # First 5 rows, all columns
print("Sample data for analysis:")
print(f"{sample_data}\n")

# Calculate average marks from sample data
average_marks = sample_data['Marks'].sum() / len(sample_data)
print(f"Average marks in sample: {average_marks:.2f}\n")

# Find maximum marks in sample data
max_marks = sample_data['Marks'].max()
print(f"Highest marks in sample: {max_marks}\n")

# =============================================================================
# 6. SINGLE CONDITION FILTERING
# =============================================================================

print("=" * 60)
print("6. SINGLE CONDITION FILTERING:")
print("=" * 60)

# Find student(s) with highest marks in sample data
print("Student(s) with highest marks in sample:")
print(f"{sample_data[sample_data['Marks'] == sample_data['Marks'].max()]}\n")

# Find students with marks less than 80
print("Students with marks < 80:")
print(f"{df[df['Marks'] < 80]}\n")

# Find students with marks greater than 75
print("Students with marks > 75:")
print(f"{df[df['Marks'] > 75]}\n")

# Find students from Delhi
print("Students from Delhi:")
print(f"{df[df['City'] == 'Delhi']}\n")

# =============================================================================
# 7. MULTIPLE CONDITION FILTERING
# =============================================================================

print("=" * 60)
print("7. MULTIPLE CONDITION FILTERING:")
print("=" * 60)

# Method 1: Using .query() - cleaner syntax
print("Method 1 - Using .query() for multiple conditions:")
print("Students from Delhi with marks > 80:")
print(f"{df.query('City == \"Delhi\" and Marks > 80')}\n")

# Method 2: Using boolean operators (&, |, ~)
print("Method 2 - Using boolean operators:")
print("Students from Delhi with marks > 80:")
print(f"{df[(df['City'] == 'Delhi') & (df['Marks'] > 80)]}\n")

# Find female students with marks > 85
print("Female students with marks > 85:")
print(f"{df[(df['Gender'] == 'Female') & (df['Marks'] > 85)]}\n")

# Find students from Delhi OR Mumbai with marks > 80
print("Students from Delhi OR Mumbai with marks > 80:")
print(f"{df[((df['City'] == 'Delhi') | (df['City'] == 'Mumbai')) & (df['Marks'] > 80)]}\n")
