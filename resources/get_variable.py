import yaml


def get_pet_variable(variable_name):
    with open("/home/korbut/PycharmProjects/pet_store/resources/pet_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]


def get_store_variable(variable_name):
    with open("/home/korbut/PycharmProjects/pet_store/resources/store_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]


def get_user_variable(variable_name):
    with open("/home/korbut/PycharmProjects/pet_store/resources/user_data.yaml", "r") as f:
        config = yaml.safe_load(f)
        return config[variable_name]
