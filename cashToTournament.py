from __future__ import unicode_literals
import easygui
import re
import os

# -- ! Program Variables Table ! -- #
# 1. cashFile - A file in the system from where the cash hands are going to be extracted into the program
# 2. pokerHands - The string with all the text read from cashFile that will be transformed into tournament format
# 3. tournamentFile - The file in the system where the pokerHands string is going to be saved.
# --------------------------------------------------------------------------------------------------------------



def searchAndReplace (expression, replacement, text):
    return re.sub(expression, replacement, text)


print("Select the PokerStars file with the hands in cash format.")

cashFile = open(easygui.fileopenbox("", "Open", os.path.expanduser("~\Desktop\*.txt")), "r")
pokerHands = cashFile.read()
print("OK")

pokerHands = (searchAndReplace ('((\s|\()([0-9]+(\s|\))))', r'\2€\3', pokerHands ) )
pokerHands = (searchAndReplace ('(\*\*\*\*\*\*).*', r'\n', pokerHands ) )
pokerHands = (searchAndReplace ('Tournament.+\)', r"Hold'em No Limit (€1000/€2000)", pokerHands ) )

print("Choose where to save the converted file in tournament format, ready to be fed into PokerSnowie.")
tournamentFile = open (easygui.filesavebox("", "Save As", "tournamentHands.txt", ["*.txt"]), "w", encoding="utf-8")


tournamentFile.write( pokerHands )
tournamentFile.close()

input('Press any key to terminate the program')


