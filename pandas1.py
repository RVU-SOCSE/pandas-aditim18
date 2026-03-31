import pandas as pd


data = {
    "Name": ["Aditi", "Rohan", "Meera"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


df["Percentage"] = df["Marks"] * 1.0


print("\nDataFrame after adding new column:")
print(df)
