import pytorch_lightning as pl
from torch.utils.data import DataLoader
from ReceipeDataset import ReceipeDataset
from transformers import AdamW
class DataModule(pl.LightningDataModule):
    def __init__(self,x_train,x_test, tokenizer):
        super().__init__()
        self.train = ReceipeDataset(x_train,tokenizer)
        self.test = ReceipeDataset(x_test,tokenizer)
        self.val = ReceipeDataset(x_test,tokenizer)
    
    def train_dataloader(self):
        return DataLoader(self.train , batch_size = 1 , shuffle = True)
    def test_dataloader(self):
        return DataLoader(self.test , batch_size = 1 , shuffle = False)
    def val_dataloader(self):
        return DataLoader(self.val , batch_size = 1 , shuffle = False)
    
class Model(pl.LightningModule):
    def __init__(self, model):
        super().__init__()
        model.train()
        self.model = model
        
    def forward(self,x):
        # print(x)
        return self.model(x[0] , labels = x[1])
    
    def configure_optimizers(self):
        return AdamW(self.parameters(), 1e-4)
        
    def training_step(self,batch,batch_idx):
        x= batch
        output = self(x)
        return output.loss
    
    def test_step(self,batch,batch_idx):
        x= batch
        output = self(x)
        return output.loss
    
    def validation_step(self,batch,batch_idx):
        x= batch
        output = self(x)
        return output.loss