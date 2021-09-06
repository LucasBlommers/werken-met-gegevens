croisantPrijs = .39
croisants = 17
stokbroodPrijs = 2.78
stokbroden = 2
kortingsbonKorting = 0.5
kortingsbonnen = 3

totalPrice = (croisantPrijs * croisants) + (stokbroodPrijs * stokbroden) - (kortingsbonKorting * kortingsbonnen)
print("De feestlunch kost je bij de bakker " + str(totalPrice) + " voor de " + str(croisants) + " croissantjes en de " + str(stokbroden) + " stokbroden als de " + str(kortingsbonnen) + " kortingsbonnen nog geldig zijn!")