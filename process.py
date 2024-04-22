import pandas as pd
import json

df = pd.read_csv('dataaa')
def parse_json_column(column):
    return column.apply(json.loads)
df['ingredients'] = parse_json_column(df['ingredients'])
df['directions'] = parse_json_column(df['directions'])
df['ingredients'] = df['ingredients'].apply(lambda x: '\n'.join(x).lower())
df['directions'] = df['directions'].apply(lambda x: '\n'.join(x).lower())
df['full_recipe'] = "Title:\n" + df['title'] + "\n\nIngredients:\n" + df['ingredients'] + "\n\nDirections:\n" + df['directions']
print(df['full_recipe'].head())
print(df['full_recipe'][0])

df['full_recipe'].to_csv('processed.csv', index=False)