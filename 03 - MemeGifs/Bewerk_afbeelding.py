from PIL import Image, ImageDraw
from PIL import Image, ImageFont
# Afbeelding openen en oplsaan in de variabele met de naam: afbeelding
afbeelding = Image.open("Spooks.jpg")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen
breedte = afbeelding.width
hoogte = afbeelding.height

# Afmetingen op het scherm zetten
# Met str() zet je een int (getal) naar een string om. Dan kan print() het gebruiken.
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

# Andere info uitlezen en tonen
print(afbeelding.format, afbeelding.size, afbeelding.mode)



#Eigen Code
lettertype = ImageFont.truetype("impact.ttf", 20)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)


# En opslaan onder een andere naam
afbeelding.save("Spooks_achtergrond.jpg")
