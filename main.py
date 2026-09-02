import sys
import json

# print(f'Python version: {sys.version}')
# print(f'Platform: {sys.platform}')
# print(f'Passed to the script: {sys.argv}')
# print(f'Copyright: {sys.copyright}')
# print(f'Version tuple: {sys.version_info}')

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
print(json.dumps(thisdict))