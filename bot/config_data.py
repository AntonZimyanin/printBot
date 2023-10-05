import json


def config_data(path) -> dict:
    with open(path) as config_file:
        config_data = json.load(config_file)

        return config_data
    

config_dict = config_data("bot/config.json")