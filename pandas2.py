import pandas as pd


data = {
    "Product": ["Pen", "Book", "Pencil"],
    "Price": [10, 50, 5]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


df["Total Price"] = df["Price"] * 2

print("\nUpdated DataFrame:")
print(df)
