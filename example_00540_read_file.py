
# einlesen von test.txt
filename="test.txt"
myfile=open(filename)   #oder open("test.txt), wenn dateiname bekannt (harte kodierung - gefahr, wenn dateiname nicht fix oder geändert)
mylines=myfile.readlines() #öffnet permanent das paket myfile - muss extra beendet werden
myfile.close() #beendet die abfrage des pakets
print(mylines) #gibt das resultat des abgefragten pakets aus
