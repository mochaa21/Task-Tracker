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
    "Academy": "Lindris Academy"
}

print(thisdict)
print(thisdict["Name"])

for daftar in thisdict.values():
    print(daftar)

user_profile = {"username": "clara99", "role": "admin", "status": "active"}

for user in user_profile.items():
    print(user)