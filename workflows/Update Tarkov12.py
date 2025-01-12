import json

# 讀取Tarkov.json文件
with open('Tarkov.json', 'r', encoding='utf-8') as file:
    tarkov_data = json.load(file)

# 創建Tarkov2.json的內容
tarkov2_data = {}
for index, response in enumerate(tarkov_data['responses']):
    tarkov2_data[f'故事{index + 1}'] = response

# 寫入Tarkov2.json文件
with open('Tarkov2.json', 'w', encoding='utf-8') as file:
    json.dump(tarkov2_data, file, ensure_ascii=False, indent=4)

print("Tarkov2.json已更新")