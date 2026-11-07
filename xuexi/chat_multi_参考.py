# -*- coding: utf-8 -*-
r"""
chat_multi.py 参考实现（板块⑤ 96-99）

用的是「OpenAI 兼容格式」——也就是 DeepSeek 官方 API 用的那套格式。
好处：同一份代码，改 3 个变量就能在「本地 Ollama」和「DeepSeek 云端」之间切换。

本地（免费、不用联网、随便试）：
    USE_LOCAL = True  →  http://127.0.0.1:11434/v1/chat/completions

云端（要 key、要余额、效果更好）：
    USE_LOCAL = False →  https://api.deepseek.com/chat/completions
    并设置环境变量 DEEPSEEK_API_KEY
"""

import os
import requests

# ---------- 只改这一块 ----------
USE_LOCAL = True

if USE_LOCAL:
    BASE_URL = "http://127.0.0.1:11434/v1"
    MODEL = "qwen2.5:3b"
    API_KEY = "ollama"                      # 本地不需要真 key，随便填
else:
    BASE_URL = "https://api.deepseek.com"
    MODEL = "deepseek-chat"
    API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")   # 从环境变量读，绝不写死在代码里

URL = BASE_URL.rstrip("/") + "/chat/completions"
# --------------------------------


def chat(messages, model=MODEL):
    """发一次对话请求，返回模型的回答字符串；出错返回 None。"""
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        resp = requests.post(URL, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("【错误】连不上服务器。本地模式检查 Ollama 有没有在跑")
        return None
    except requests.exceptions.Timeout:
        print("【错误】等了 120 秒还没回")
        return None
    except requests.exceptions.HTTPError as e:
        print("【错误】状态码异常：", e)
        print("       返回：", resp.text[:300])
        return None

    data = resp.json()
    # OpenAI 兼容格式：答案是 choices[0].message.content
    return data["choices"][0]["message"]["content"]


def main():
    messages = [
        {"role": "system", "content": "你是一个简洁的助手，每次回答不超过 50 个字。"}
    ]

    print(f"=== 多轮对话（模型：{MODEL}）===")
    print("连续问：我叫小明 / 我喜欢打篮球 / 我刚才说了什么")
    print("输入 exit 退出\n")

    while True:
        user_input = input("你：").strip()

        if user_input == "":
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            print("再见。")
            break

        messages.append({"role": "user", "content": user_input})

        reply = chat(messages)
        if reply is None:
            messages.pop()          # 失败就撤回，历史里不留没回答的问题
            continue

        print("AI：", reply)
        messages.append({"role": "assistant", "content": reply})
        print(f"     [历史 {len(messages)} 条]\n")


if __name__ == "__main__":
    main()
