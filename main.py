import requests

a = requests.get("https://grabify.org/2UPJ")

print(a.text)
