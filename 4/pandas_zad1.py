import pandas as pd
import openpyxl

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', "Krzysztof Zakrzewski"],
                   'wynik': [15, 38, 21]})
print(df)


#                   Osoba  wynik
# 0          Michał Jakub     15
# 1              Ewa Noga     38
# 2  Krzysztof Zakrzewski     21

def sprawdz(punkty):
    if punkty > 20:
        return "Zdany"
    else:
        return "Oblany"


df.wynik = df.wynik.apply(sprawdz)
print(df)
#                   Osoba   wynik
# 0          Michał Jakub  Oblany
# 1              Ewa Noga   Zdany
# 2  Krzysztof Zakrzewski   Zdany

df.to_csv('wynik.csv', index=False)
df.to_excel('wynik.xlsx', index=False)
