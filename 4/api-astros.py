from typing import List

import requests as re
from pydantic import BaseModel

#  pip install requests

url = "http://api.open-notify.org/astros.json"

response = re.get(url)
print(response)  # <Response [200]>

# HTTP 200 ok
# HTTP 301 - przekierowania
# HTTP 404 - Page not found
# HTTP 400 Bad Requests - przekazalismy błedne parametry
# HTTP 500 Wewnętrzny bład serwera

print(response.text)
# {"people": [{"craft": "ISS", "name": "Oleg Kononenko"}, {"craft": "ISS", "name": "Nikolai Chub"},
#             {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, {"craft": "ISS", "name": "Matthew Dominick"},
#             {"craft": "ISS", "name": "Michael Barratt"}, {"craft": "ISS", "name": "Jeanette Epps"},
#             {"craft": "ISS", "name": "Alexander Grebenkin"}, {"craft": "ISS", "name": "Butch Wilmore"},
#             {"craft": "ISS", "name": "Sunita Williams"}, {"craft": "Tiangong", "name": "Li Guangsu"},
#             {"craft": "Tiangong", "name": "Li Cong"}, {"craft": "Tiangong", "name": "Ye Guangfu"}], "number": 12,
#  "message": "success"}
response_data = response.json()  # zammiana na słownik
print(response_data)
print(response_data['people'])


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int


data = AstroData(**response_data)
print(data)
print(data.number)
print(data.people)
for astronaut in data.people:
    print(f"{astronaut.name}, {astronaut.craft}")
# Oleg Kononenko, ISS
# Nikolai Chub, ISS
# Tracy Caldwell Dyson, ISS
# Matthew Dominick, ISS
# Michael Barratt, ISS
# Jeanette Epps, ISS
# Alexander Grebenkin, ISS
# Butch Wilmore, ISS
# Sunita Williams, ISS
# Li Guangsu, Tiangong
# Li Cong, Tiangong
# Ye Guangfu, Tiangong
