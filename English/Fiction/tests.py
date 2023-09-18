import json


def return_config_status(configVar):
    with open("config.json", "r") as f:
        data = json.load(f)

    if data[configVar]:
        status = "Ativado"
    else:
        status = "Desativado"

    return status


def read_config():
    with open("config.json", "r") as f:
        data = json.load(f)
    print(data["clear-terminal"])


def change_config():
    with open("config.json", "r") as f:
        data = json.load(f)
        if data["clear-terminal"]:
            data["clear-terminal"] = False
        else:
            data["clear-terminal"] = True
    with open("config.json", "w") as f:
        json.dump(data, f)
        f.close()


change_config()
read_config()
