import os

naamMap = " "

lengte_naamMap = 0

while lengte_naamMap == 0:
     naamMap = input("Hoe moet de map heten? ")

     lengte_naamMap = len(naamMap)

     if lengte_naamMap > 0:
         os.mkdir(naamMap)
     else:
         print

         print("Je hebt nog geen naam ingevoerd..")
         

print("De map " + naamMap + " is aangemaakt! :)")
