import pandas as pd
import json
import re

test = ["a bottle of milk\nthree hundred grams cheese\n1.5 pound flour\na l of boiling water\n1/2 tsp. coca powder\n4 tablespoon of honey"]

number = r'(a|\d+\s*\d+/\d+|\d+/\d+|\d+\.\d+|\d+)'
text_numbers = r'(a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)'
tens = r'(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)'
large = r'(hundred|thousand)'
common = r'(c[\.]?|cup[s]?|tsp[\.]?|teaspoon[s]?|tbsp[\.]?|tablespoon[s]?|g[\.]?|gram[s]?|kg[\.]?|kilogram[s]?|ml[\.]?|milliliter[s]?|l[\.]?|liter[s]?)'
en = r'(oz[\.]|ounce[s]?|fl[\.]?\s*oz[\.]?|fluid\s*ounce[s]?|fluid\s*oz[\.]?|fl[\.]?\s*ounce[s]?|lb[\.]?|pound[s]?|pt[\.]?|pint[s]?|qt[\.]?|quart[s]?)'
amount = r'(pkt[\.]?|packet[s]?|pack[s]?|pkg[\.]?|package[s]?|can[s]?|tin[s]?|stk[\.]?|stick[s]?|carton[s]?|box[s]?|jar[s]?|bottle[s]?|bag[s]?|pouch[es]?)'
few =r'(catty|catties|bunch[es]?|chunk[s]?|slice[s]?|piece[s]?|clove[s]?|pinch|dash|handful|jigger[s]?|sachet[s]?|tube[s]?)'
unit_pattern = rf'\(({number}|{text_numbers}(?:\s*{large})?|{tens}(?:-{text_numbers})?(?:\s*{large})?)\s*({common}|{en}|{amount}|{few})\)\s*'
test = [re.sub(unit_pattern, '', ingredient).strip() for ingredient in test]
unit_pattern = rf'\b({number}|{text_numbers}(?:\s*{large})?|{tens}(?:-{text_numbers})?(?:\s*{large})?)\b\s+?'
test = [re.sub(unit_pattern, '', ingredient).strip() for ingredient in test]
unit_pattern = rf'\b({common}|{en}|{amount}|{few})\s+(\bof\s+)?'
test = [re.sub(unit_pattern, '', ingredient).strip() for ingredient in test]

print(test)