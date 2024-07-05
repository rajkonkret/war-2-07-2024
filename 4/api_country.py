from typing import List

import requests
from pydantic import BaseModel

url = "https://restcountries.com/v3.1/name/Poland"

response = requests.get(url)
print(response.text)  # odczytanie jsona jaki przysłało api


class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    nativeName: NativeName


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


data = response.json()
country_data = [CountryInfo(**data) for data in response.json()]
print(type(country_data))  # <class 'list'>
for country in country_data:
    print(country)
    print(country.capital)
    print(country.population)
    print(country.name.nativeName.pol.official)
# ['Warsaw']
# 37950802
# Rzeczpospolita Polska
