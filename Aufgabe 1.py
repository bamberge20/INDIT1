#Aufgabe 1
#1.) Benutzer begrüßen
#2.) eine erste und zweite Zahl engegen nimmt
#3.) Summe der Zahlen
#4.) Differenz Kleinerer weniger Größeren 
#5.) Produkt der Zahlen
#6.) Quotient der Kleineren durch Größeren 
#Benutzer Grüßen
print("Hallo Benutzer")
#erste Zahl entgegen nehmen
zahl1 = input("Eingabe einer Zahl: ")
#zweite Zahl entgegen nehmen
zahl2 = input("Eingabe einer zweiten Zahl: ")
a = float(zahl1)
b = float(zahl2)

if a<b:
    ZahlKlein = a 
    ZahlGroß = b 
    
elif a>b:
    ZahlGroß = a 
    ZahlKlein = b
else:
    ZahlKlein = a
    ZahlGroß = b
    
print("Summe: ", a + b)
print("Differenz: ", ZahlKlein - ZahlGroß)
print("Produkt: ", a * b)
print("Quotient: ", ZahlKlein / ZahlGroß)

    

    



