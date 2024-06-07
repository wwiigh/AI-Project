import pandas as pd
import json
import csv
# df = pd.read_csv('full_dataset.csv')

df_small = pd.read_csv('data_2\\vegan_processed.csv',index_col = False)
# df_small = pd.read_csv('full_dataset.csv', nrows = 1, index_col=None)
# df_small = pd.read_csv('test.csv', nrows = 100, usecols=['ingredients'], index_col=None)

# for index, row in df_small.iterrows():
#     ingredient = row['ingredients']
#     ingredient = ingredient.replace('", "','\n')
#     ingredient = ingredient.replace('[','')
#     ingredient = ingredient.replace(']','')
#     ingredient = ingredient.replace('"','')
#     ingredient = f"Ingredients: {ingredient}.\n"
#     df_small.at[index, 'ingredients'] = ingredient

#     title = row['title']
#     # title = title.replace('[','').replace(']','').replace('"','').replace('", "','\n')
#     title = title.replace('", "','\n')
#     title = title.replace('[','')
#     title = title.replace(']','')
#     title = title.replace('"','')
#     title = f"{ingredient}Title: {title}.\n"
#     df_small.at[index, 'title'] = title
    
#     directions = row['directions']
#     print(directions)
#     # directions = directions.replace('[','').replace(']','').replace('"','').replace('", "','\n')
#     directions = directions.replace('", "','\n')
#     directions = directions.replace('[','')
#     directions = directions.replace(']','')
#     directions = directions.replace('"','')
#     directions = f"{title}Receipe: {directions}"
#     df_small.at[index, 'directions'] = directions

# df_small.to_csv('test.csv', index=False)


# ingredients = []
# titles = []
# directions = []
# with open('test.csv', 'r', newline='') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     next(csv_reader)  # 跳过标题行
#     for row in csv_reader:
#         ingredients.append(row[1])
#         titles.append(row[0])
#         directions.append(row[2])
    
# # 将数据写入 JSON 文件
# with open('test.json', 'w') as jsonfile:
#     json.dump({'ingredients': ingredients,'titles': titles,'directions': directions}, jsonfile, ensure_ascii=False, indent=4)


# # df_small.to_csv('test-origin-data.csv', index=False)