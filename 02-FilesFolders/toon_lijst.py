import os


huidige_map = os.getcwd()

alle_bebstanden = os.scandir(huidige_map)

#print("inhoudsopgaven van de map: " + huidige_map)
for bestand in alle_bebstanden:

    #print(bestand.name)

    if bestand.is_file():

        print(bestand.name + " (BESTAND)")
    elif bestand.is_dir():

        print(bestand.name + " (MAP)")
    else:
        print(bestand.name + " (ONBEKEND TYPE)")
