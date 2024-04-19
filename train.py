from transformers import  GPT2LMHeadModel, GPT2Tokenizer,AdamW
import pandas as pd
from torch.utils.data import Dataset , DataLoader
import pytorch_lightning as pl
from sklearn.model_selection import train_test_split
from pytorch_lightning import Trainer
from model import Model,DataModule

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium", cache_dir="./cache/gpt2token", padding_side='left')
gpt2 = GPT2LMHeadModel.from_pretrained("gpt2-medium", cache_dir="./cache/gpt2model")
tokenizer.pad_token = tokenizer.eos_token

df = pd.read_csv("test.csv")
x_train , x_test = train_test_split(df, test_size = 0.3 , random_state = 42)


model = Model(gpt2)
module = DataModule(x_train , x_test,tokenizer)
trainer = Trainer(max_epochs = 8)
trainer.gpus = 1

trainer.fit(model,module)


gpt2.state_dict = model.state_dict
raw_text = ["Ingredients: milk. Recipe:" ,"Ingredients: 1 box powdered sugar 8 oz. Recipe:"  , "Ingredients: 1 box yellow cake mix 2 eggs 1/3 c. soft margarine 1 can Eagle Brand milk 1 c. pecans 1/2 c. Bits 'O Brickle. Recipe:" , "Ingredients: 1 can Spanish rice 1 can corned beef 1 diced onion 1/2 c. grated Cheddar cheese. Recipe:"]
output_text = []
for x in raw_text:
    prompt = tokenizer.encode(x, return_tensors = "pt")
    output = gpt2.generate(prompt,do_sample = True, max_length = 400,top_k = 10, temperature = 0.8,pad_token_id=tokenizer.pad_token_id)
    output_text.append(tokenizer.decode(output[0] , skip_special_tokens = True))

for t in output_text:
  print(t)