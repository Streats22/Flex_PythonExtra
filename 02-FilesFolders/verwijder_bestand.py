
import os

bestand = input("Welk bestand wil je verwijderen? ")

if len(bestand) > 0:
    if os.path.exists(bestand):

        #verwijder bestandnaam
        os.remove(bestand)
        print("Het bestand " + bestand + " is verwijdert, das pech..")
    else:
        print("Dit bestand bestaat niet")
else:
    print("geen invoer, script zal stoppen...")
