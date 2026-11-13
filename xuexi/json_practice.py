import json

data = {
    "id": "chat_001",
    "title": "第一次对话",
    "messages": [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！有什么可以帮你的？"},
    ],
}

# 存
with open("test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读
with open("test.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(type(loaded))                       # dict
print(loaded["title"])                    # 第一次对话
print(loaded["messages"][0]["content"])   # 你好