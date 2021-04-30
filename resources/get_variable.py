import yaml


def get_pet_variable(variable_name):
    with open("./resources/pet_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]


def get_store_variable(variable_name):
    with open("./resources/store_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]


def get_user_variable(variable_name):
    with open("./resources/user_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]
