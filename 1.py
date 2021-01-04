a = 3
b = 5
c = 2.5
d = 1 * 2
o = 0.5 * 0.5


S1 = a * c
S2 = b * c
Su = a * b

P1 = (S1 * 2) + (S2 * 2) + Su
P2 = (S1 * 2) + (S2 * 2) + Su - (d + o)
print("Powierzchnia ścian i sufitu (bez uwzględnienia drzwi i okien) wynosi: ", P1, "m^2")
print("Powierzchnia ścian i sufitu (z uwzględnieniem drzwi i okna) wynosi: ", P2, "m^2")


