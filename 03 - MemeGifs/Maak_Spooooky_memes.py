from PIL import Image, ImageDraw
from PIL import Image, ImageFont

achtergrond = Image.open("Spooks.jpg")
breedte = achtergrond.width
hoogte = achtergrond.height
lettertype = ImageFont.truetype("impact.ttf", 40)

breedte = str(achtergrond.width)
hoogte = str(achtergrond.height)
print(hoogte, breedte)


# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Seeing a Syntax error like.."
# Bereken de breedte en hoogte van de tekst
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (647 - tekst_breedte) / 2
tekst_y = (340 - tekst_hoogte) / 2

# De nieuw berekende tekst_x en tekst_y gebruiken
tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))


# Het resultaat tonen
achtergrond.show()

# breedte en hoogte door twee delen (en afronden naar beneden)


achtergrond.save('Spooks_Met_text.jpg')
