import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=fe16237c900f449681a134851243001&q={city}"

r = requests.get(url)

# print(r.text)

wdic = json.loads(r.text)
print(wdic['current']['temp_c'])

text = f"The current weather in {city} is {wdic['current']['temp_c']} degrees"
speak.Speak(text)