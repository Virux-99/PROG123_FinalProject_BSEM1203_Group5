#----------------clients----------------------
def validate_client_data(data):
    if "client_number" not in data:
        return False, "Client number is required"

    try:
        client_number = int(data["client_number"])
        if client_number <= 0:
            return False, "Client number must be greater than 0"
    except ValueError:
        return False, "Client number must be a valid number"

    if not isinstance(data["name"], str) or data["name"].strip() == "":
        return False, "Client name is required"

    if not isinstance(data["goods"], str) or data["goods"].strip() == "":
        return False, "Goods is required"

    if not isinstance(data["quantity"], int) or data["quantity"] <= 0:
        return False, "Quantity must be a valid number"

    if not isinstance(data["total"], (int, float)) or data["total"] <= 0:
        return False, "Total must be a valid amount"

    if not isinstance(data["paid"], (int, float)) or data["paid"] < 0:
        return False, "Paid amount is invalid"

    return True, ""

#---------------------stock---------------------
def validate_stock_data(data):

    if not isinstance(data["stock_name"], str) or data["stock_name"].strip() == "":
        return False, "Stock name is required"

    try:
        stock_amount = int(data["stock_amount"])
        cost_price = float(data["cost_price"])
        selling_price = float(data["selling_price"])
    except ValueError:
        return False, "Invalid numeric values"

    return True, ""