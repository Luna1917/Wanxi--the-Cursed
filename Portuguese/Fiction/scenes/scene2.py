import sys
sys.path.append("../Fiction")

import subprocess
from classes import colors
from classes import textMethods
from classes import sceneControl

page = 1

pages = [
    f"Acordei deitada numa cama dentro de um pequeno quarto, vestida em um vestido azul de {colors.YELLOW}lã{colors.END} "
    f"decorado com os pelos brancos de algum animal ao redor das golas. Senti-me um pouco melhor, "
    f"mas ainda estava fraca; no entanto, já conseguia manter o foco de maneira razoável. Supus que "
    f"estava no quarto do homem.\n"
    ,#0
    f"Era um quarto de madeira decorado com um quadro retratando um sereno oceano durante a noite. No "
    f"quarto, havia um armário, uma estante vazia e uma mesa de jantar com duas cadeiras. A minha "
    f"cama era uma cama de casal com um confortável cobertor marrom."
    ,#1

    "À minha esquerda, havia uma mesinha com um prato e uma vela recém acesa. Em cima do prato, "
    "havia um pequeno pedaço de carne e queijo, e ao lado, um metálico copo de vinho."
    ,#2
    "Eu sentia fome e sede, e rapidamente consumi o alimento e a bebida, grata por estar viva."
     #3
     ]


while True:
    sceneControl.setSceneJump(0)
    try:
        match page:
            case 1:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(0, pages)

                choice = input(f"1. Avançar\n2. Voltar para cena 1\n{colors.YELLOW}3. Lore: Uso de lã na região{colors.END}\n")
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
                    f"{colors.YELLOW}Lore{colors.END}:\nLã e linho são os materiais mais comuns da região por serem baratos e de "
                    f"fácil aquisição. No frio, roupas de lã são preferíveis, e no calor, roupas de linho são "
                    f"preferíveis."
                    )
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()
            case 2:
                print(f"{colors.GREEN}???{colors.END}")
                textMethods.printPage(1, pages)

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Cena 3\n2. Voltar\nX. Menu inicial\n")
                choice = textMethods.checkNumeric(choice)

                if choice == 1:
                    print("Código ainda não escrito.")
                    #page = page + 1
                elif choice == 2:
                    page = page - 1
                elif choice == "X":
                    textMethods.clearTerminal()
                    break
                else:
                    textMethods.invalid_option_error()

    except ValueError:
        print("Tecla inválida.")
