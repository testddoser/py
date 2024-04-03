import requests
import time

a = requests.get("https://grabify.org/2UPJ")

print(a.text)

time.sleep(60)
