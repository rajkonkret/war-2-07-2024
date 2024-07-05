import xml.etree.ElementTree as ET
import requests as re
from pydantic import BaseModel

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

