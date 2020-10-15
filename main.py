import time
print("Codez par Remi_ByPass#7867")
print("Valeur du prdouit (en €)")
prix = float(input("Le produit vaut : "))
print("Donnez la remise en % \nExemple: 40% de remise sur un produit d'une valeur de 48€ (99 au max) :")
remise = float(input())
while remise >=100:
    print('La remise ne doit pas faire plus de 99% !\n(La valeur fait', remise, ')')
    remise = float(input('Remise = '))
total = prix*remise
prix_total = total/100-prix
print("Le produit (",prix,"€ ) coutera", -prix_total,"€ avec une remise de", remise, "%")
print("Mon discord: https://discord.gg/vEz64HF")
time.sleep(5)
