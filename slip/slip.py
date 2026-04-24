import qrcode
import os
import json
import base64
from datetime import datetime
from io import BytesIO
import webbrowser



def generate_invoice_slip():
    shop_details = {
    "name": "TAJ GENERAL STORE",
    "address": "123 Main Bazaar, City Center",
    "phone": "+92 123 4567890",
    "gst": "GST123456"
    }
    order_file = "last_order_number.txt"

    if os.path.exists(order_file):
        with open (order_file, 'r') as f:
            last_order = int(f.read().strip())
        order_number = last_order + 1
    else:
        order_number = 1
        with open (order_file, 'w') as f:
            f.write(str(order_number))

print ("=" * 30)
print(f"📋 NEW Order # {order_number}")

#get customer
customer = input("Customer Name: ")

#get Item
items = []
while True:
    item_name = input("   Item name (or 'done'): ")
    if item_name.lower() == 'done':
        if len(items) == 0:
            print("   ⚠️ Please add at least one item!")
            continue
        break
    try:
        item_price = float(input(f"     price of'{item_name}': $"))
        item_qty = input(f"   Quantity (Enter for 1): ") or "1"
        items.append({
            "name": item_name,
            "price": item_price,
            "quantity": int(item_qty),
            "total": item_price * int(item_qty)
        })
        print(f"   ✅ Added: {item_name} x{item_qty} = ${item_price * int(item_qty):.2f}")
    except ValueError:
        print("   ❌ Invalid price! Please enter a number.")
