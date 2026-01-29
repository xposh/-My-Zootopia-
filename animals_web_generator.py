import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
output = ""

for animal in animals_data:
    output += '<li class="cards__item">'
    # Name prüfen und ausgeben
    if "name" in animal:
        output += f"  <div class='card__title'>{animal['name']}</div>\n"

    output += '  <p class="card__text">\n'

    #Diet prüfen und Achtung! *(liegt innerhalb von 'characteristics')
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n" #<--- *

    #Location prüfen *(erstes Element der Liste 'locations')
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n" #* [0] = erstes Element

    #Type prüfen (liegt auch in 'characteristics')
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output += '</li>\n'



print(output)

with open("animals_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html_content)