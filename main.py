import time
print("Codez par Remi_ByPass#7867")
print("Valeur du produit (en €)")
prix = float(input("Le produit vaut : "))
time.sleep(1)
print("Donnez la remise en % \nExemple: 40% de remise sur un produit d'une valeur de 48€ (99 au max) :")
remise = float(input())
while remise >=100:
    print('La remise ne doit pas faire plus de 99% !\n(La valeur fait', remise, ')')
    remise = float(input('Remise = '))
total = prix*remise
prix_total = total/100-prix
time.sleep(1)
print("Le produit (",prix,"€ ) coutera", -prix_total,"€ avec une remise de", remise, "%")
time.sleep(1)
print("Mon discord: https://discord.gg/vEz64HF")
time.sleep(10)
