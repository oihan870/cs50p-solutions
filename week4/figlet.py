import sys
import random
import pyfiglet

fonts = pyfiglet.FigletFont.getFonts()


if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

figlet = pyfiglet.Figlet(font=font)

text = input("Input: ")

print(figlet.renderText(text))
