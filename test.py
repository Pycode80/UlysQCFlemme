import json
print("1525" in json.load(open("data.json")))
print(json.load(open("data.json"))["1525"])