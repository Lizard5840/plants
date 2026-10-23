import json
def read():
    file = open("./data/plants.json", encoding="utf-8")
    plants = json.load(file)
    file.close()
    return plants

def write(plants):
    file = open("./data/plants.json", encoding="utf-8", mode="w")
    json.dump(plants, file, ensure_ascii=False, indent=4)
    file.close()
