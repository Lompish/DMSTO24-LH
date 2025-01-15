import pandas as pd 
import os


sales_data = pd.read_csv("DMSTO24-DS\DS9\ovningar\sales_2025.csv")
customer_data = pd.read_csv("DMSTO24-DS\DS9\ovningar\customers.csv")

merged_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")

print(merged_data)

sales_data["Försäljning"] = sales_data["Price"] * sales_data["Quantity"]
print(sales_data)


combined_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")
print(combined_data)

combined_data.to_csv("Private\\processed_sales_data.csv", index=False)
print("Data sparad i 'processed_sales_data.csv'")

print(os.getcwd())
