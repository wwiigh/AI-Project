from transformers import pipeline

generator = pipeline('text-generation', model='./final_model', tokenizer='gpt2')

recipes = generator("Use:\nchocolate\nflour\nmilk\neggs\n\nTitle:\nchocolate cake\n", max_length=200)
print(recipes[0]['generated_text'])