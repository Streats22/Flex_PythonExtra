import io
import os


bestand = open("klasgenoten.txt", "r")

#regel1 = bestand.readline()
#print(regel1)

#regel2 = bestand.readline()
#print(regel2)

tekst_regel = bestand.readline()


while tekst_regel:
    os.mkdir(tekst_regel)
    tekst_regel = tekst_regel.strip()

    print(tekst_regel)

    tekst_regel = bestand.readline()
