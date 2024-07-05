# decimal - typ liczbowy do ominięcia problemu zaokrąglanie
# # zajmuje duzo pamięci w porównaniu z float
# wolniejsze operacje na tych liczbach
from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja = Decimal('0.00')

suma = kwota1 + kwota2
print("Suma", suma)  # Suma 15.75

roznica = kwota1 - kwota2
print("Róznica", roznica)  # Róznica 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem", kwota_z_podatkiem)
print("Kwota z podatkiem", kwota_z_podatkiem.quantize(precyzja))
# Kwota z podatkiem 12.6075
# Kwota z podatkiem 12.61
