sales_data = pd.read_csv("sales_2025.csv")
customer_data = pd.read_csv("customers.csv")

merged_data = pd.read_csv(sales_data, customers_data, on ="CustomerID", how="inner")

print(merged_data)