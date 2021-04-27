#Leibnitzreihe


name = input("ihren Namen eingeben:")
print("hallo", name)

i =  int(input("Wie oft soll es ausgeführt werden:"))
zahl = 0 # benötigte Laufvariable
pi = 0
 
while zahl < i:
    pi += (-1)**zahl/(2*zahl+1) # Berechnung der Reihe 
    print("Momentane Annäherung an Pi:", pi)
    zahl += 1
    
pi *= 4 # multiplikation der Annäherung für Korrektheit 
print("Annäherung an Pi:", pi)