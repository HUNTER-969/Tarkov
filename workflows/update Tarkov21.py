import json

# 讀取Tarkov2.json文件
with open('Tarkov2.json', 'r', encoding='utf-8') as file:
    tarkov2_data = json.load(file)

# 創建Tarkov.json的內容
tarkov_data = {'responses': []}
for key in sorted(tarkov2_data.keys(), key=lambda x: int(x[2:])):
    tarkov_data['responses'].append(tarkov2_data[key])

# 寫入Tarkov.json文件
with open('Tarkov.json', 'w', encoding='utf-8') as file:
    json.dump(tarkov_data, file, ensure_ascii=False, indent=4)

print("Tarkov.json已更新")
