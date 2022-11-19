from faker import Faker
import json

fake = Faker()
color_list = []
color_list_no_dups = []

for i in range(20):
  color_names = (fake.color_name())
  color_list.append(color_names)

def remove_dups(list_of_colors):
  [color_list_no_dups.append(color) for color in list_of_colors if color not in color_list_no_dups]

remove_dups(color_list)
color_dict = {color: len(color) for color in color_list_no_dups}

with open("./data/colors.json", "w+") as json_colors:
  json.dump(color_dict, json_colors)

with open("./data/colors.json", "r") as json_colors_short:
  colors_short = json.load(json_colors_short)
  print(colors_short)
  for key, value in colors_short.items():
    if len(key) >= 4:
      print(f" The color {key} has {len(key)} letters in its name")