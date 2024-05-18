import pandas as pd
import os

# 設定 CSV 文件所在的目錄
csv_dir = 'D:\講義\人工智慧概論\project\processeddata'  # 替換為你的 CSV 文件所在的實際路徑

# 獲取所有 CSV 文件的文件名
csv_files = [file for file in os.listdir(csv_dir) if file.endswith('.csv')]

# 創建一個空的 DataFrame
combined_df = pd.DataFrame()

# 逐個讀取 CSV 文件並添加到 combined_df 中
for file in csv_files:
    file_path = os.path.join(csv_dir, file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# 將合併後的 DataFrame 保存為新的 CSV 文件
combined_df.to_csv('combined_output.csv', index=False)
