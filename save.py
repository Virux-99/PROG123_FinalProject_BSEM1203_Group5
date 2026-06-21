from tkinter import messagebox
import json
from input_v import validate_client_data, validate_stock_data

def load_clients_from_json():
    try:
        with open("clients.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def load_stocks_from_json():
    try:
        with open("stocks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_clients_to_json(transactions_queue):
    with open("clients.json", "w") as file:
        json.dump(transactions_queue, file, indent=4)


def save_stocks_to_json(stock_queue):
    with open("stocks.json", "w") as file:
        json.dump(stock_queue, file, indent=4)

#-----------------client--------------------
def save_client_records(transactions_queue, data):

    valid, msg = validate_client_data(data)

    if not valid:
        messagebox.showerror("Error", msg)
        return False

    transactions_queue.append(data)
    save_clients_to_json(transactions_queue)

    messagebox.showinfo("Success", "Client record saved successfully")
    return True
#------------------stock------------------
def save_stock_records(stock_queue, data):

    valid, msg = validate_stock_data(data)

    if not valid:
        messagebox.showerror("Error", msg)
        return False

    cost = data["cost_price"]
    selling = data["selling_price"]

    profit = selling - cost

    stock = {
        "stock_name": data["stock_name"],
        "stock_amount": data["stock_amount"],
        "cost_price": cost,
        "selling_price": selling,
        "profit": profit
    }

    stock_queue.append(stock)
    save_stocks_to_json(stock_queue)

    messagebox.showinfo("Success", "Stock saved successfully")
    return True



