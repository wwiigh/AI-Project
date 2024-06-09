from torch.utils.data import Dataset , DataLoader
import pandas as pd
from transformers import  GPT2LMHeadModel, GPT2Tokenizer,AdamW
import json
class ReceipeDataset(Dataset):
    def __init__(self,datas, tokenizer):
        self.tokenizer = tokenizer
        self.ingredients = datas['ingredients'].values
        self.directions = datas['directions'].values
    def __len__(self):
        return len(self.ingredients)
    
    def __getitem__(self,index):
        ingredient = self.ingredients[index]
        direction = self.directions[index]
        ingredient_token = self.tokenizer.encode(ingredient , max_length = 100 , padding = "max_length" , truncation = True, return_tensors = "pt").reshape(-1)
        direction_token = self.tokenizer.encode(direction , max_length = 100 , padding = "max_length" , truncation = True, return_tensors = "pt").reshape(-1)
        return ingredient_token,direction_token
    

if __name__ == '__main__':

    with open('test.json', 'r') as file:
        data = json.load(file)

    df = pd.read_csv("test.csv")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
    tokenizer.pad_token = tokenizer.eos_token
    dset = ReceipeDataset(df,tokenizer)
    title = next(iter(DataLoader(dset , batch_size = 1,shuffle = True)))
    print(title)