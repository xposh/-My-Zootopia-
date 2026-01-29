import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    # Name prüfen und ausgeben
    if "name" in animal:
        print(f"Name: {animal['name']}")

    #Diet prüfen und Achtung! *(liegt innerhalb von 'characteristics')
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print(f"Diet: {animal['characteristics']['diet']}") #<--- *

    #Location prüfen *(erstes Element der Liste 'locations')
    if "locations" in animal and len(animal["locations"]) > 0:
        print(f"Location: {animal['locations'][0]}") #* [0] = erstes Element

    #Type prüfen (liegt auch in 'characteristics')
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print(f"Type: {animal['characteristics']['type']}")
