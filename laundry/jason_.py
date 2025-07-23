import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Function to update payment and delivery status for a given order ID
def update_order(order_id, new_payment, new_delivery):
    with open('data.json', 'r') as file:
        data = json.load(file)

    if order_id in data:
        data[order_id]["payment"] = new_payment
        data[order_id]["delivery"] = new_delivery

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Example: Update payment and delivery status for order ID "1"
# order_id = "1"
# new_payment = "paid"
# new_delivery = "completed"

# if update_order(order_id, new_payment, new_delivery):
#     print(f"Payment and delivery status for order ID {order_id} updated successfully.")
# else:
#     print(f"Order ID {order_id} not found.")

# Write the updated data back to the JSON file

