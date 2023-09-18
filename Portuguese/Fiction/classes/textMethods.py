import json
import sys

sys.path.append("../Fiction")

from classes import colors
import os


# Works similar to an exception
def invalid_option_error():
    print(f"{colors.RED}Opção inválida!{colors.END}")


# Check if number is numeric, if it is then turn into integer, if not then turn into uppercased version
def checkNumeric(variable):
    if variable.isnumeric():
        variable = int(variable)
    else:
        variable = variable.upper()

    return variable


# Prints text inside list index by position of the first argument, uses the first argument as the first page and the length
# Of the list as to print "Page: 1/9" for example
def printPage(pageNumber, list):
    print(f"{list[pageNumber]}\nPágina: {pageNumber + 1}/{len(list)}")

# Clears the terminal
def clearTerminal():
    with open("config.json", "r") as f:
        data = json.load(f)
        if data["clear-terminal"]:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            pass
