import sys
import json
import datetime
import os

print(f'Python version: {sys.version}')
print(f'Platform: {sys.platform}')
print(f'Passed to the script: {sys.argv}')
print(f'Copyright: {sys.copyright}')
print(f'Version tuple: {sys.version_info}')

thisdict = {
    "Name": "Ariel Ashera",
    "Age": 20,
    "Academy": ["Lindris Academy", "Venezia Pax Institute", "Gehenna del Silencio"]
}

x = '{"Name": "Ariel Ashera", "Age": 20, "Academy": "Lindris Academy"}'

y = json.loads(x)

print(y)

benedict = '{"Name": "Ariel Ashera", "Age": 20, "Academy": ["Lindris Academy", "Venezia Pax Institute", "Gehenna del Silencio"]}'

waine = json.loads(benedict)

print(waine)

# convert scheme
print(json.dumps(thisdict, indent=4))

a = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(a, indent=4, separators=(" . ", " = "), sort_keys=True))

# datetime
isDate = datetime.datetime.now()
print(isDate)
print(isDate.year)
print(isDate.strftime("%A"))

isNDate = datetime.datetime(2016, 8, 20)
print(isNDate)
print(isNDate.strftime("%B"))