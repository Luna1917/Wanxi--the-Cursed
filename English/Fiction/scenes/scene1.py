import sys

# So i can import the classes from parent directory
sys.path.append("../Fiction")

import subprocess
from classes import colors
from classes import textMethods
from classes import sceneControl

# The scene Match/Case, mainly decides what text to show
page = 1

# The texts to show
pages = [
    f"I was lying in the snow, looking at the clouds in the sky, without remembering anything at all. As I observed "
    f"around me, I realized I was in the middle of nowhere, wearing a sophisticated black dress."
    ,  # 0

    f"I tried to get up, but I couldn't. The movement of my body was extremely limited, as if there was a heavy "
    f"weight paralyzing me on the ground."
    ,  # 1

    "I felt cold; my lips were dry, and my breath weak, but from afar, I saw something... A man mounted on a creature."
    ,  # 2

    "I screamed for help, but words didn't come out of my mouth; only meaningless sounds. I felt fear, but I kept screaming, "
    "and the man kept getting closer and closer."
    ,  # 3

    "The man saw me, quickly dismounted from the beast, and ran towards me. He was a tall man with long black hair "
    "and a very well-groomed beard; he certainly cared about his looks. When he reached me, he crouched down and said "
    "desperately, 'What happened? Can't you move?' I didn't understand him..."
    ,  # 4

    "He approached and held me carefully, carrying me in his arms. He walked to his beast, which carried a small "
    "backpack, and lovingly placed me back in the snow. The beast was furry, white, quadrupedal, with black stripes "
    "scattered across its fur. It had sharp claws and a strong body; its pointed ears looked soft, and it had a "
    "large tail and elegant appearance. The man took a leather canteen from the backpack and quenched my thirst with "
    "it."
    ,  # 5
    # "Kolosoto, mjal" is written in a conlang
    "The man held me again and said to the beast: [kolosoto, Mjal] 'Let's go, Mjal.' The beast emitted a small roar "
    "and began to walk alongside the man, who carried me in his arms, away from the beast."
    ,  # 6

    "I felt sad and cried in silence; I didn't understand my situation and didn't grasp my destiny."
    ,  # 7

    "After a few minutes, exhausted, I fell asleep."
    # 8
]


while True:
    # Just a precaution, line below might not be needed
    sceneControl.setSceneJump(0)
    try:
        match page:
            case 1:
                # Prints character name > page text inside pages > {page index + 1}/len(pages) so we have a page counter
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(0, pages)

                choice = input("1. Forward\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                # Clears terminal if set to do so
                textMethods.clearTerminal()

                # Next Page
                if choice == 1:
                    page = page + 1
                elif choice == "X":
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
                # Previous page
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
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
                    break

                else:
                    textMethods.invalid_option_error()

            case 4:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(3, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")

                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case 5:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(4, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case 6:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(5, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case 7:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(6, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case 8:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(7, pages)

                choice = input("1. Forward\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case 9:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(8, pages)

                choice = input("1. Go to Scene 2\n2. Back\nX. Start menu\n")
                choice = textMethods.checkNumeric(choice)

                textMethods.clearTerminal()

                if choice == 1:
                    # Next scene
                    # It sets the scene jump to 2 and executes the main file so it will open the scene instead
                    sceneControl.setSceneJump(2)
                    subprocess.run(["python", "../Fiction/main.py"])
                    break
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    break

                else:
                    textMethods.invalid_option_error()

            case _:
                print("Invalid page.")
                break

    except ValueError:
        print("Invalid Key.")
