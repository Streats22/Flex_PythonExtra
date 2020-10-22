from PIL import Image, ImageDraw
from PIL import Image, ImageFont

achtergrond = Image.open("Meme_01.jpg")
breedte = achtergrond.width
hoogte = achtergrond.height
lettertype = ImageFont.truetype("impact.ttf", 40)

breedte = str(achtergrond.width)
hoogte = str(achtergrond.height)


# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Running my first Python code like \nNo problem..."
# Bereken de breedte en hoogte van de tekst
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (620 - tekst_breedte) / 2
tekst_y = (1020 - tekst_hoogte) / 2

# De nieuw berekende tekst_x en tekst_y gebruiken
tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))


# Het resultaat tonen
achtergrond.show()

# breedte en hoogte door twee delen (en afronden naar beneden)


achtergrond.save('Meme_met_text.jpg')
