# write a while loop to check if input with following symbols *,+,-,/ is  correct
# if yes exit loop
# True-> while True:

###
#while True:
#    sym=input("Bitte Symbol eingeben *+-/: ")
#    if sym in "*+-/":
#        print("ok")
#        break
###
#hier würde jede Kombination der verfügbaren Zeichen die Schleife brechen


# solution b
#Variante 2, wenn exakte Eingabe erforderlich - aus Liste (mit eckiger Klammer dargestellt)

while True: #dieser Befehl führt zu endloser Schleife - wenn weggelassen, wäre nur 1 Abfrage. Anwendungsbeispiel Passwortabfrage#
    sym=input("Bitte Symbol eingeben *+-/: ")
    if sym in ["*", "+", "-", "/"]:
        print("ok")
        break
