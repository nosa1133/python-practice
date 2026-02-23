import pandas as pd

file_path = r"C:\Users\20128\Downloads\Book.xlsx"
data = pd.read_excel(file_path)


data.columns = data.columns.str.strip()


clean_data = data[data["name"].notna()]

print(clean_data)

print("Total salary:", clean_data["salary"].sum())
print("Average salary:", clean_data["salary"].mean())
print("Max salary:", clean_data["salary"].max())
print("Min salary:", clean_data["salary"].min())