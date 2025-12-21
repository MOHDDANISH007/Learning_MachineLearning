import pandas as pd


# 📥 1️⃣ Data Input / Output (Reading & Writing Files)

# reading the csv file

# getting the data into the dataframe format
df = pd.read_csv(
    r"C:\Users\mohdd\OneDrive\Documents\Desktop\Machine_Learning\pandas\sales_data.csv")
print(df)


# creating own dataframe

creatingData_frame = pd.DataFrame(
    {
        "Name": ["Mohammad", "Kashif", "Ali"],
        "Age": [20, 25, 30],
        "Gender": ["Male", "Male", "Male"]
    },

    {
        "Name": ["Hammad", "Kashif", "Ali"],
        "Age": [20, 25, 30],
        "Gender": ["Male", "Male", "Male"]
    }
)

print(f"Creating Data Frame: \n {creatingData_frame}")


# creating data with list

data = [
    ["Mohammad", 20, "Male"],
    ["Kashif", 25, "Male"],
    ["Ali", 30, "Male"]
]

creatingData_frame = pd.DataFrame(data, columns=["Name", "Age", "Gender"])
print(f"Creating Data Frame: \n {creatingData_frame}")


anotherData = {
    "Name": ["Mohammad", "Kashif", "Ali"],
    "Subjects": [["Math", "Science"], ["English", "History"], ["Physics", "Chemistry"]]
}


creatingData_frame = pd.DataFrame(anotherData)
print(f"Creating Data Frame: \n {creatingData_frame}")

# saving the file as a csv file

creatingData_frame.to_csv("creatingData_frame.csv", index=False)


# saving the file as a excel file

creatingData_frame.to_excel("creatingData_frame.xlsx")


# saving the file as a html file

creatingData_frame.to_html("creatingData_frame.html")


# saving the file as a json file

creatingData_frame.to_json("creatingData_frame.json")