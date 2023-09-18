import json


# Checks if any Scene changed the config.json so main.py will execute it instead of running its own code
def checkSceneJump():
    with open("config.json", "r") as f:
        data = json.load(f)

    jump = data["jump-to-scene"]

    f.close()

    return jump

# Changes config.json so main.py will execute a scene instead of running its own code
def setSceneJump(scene):
    with open("config.json", "r") as f:
        data = json.load(f)
        data["jump-to-scene"] = scene
    with open("config.json", "w") as f:
        json.dump(data, f)
    f.close()

# Resets config.json jump config to 0, i could just use setSceneJump but it's more comfortable to me to use reset
def resetSceneJump():
    jump_to_scene = checkSceneJump()
    if jump_to_scene != 0:
        setSceneJump(0)
    else:
        pass
