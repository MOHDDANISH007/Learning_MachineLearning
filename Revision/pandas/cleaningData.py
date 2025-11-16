# import pandas as pd
# import numpy as np

# # Create a DataFrame with missing values and mixed data types
# data = {
#     'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve', 'Frank', 'Grace', 'Henry', None, 'Jack'],
#     'Age': [25, 30, np.nan, 28, 32, 45, 29, np.nan, 35, 27],
#     'Department': ['IT', 'HR', 'Finance', 'IT', None, 'Marketing', 'IT', 'HR', 'Finance', None],
#     'Salary': [50000, 60000, 75000, None, 65000, 80000, 55000, 62000, np.nan, 58000],
#     'Experience': [2, 5, np.nan, 3, 6, 12, 4, 7, 10, 3],
#     'Performance_Rating': [4.2, 3.8, 4.5, 3.9, np.nan, 4.8, 4.1, 3.7, 4.3, 3.5],
#     'Join_Date': pd.to_datetime(['2020-01-15', '2018-03-20', '2017-06-10', None, 
#                                 '2019-11-05', '2010-08-15', '2021-02-28', '2017-12-01', 
#                                 '2015-04-20', '2022-01-10']),
#     'Projects_Completed': [5, 8, 12, 6, None, 20, 7, 9, 15, 4],
#     'Training_Hours': [40, 35, 50, None, 45, 60, 30, np.nan, 55, 25]
# }

# df = pd.DataFrame(data)
# print("DataFrame with Missing Values:")
# print(df)
# print("\n" + "="*80)

# # df.rename(columns={'old':'new'})

# df.rename(columns={'Projects_Completed': 'Completed_Projects'}, inplace=True)

# print("DataFrame after Renaming a Column:")
# print(df)
# print("\n" + "="*80)


# df["Completed_Projects"].fillna(df["Completed_Projects"].mean(), inplace=True)
# print("DataFrame after Filling Missing Values:")
# print(df)
# print("\n" + "="*80)



# print("DataFrame after Filling Missing Values:")
# print(df)
# print("\n" + "="*80)

# # Sorting the values by a specific column
# df.sort_values(by='Completed_Projects', inplace=True)
# print("DataFrame after Sorting by a Specific Column:")
# print(df)
# print("\n" + "="*80)




# --------------------------Data Selection & Filtering---------------------------

import pandas as pd
import numpy as np


data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve', 'Frank', 'Grace', 'Henry', None, 'Jack'],
    'Age': [25, 30, np.nan, 28, 32, 45, 29, np.nan, 35, 27],
    'Department': ['IT', 'HR', 'Finance', 'IT', None, 'Marketing', 'IT', 'HR', 'Finance', None],
    'Salary': [50000, 60000, 75000, None, 65000, 80000, 55000, 62000, np.nan, 58000],
    'Experience': [2, 5, np.nan, 3, 6, 12, 4, 7, 10, 3],
    'Performance_Rating': [4.2, 3.8, 4.5, 3.9, np.nan, 4.8, 4.1, 3.7, 4.3, 3.5],
    'Join_Date': pd.to_datetime(['2020-01-15', '2018-03-20', '2017-06-10', None, 
                                '2019-11-05', '2010-08-15', '2021-02-28', '2017-12-01', 
                                '2015-04-20', '2022-01-10']),
    'Projects_Completed': [5, 8, 12, 6, None, 20, 7, 9, 15, 4],
    'Training_Hours': [40, 35, 50, None, 45, 60, 30, np.nan, 55, 25]
}

pdData = pd.DataFrame(data)

print(f"Original DataFrame: \n {pdData}")




print(f"Department looks cool: \n {pdData['Department']}")

print("More then one column looks cool: \n")
print(pdData[['Department', 'Salary']])

print(f"Age looks cool: \n {pdData['Age']}")


# location labels

print(f"Age looks cool: \n {pdData.loc[0:5, 'Age']}")

print(f"Age looks cool: \n {pdData.loc[:, ['Age', 'Salary']]}")

# print(f"Age looks cool: \n {pdData.loc[2, 'Age']}")


# df[df['Marks'] > 80]


print(f"I want to see the data whose salary is greater then: \n {pdData[pdData['Salary'] >= 75000]}")