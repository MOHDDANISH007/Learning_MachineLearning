import pandas as pd

# 📥 1️⃣ Data Input / Output (Reading & Writing Files)

Sales_Data = pd.read_csv(
    r"C:\Users\mohdd\OneDrive\Documents\Desktop\Machine_Learning\pandas\sales_data.csv"
)

print(f"Sales Data: \n {Sales_Data}")


# 📤 2️⃣ Data Input / Output (Reading & Writing Files

dataFrame = pd.DataFrame({
    "Name": ["Mohammad", "Kashif", "Ali"],
    "Age": [20, 25, 30],
    "Gender": ["Male", "Male", "Male"]
})

# print(f"Data Frame: \n {dataFrame}")


# 🔍 2️⃣ Viewing & Understanding Data

# head => it will give you the head / top rows data...abs

print(f"Top 5 rows of Data: \n {Sales_Data.head(5)}")

# tail => it will give you the bottom rows data...abs

print(f"Bottom 5 rows of Data: \n {Sales_Data.tail(5)}")


# df.info() Get column types, null values, etc.

print(f"Data Information: \n {Sales_Data.info()}")


# df.shape Get number of rows & columns

print(f"Shape of Dataframe: {Sales_Data.shape}")
print(f"Columns of Dataframe: {Sales_Data.columns}")

# df.describe() Get summary stats (mean, std, etc.)

print(f"Data Description: \n {Sales_Data.describe()}")

# print(f"Total Quantity: \n {Sales_Data['Quantity'].sum()}")
# print(f"Total Quantity: \n {Sales_Data['Quantity'].mean()}")

# print(Sales_Data.notna().sum())


# print(f"Data is \n : {dataFrame}")
# print(f"Describe the data {dataFrame.describe()}")


# df.index Row index info
print(f"Index range: {Sales_Data.index}")

print(f"Number of rows: {len(Sales_Data.index)}")
print(f"Selecting rows from index 2 to 5: \n {Sales_Data[2:5]}")



print(f"Checking how many missing values are there\n {Sales_Data.isna().sum()}")

averageValueOfQuantity = Sales_Data["Quantity"].mean()
print(f"Average Quantity: {averageValueOfQuantity}")

Sales_Data["Quantity"].fillna(averageValueOfQuantity, inplace=True)
print(f"Data after filling missing values: \n {Sales_Data}")

Unit_Price_Average_Value = Sales_Data["Unit_Price"].mean()
Sales_Data["Unit_Price"].fillna(Unit_Price_Average_Value, inplace=True)
print(f"Data after filling missing values: \n {Sales_Data}")


Revenue_Average_Value = Sales_Data["Revenue"].mean();
Sales_Data["Revenue"].fillna(Revenue_Average_Value, inplace=True)
print(f"Data after filling missing values: \n {Sales_Data}")


Sales_Data["Salesperson"].fillna(Sales_Data["Salesperson"].mode()[0], inplace=True)
print(f"Data after filling missing values: \n {Sales_Data}")


# SalesPersonData_RepeatedMost = Sales_Data["Salesperson"].mode()
# print(f"Data after filling missing values: \n {SalesPersonData_RepeatedMost}")


print(f"Checking how many missing values are there\n {Sales_Data.isna().sum()}")

# Product_Most_Sold_Data_Name  = Sales_Data["Product"].mode()
# print(f"Data after filling missing values: \n {Product_Most_Sold_Data_Name}")

# Sales_Data["Product"].fillna(Sales_Data["Product"].mode()[0], inplace=True)


print(f"Data after filling missing values: \n {Sales_Data}")




print(f"Checking how many missing values are there\n {Sales_Data.isna().sum()}")


print(f"Removing the row from the dataframe: \n {Sales_Data.dropna(axis=0, inplace=True)}")

print(f"Data after removing missing values: \n {Sales_Data}")