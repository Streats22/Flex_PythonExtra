import os

werkmap = os.getcwd()
print("De huidige map is: " + werkmap)

mapnaam = input("Welke naam wil je voor de map? ")

lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + " is aan gemaakt.")
else:
    print("Voer een naam in A.U.B")

    
