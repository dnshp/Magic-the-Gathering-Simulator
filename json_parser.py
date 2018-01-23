import json
DELIMITER = ";"

csv = open("AllCards.txt", 'a')
file = open("AllCards.json", 'r')
data = json.load(file)
s = {"Enchantment"}
for card in data:
    current = data[card]
    print(current["name"])
    if current["layout"] != "token":
        types = 00000000
        if "Artifact" in current["types"]:
            types += 10000000
        if "Creature" in current["types"]:
            types += 1000000
        if "Enchantment" in current["types"]:
            types += 100000
        if "Instant" in current["types"]:
            types += 10000
        if "Land" in current["types"]:
            types += 1000
        if "Planeswalker" in current["types"]:
            types += 100
        if "Sorcery" in current["types"]:
            types += 10
        if "Tribal" in current["types"]:
            types += 1

        types = str(types)
        while len(types) < 8:
            types = "0" + types

        if "power" in current:
            power = current["power"]
            toughness = current["toughness"]
        else:
            power = "0"
            toughness = "0"

        if "manaCost" not in current:
            manaCost = "0"
        else:
            manaCost = current["manaCost"]

        if "text" in current:
            text = current["text"]
        else:
            text = ""

        csv.write(current["name"] + DELIMITER + manaCost + DELIMITER + types + DELIMITER + current["type"] + DELIMITER + power + DELIMITER + toughness + DELIMITER + text + "\n\n")
csv.close()
file.close()
