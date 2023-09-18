import os                          # Mainly to access other directories
import subprocess                  # To run other python files
from classes import colors         # Variables to color text
from classes import textMethods    # Most methods
from classes import sceneControl   # Methods that control what scene to show, mainly for going from one scene to another
import json                        # For configuration files


# Verifies if boolean inside config.json is True or False
def return_config_status_bool(config_var):
    with open("config.json", "r") as f:
        data = json.load(f)

    if data[config_var]:
        status = "On"
    else:
        status = "Off"

    return status


# If True change to False and vice-versa
def change_config_bool(config):
    with open("config.json", "r") as f:
        data = json.load(f)
        if data[config]:
            data[config] = False
        else:
            data[config] = True

    with open("config.json", "w") as f:
        json.dump(data, f)
        f.close()


# List with scene titles
scenes = ["Forgetfulness, cold, encounter", "Memories, gratitude, gestures"]

# Variable "screen" will define what the match/case below will do
screen = 0

while True:
    # variable jump_to_scene verifies if code should instead redirect to scene using method inside classes/sceneControl.py
    jump_to_scene = sceneControl.checkSceneJump()

    # if jump_to_scene is not 0 then it means redirection shoul happen, and will happen through subprocess
    # otherwise does nothing
    if jump_to_scene != 0:
        subprocess.run(["python", f"scenes/scene{jump_to_scene}.py"])
    else:
        pass

    # variable "i" counts how many scenes are inside "scenes" list
    i = 0
    match screen:
        # Main screen
        case 0:
            try:
                # Asks what screen or action user wants to take
                choice = input("1. Scenes\n2. Configurations\nX. Close\n")

                # Method inside classes will check if choice is numeric, if it is then turn it into integer
                # If not then .upper() the String
                choice = textMethods.checkNumeric(choice)

                if choice == 1:
                    screen = 1

                elif choice == 2:
                    screen = 2

                # Terminates code safely
                elif choice == "X":
                    exit()

                else:
                    print(f"{colors.RED}Option does not exist!\n{colors.END}")

            except Exception as e:
                print(e)
        # Scene selection
        case 1:
            textMethods.clearTerminal()
            # Asks what scene you want and then prints the "scenes" list indexed by "i" variable
            print("What scene do you want to read?")
            for scene in scenes:
                i = i + 1
                print(f"{i}. {scene}")
            try:
                # That's the actual input for the prompt
                chosenScene = input("\nX. Back\n")
                chosenScene = textMethods.checkNumeric(chosenScene)
                # If "X" then close
                # If user input is numeric and scene in scenes folder then run scene
                if f"scene{chosenScene}.py" in os.listdir("scenes"):
                    subprocess.run(["python", f"scenes/scene{chosenScene}.py"])
                elif chosenScene == "X":
                    screen = 0
                # inform if the file was not found inside scenes folder
                else:
                    raise FileNotFoundError
            # the exception itself
            except FileNotFoundError:
                print(f"{colors.RED}Desired file not found in scenes list.{colors.END}")
            except ValueError:
                print(f"{colors.RED}Invalid option!{colors.END}")
            except Exception as e:
                print(e)
        # Configuration screen
        case 2:

            try:
                # Shows settings and asks which one to change
                choice = input(
                    f"{colors.YELLOW}Configurations{colors.END}\n1. Clear terminal after choice?: {return_config_status_bool('clear-terminal')}\nX. Back\n")
                choice = textMethods.checkNumeric(choice)

                # That setting is responsible to clear the terminal every time an action is taken
                # It is defined in classes/textMethods.py
                if choice == 1:
                    change_config_bool("clear-terminal")
                    print(
                        f"{colors.GREEN}CLear terminal set to: {return_config_status_bool('clear-terminal')}{colors.GREEN}\n")
                    pass
                elif choice == "X":
                    screen = 0

            except ValueError:
                print(f"{colors.RED}Invalid option!{colors.END}\n")
            except Exception as e:
                print(e)
