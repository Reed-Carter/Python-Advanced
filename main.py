from typing import ByteString
from faker import Faker
import json

fake = Faker()
color_list = []

for i in range(20):
  color_names = (fake.color_name())
  color_list.append(color_names)

def remove_dups(list_with_dups):
  no_dups = []
  [no_dups.append(color) for color in list_with_dups if color not in no_dups]
  return "".join(no_dups) if isinstance(list_with_dups, str) else no_dups

color_list_no_dups = remove_dups(color_list)
color_dict = {color: len(color) for color in color_list_no_dups}

with open("./data/colors.json", "w+") as json_colors:
  json.dump(color_dict, json_colors)

with open("./data/colors.json", "r") as json_colors_short:
  colors_short = json.load(json_colors_short)
  print(colors_short)
  for key, value in colors_short.items():
    if len(key) >= 4:
      print(f" The color {key} has {len(key)} letters in its name")



