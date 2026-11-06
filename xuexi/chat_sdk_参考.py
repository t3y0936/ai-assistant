

import os
from openai import OpenAI

# ---------- CONFIG：只改这里 ----------
USE_LOCAL = True

if USE_LOCAL:
    client = OpenAI(
        api_key="ollama",                            # 本地随便填
        base_url="http://127.0.0.1:11434/v1",        # Ollama 的 OpenAI 兼容端点
    )
    MODEL = "qwen2.5:3b"
else:
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY", ""),
        base_url="https://api.deepseek.com",         # DeepSeek 官方
    )
    MODEL = "deepseek-chat"
# --------------------------------------


def ask(messages):
    """发一次对话，返回 (回答文本, 用量对象)。出错返回 (None, None)。"""
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=False,
        )
    except Exception as e:                 # SDK 的各种异常统一先接住，打印出来
        print("【调用失败】", type(e).__name__, e)
        return None, None

    return resp.choices[0].message.content, resp.usage


def main():
    messages = [
        {"role": "system", "content": "你是一个简洁的助手，每次回答不超过 50 个字。"}
    ]

    print(f"=== openai SDK 多轮对话（模型：{MODEL}）===")
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

        reply, usage = ask(messages)
        if reply is None:
            messages.pop()
            continue

        print("AI：", reply)
        messages.append({"role": "assistant", "content": reply})

        if usage:
            print(f"     [本次 token：输入 {usage.prompt_tokens} / 输出 {usage.completion_tokens}，"
                  f"历史 {len(messages)} 条]\n")
        else:
            print()


if __name__ == "__main__":
    main()
