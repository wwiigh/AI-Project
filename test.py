
from transformers import pipeline

generator = pipeline('text-generation', model='./final_model', tokenizer='gpt2')

recipes = generator("chocolate cookie", max_length=400)
print(recipes[0]['generated_text'])