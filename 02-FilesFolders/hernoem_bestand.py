
import os

bestandnaam = "demobestand.txt"

huidige_map = os.getcwd()
volledige_pad = os.path.join(huidige_map, bestandnaam)

print("Dit bestand gaan we hernoemen: " + volledige_pad)

nieuwe_naam = input("nieuwe bestandnaam: ")

if len(nieuwe_naam) > 0:
    nieuw_volledige_pad = os.path.join(huidige_map, nieuwe_naam)

    print("bestand wordt hernoemt naar: " + nieuw_volledige_pad)

    os.rename(volledige_pad, nieuw_volledige_pad)
    print("bestand hernoemt")

else:
    print("Sorry, geen juist of geldige invoer -END- ")
