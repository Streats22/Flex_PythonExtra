import io

bestand = open("test.txt", "w")
bestand.write("Test 123!");

bestand.close()

bestand2 = open("test.text", "r")
bestand2.write("Lekker alles overschrijven")
