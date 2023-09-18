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
    f"Eu estava deitada na neve olhando para as nuvens no céu sem me lembrar de absolutamente nada. Ao observar ao "
    f"meu redor, percebi que estava no meio do nada, vestindo um sofisticado vestido"
    ,  # 0

    f"Tentei me levantar, mas não era capaz. O movimento do meu corpo estava extremamente limitado, "
    f"como se houvesse um grande peso me paralisando no chão."
    ,  # 1

    "Sentia frio; meus lábios estavam secos e minha respiração fraca, mas de longe vi algo... Um "
    "homem montado em uma criatura."
    ,  # 2

    "Gritava por ajuda, mas palavras não saíam da minha boca; apenas sons sem sentido. Sentia medo, "
    "mas continuei a gritar, e o homem continuava a se aproximar cada vez mais."
    ,  # 3

    "O homem me viu, rapidamente desmontou da besta e correu em minha direção. Era um homem alto, "
    "de cabelos longos e negros e uma barba muito bem cuidada; ele certamente era vaidoso. Ao me alcançar, "
    "agachou-se e disse desesperado: 'O que houve? Não consegue se mover?' Eu não o entendia..."
    ,  # 4

    "Ele se aproximou e me segurou com cuidado, levando-me em seus braços. Caminhou até sua besta, "
    "que carregava uma pequena mochila, e carinhosamente me colocou novamente na neve. A besta era "
    "peluda, branca, quadrúpede, com listras pretas espalhadas por seu pelo. Possuía afiadas garras "
    "e um forte corpo, suas pontudas orelhas pareciam macias, tinha uma grande cauda e uma aparência "
    "elegante. O homem tirou da mochila um cantil de couro e com ele saciou minha sede."
    ,  # 5

    "O homem me segurou novamente e disse para a besta: [kolosoto, Mjal] 'Vamos, Mjal.' A besta emitiu um pequeno "
    "rugido e começou a andar ao lado do homem, que me carregava em seus braços, fora da besta."
    ,  # 6

    "Senti-me triste e chorei em silêncio; eu não entendia minha situação e não compreendia meu "
    "destino."
    ,  # 7

    "Após alguns minutos, exausta, adormeci."
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

                choice = input("1. Avançar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")

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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Avançar\n2. Voltar\nX. Menu inicial\n")
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

                choice = input("1. Ir para cena 2\n2. Voltar\nX. Menu inicial\n")
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
                print("Página inválida.")
                break

    except ValueError:
        print("Tecla inválida!")
