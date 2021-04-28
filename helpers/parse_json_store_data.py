def get_pet_id(order_data):
    pet_id = order_data["petId"]
    return pet_id


def get_order_id(order_data):
    order_id = order_data["id"]
    return order_id


def get_order_message(order_data):
    order_message = order_data["message"]
    return order_message
