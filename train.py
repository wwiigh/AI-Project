from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from transformers import pipeline

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

train_dataset = TextDataset(
  tokenizer=tokenizer,
  file_path="processed.csv",
  block_size=128)

data_collator = DataCollatorForLanguageModeling(
  tokenizer=tokenizer, mlm=False)

training_args = TrainingArguments(
    output_dir="./results",    # 輸出文件夾
    overwrite_output_dir=True, # 覆蓋輸出目錄
    num_train_epochs=3,        # 訓練輪數
    per_device_train_batch_size=4, # 每個設備的批次大小
    save_steps=1000,           # 保存模型的步數
    save_total_limit=2)        # 最大保存模型的數量

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset)

trainer.train()
trainer.save_model("./final_model")  # 保存模型



