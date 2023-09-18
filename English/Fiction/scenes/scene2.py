import sys
sys.path.append("../Fiction")

import subprocess
from classes import colors
from classes import textMethods
from classes import sceneControl

page = 1

pages = [
    f"I woke up lying in a bed inside a small room, dressed in a blue {colors.YELLOW}wool{colors.END} "
    f"dress adorned with white fur around the collars. I felt a little better, "
    f"but still weak; however, I could already focus reasonably well. I assumed I was in the man's room.\n"
    ,#0
    f"It was a wooden room decorated with a painting depicting a serene ocean at night. In the "
    f"room, there was a wardrobe, an empty bookshelf, and a dining table with two chairs. My "
    f"bed was a double bed with a comfortable brown blanket."
    ,#1

    "To my left, there was a small table with a plate and a newly lit candle. On the plate, "
    "there was a small piece of meat and cheese, and next to it, a metallic cup with wine."
    ,#2
    "I was feeling hungry and thirsty, and I quickly consumed the food and drink, grateful to be alive."
     #3
     ]


while True:
    sceneControl.setSceneJump(0)
    try:
        match page:
            case 1:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(0, pages)

                choice = input(f"1. Forward\n2. Back to Scene 1\n{colors.YELLOW}3. Lore: Wool usage in the region{colors.END}\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)
                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    sceneControl.setSceneJump(1)
                    subprocess.run(["python", "../Fiction/main.py"])
                    break
                elif choice == 3:
                    # Yellow indicates there's additional information you can access; the information below
                    print(
                    f"{colors.YELLOW}Lore{colors.END}:\nWool and linen are the most common materials in the region because they are inexpensive and "
                    f"easy to obtain. In cold weather, woolen clothes are preferred, and in hot weather, linen clothes are "
                    f"preferred."
                    )
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()
            case 2:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(1, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)
                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()
            case 3:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(2, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)
                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()

            case 4:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(3, pages)

                choice = input("1. Scene 3\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                if choice == 1:
                    print("Code still not written.")
                    #page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()

    except ValueError:
        print("Invalid key.")
