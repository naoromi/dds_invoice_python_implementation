import pandas as pd
from item import Item
from datetime import datetime

item_msrp = pd.read_csv("item_msrp.csv")
item_msrp_dataframe = pd.DataFrame(item_msrp)

customer_name = input("Enter the customer name: ")
customer_address = input("Enter the customer address: ")
customer_phone = input("Enter the customer phone: ")
customer_email = input("Enter the customer email: ")

invoice_data = {
    "Customer Name": customer_name,
    "Customer Address": customer_address,
    "Customer Phone": customer_phone,
    "Customer Email": customer_email,
    "Item": [],
    "Quantity": [],
    "Price": [],
    "Total": [],
}

invoice_dataframe = pd.DataFrame(invoice_data)

def add_item(current_dataframe):
    item = Item(item_msrp_dataframe)
    result = item.add_item()
    
    if result:
        invoice_data["Item"].append(result["item"])
        invoice_data["Quantity"].append(result["quantity"])
        invoice_data["Price"].append(result["price"])
        invoice_data["Total"].append(result["total"])
        return pd.DataFrame(invoice_data)
    return current_dataframe

# Usage:
invoice_dataframe = add_item(invoice_dataframe)

# Generate timestamp for unique filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"invoice_{customer_name.replace(' ', '_')}_{timestamp}.csv"

# Export to CSV
invoice_dataframe.to_csv(filename, index=False)
print(f"Invoice has been saved to {filename}")