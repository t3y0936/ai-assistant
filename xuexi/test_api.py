import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
)

messages = [{"role": "system", "content": "你是明日方舟游戏里罗德岛的领袖阿米娅，需要称呼用户为博士"}]

while True:
    text = input("你：")
    if text == "exit":
        break

    messages.append({"role": "user", "content": text})

    response = client.chat.completions.create(model="deepseek-chat", messages=messages)
    reply = response.choices[0].message.content
    print("AI：", reply)

    messages.append({"role": "assistant", "content": reply})