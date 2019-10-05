import math

#coding=utf-8
#Implementiere einen Rentenrechner
#Anfangskapital: 100
#Zinsen: 6%
#Laufzeit: Jahre
#Formel für die Zinseszinsrechnung: Anfangskapital * ((1+(Zinsatz/100)) ^ jeweiligen Jahre)
#Anfangskapital*math.pow(Zinsen,1)

"""
Ergebnis:
Anfangskapital:  100
Zinssatz:  6.0
Veranlagungszeitraum:  5
Kapital im Jahr 1 : 106.0
Kapital im Jahr 2 : 112.36
Kapital im Jahr 3 : 119.1016
Kapital im Jahr 4 : 126.247696
Kapital im Jahr 5 : 133.82255776
"""
#Knull=K*(1+1/100)^n


depot=100
zinssatz=1
zeitraum=input("Bitte Veranlagungszeitraum in Jahren eingeben: ")
i=0

while i<=int(zeitraum):
    depot=depot+(depot/100*int(zinssatz))
    print(depot)
    i=i+1




