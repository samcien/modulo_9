import requests

#  1 - Código para los planetas y su clima

resp_1 = requests.get("https://swapi.dev/api/films/")
data_1 = resp_1.json()
count = 0

for result in data_1["results"]:
    for planet in result["planets"]:
        r = requests.get(planet)
        d = r.json()
        if d["climate"] == "arid":
            #  print(d["name"] + " " + d["climate"])
            count = count + 1
        else:
            pass
    #  print("found 1 movie")
    #  print(result["planets"])
    #  print(result["title"], result["episode_id"])
    #  print(result["planets"])

print("Movies with planets with an arid climate: " + str(count))


#  2 - Código pa los frenes wookies
count_2 = 0

resp_2 = requests.get("https://swapi.dev/api/films/6/")
data_2 = resp_2.json()

for character in data_2["characters"]:
    r = requests.get(character)
    d = r.json()
    for species in d["species"]:
        r1 = requests.get(species)
        d1 = r1.json()
        if d1["name"] == "Wookie":
            count_2 = count_2 + 1
            #  print(d1["name"])

print("(Named) Wookies in the 6th movie: " + str(count_2))


#  3 - Código para determinar la nave más grande

url_array = ["https://swapi.dev/api/starships/?page=1", "https://swapi.dev/api/starships/?page=2",
             "https://swapi.dev/api/starships/?page=3", "https://swapi.dev/api/starships/?page=4"]

ref_length = 0.0
biggest_ship = {'name': "null", 'size': 0.0}


for i in range(0, 4):
    resp = requests.get(url_array[i])
    data = resp.json()

    for result in data["results"]:
        #  print("Name: " + result["name"], "/ " + "Length: " + result["length"] + " m")
        new_length = result["length"].replace(",", "")  # le quitamos la coma al numero, si no se guilla python
        if float(new_length) > ref_length:
            ref_length = float(new_length)
            biggest_ship = {'name': result["name"], 'size': new_length}
        else:
            pass

print("Biggest ship: " + biggest_ship['name'] + "; Size: " + biggest_ship['size'] + " m")
