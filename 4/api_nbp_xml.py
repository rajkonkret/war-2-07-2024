import xml.etree.ElementTree as ET
from typing import List

import requests as re
from pydantic import BaseModel


class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRatesTables(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x0000020DF00C4540>
table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

data = root.find(".//EffectiveDate").text
print(f"Data tabeli: {data}")

# numer tabeli -> No
no = root.find(".//No").text
print(f"Numer tabeli: {no}")
# Tabela: A
# Data tabeli: 2024-07-05
# Numer tabeli: 130/A/NBP/2024

rates = root.findall(".//Rate")
print(rates)
# <Rate>
#                 <Currency>SDR (MFW)</Currency>
#                 <Code>XDR</Code>
#                 <Mid>5.2450</Mid>
# </Rate>
currency_rates = []
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"Currency: {currency}, Code: {code}, Mid: {mid}")
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=mid))

exchange_rate_tables = ExchangeRatesTables(table=table_name, date=data, number=no, rates=currency_rates)
print(exchange_rate_tables)
