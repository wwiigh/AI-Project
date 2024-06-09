
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments, pipeline

# 加載模型和分詞器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# 讀取整個文本文件
df = pd.read_csv("processed.csv", header=None)  # 假設文本數據沒有列標頭
data = df[0].tolist()  # 將數據列轉換為列表

# 切割數據為訓練集和驗證集
train_texts, valid_texts = train_test_split(data, test_size=0.1, random_state=42)  # 90%訓練，10%驗證

# 保存訓練集和驗證集數據到文件（為了使用 TextDataset）
with open('train_dataset.txt', 'w', encoding='utf-8') as f:
    for text in train_texts:
        f.write(text + '\n')

with open('valid_dataset.txt', 'w', encoding='utf-8') as f:
    for text in valid_texts:
        f.write(text + '\n')

# 創建 TextDataset 對象
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="train_dataset.txt",
    block_size=128
)

valid_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="valid_dataset.txt",
    block_size=128
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

# 訓練參數設定，包括早停
training_args = TrainingArguments(
    output_dir="./results",              # 輸出文件夾
    overwrite_output_dir=True,           # 覆蓋輸出目錄
    num_train_epochs=7,                 # 訓練輪數增加為10
    per_device_train_batch_size=4,       # 每個設備的批次大小
    save_steps=1000,                     # 保存模型的步數
    save_total_limit=2,                  # 最大保存模型的數量
    evaluation_strategy="steps",         # 在訓練過程中進行評估
    eval_steps=250,                      # 每500步進行一次評估
    load_best_model_at_end=True,         # 訓練結束時加載最佳模型
    metric_for_best_model="loss",        # 以損失為最佳模型指標
    greater_is_better=False              # 指標是越小越好
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset           # 設置驗證集
)

# 開始訓練
trainer.train()

# 保存最佳模型
trainer.save_model("./final_model")


