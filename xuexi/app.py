import os
import streamlit as st
from openai import OpenAI
from pathlib import Path
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="AI 助手", page_icon="🤖", layout="wide")

DATA_FILE = Path("data/chats.json")

# ===== 0. 检查 key =====
if not os.environ.get("DEEPSEEK_API_KEY"):
    st.error("没找到 DEEPSEEK_API_KEY，先在 PowerShell 里设置环境变量，再重启 streamlit")
    st.stop()

# ===== 1. 客户端只建一次 =====
@st.cache_resource
def get_client():
    return OpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"],
        base_url="https://api.deepseek.com",
    )

client = get_client()


# ===== 2.人设配置 =====
if "nickname" not in st.session_state:
    st.session_state.nickname = "小助手"
if "persona" not in st.session_state:
    st.session_state.persona = "你是一个简洁、直接的中文助手，回答不超过三句话。"

def build_system_prompt():
    nick = (st.session_state.nickname or "").strip() or "助手"
    persona = (st.session_state.persona or "").strip() or "你是一个有帮助的助手。"
    return f"你的名字是{nick}。{persona}"

# ===== 3. 历史放在 session_state 里 =====
def new_conversation():
    now = datetime.now()
    return {
        "id": now.strftime("%Y%m%d_%H%M%S%f"),
        "title": "新对话",
        "created_at": now.strftime("%Y-%m-%d %H:%M"),
        "messages": [{"role": "system", "content": build_system_prompt()}],
    }


def load_conversations():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # 只保留有内容的对话，顺手清掉历史遗留的空对话
        useful = [c for c in data if len(c.get("messages", [])) > 1]
        if data:
            return data
    return [new_conversation()]


def save_conversations():
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.conversations, f, ensure_ascii=False, indent=2)


def current_conv():
    for c in st.session_state.conversations:
        if c["id"] == st.session_state.current_id:
            return c
    st.session_state.current_id = st.session_state.conversations[0]["id"]
    return st.session_state.conversations[0]

def is_empty(conv):
    """只有 system 一条，说明用户还没说过话"""
    return len(conv["messages"]) <= 1

# ===== 4. 初始化 =====
if "conversations" not in st.session_state:
    st.session_state.conversations = load_conversations()
    st.session_state.current_id = st.session_state.conversations[0]["id"]

# ===== 5. 侧边栏 =====
with st.sidebar:
    st.title("对话")

    if st.button("+ 新建对话", use_container_width=True):
        if is_empty(current_conv()):
            st.toast("当前已经是新对话了，先聊点什么吧")
        else:
            conv = new_conversation()
            st.session_state.conversations.insert(0, conv)
            st.session_state.current_id = conv["id"]
            save_conversations()
            st.rerun()

    for item in st.session_state.conversations:
        is_current = item["id"] == st.session_state.current_id
        col_text, col_del = st.columns([5, 1], vertical_alignment="center")

        with col_text:
            label = ("● " if is_current else "") + item["title"]
            if st.button(label, key=f"conv_{item['id']}", use_container_width=True):
                st.session_state.current_id = item["id"]
                st.rerun()

        with col_del:
            if st.button("✕", key=f"del_{item['id']}", use_container_width=True):
                st.session_state.conversations = [
                    c for c in st.session_state.conversations if c["id"] != item["id"]
                ]
                # 删光了就补一条新的
                if not st.session_state.conversations:
                    st.session_state.conversations = [new_conversation()]
                # 删的正好是当前这条，就切到第一条
                if st.session_state.current_id == item["id"]:
                    st.session_state.current_id = st.session_state.conversations[0]["id"]
                save_conversations()
                st.toast("已删除")
                st.rerun()

    st.divider()

    st.subheader("人设配置")
    st.text_input("昵称", key="nickname")
    st.text_area("性格", key="persona", height=110)

    st.caption(f"共 {len(st.session_state.conversations)} 个对话")

# ===== 6. 主区：把历史画出来 =====
conv = current_conv()
messages = conv["messages"]

st.title(conv["title"])

for msg in messages[1:]:   # 跳过 system
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ===== 7. 输入框 + 调 API =====
user_input = st.chat_input("问点什么…")

if user_input:

    messages[0] = {"role": "system", "content": build_system_prompt()}
    messages.append({"role": "user", "content": user_input})

    save_conversations()

    with st.chat_message("user"):
        st.write(user_input)

    # 再问模型，画它的回答
    with st.chat_message("assistant"):
        usage_note = None
        with st.spinner("思考中…"):
            try:
                stream = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stream=True,
                    stream_options={"include_usage": True},
                )
                placeholder = st.empty()
                full = ""
                u = None
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        full += chunk.choices[0].delta.content
                        placeholder.markdown(full + "▌")
                    if getattr(chunk, "usage", None):
                        u = chunk.usage

                placeholder.markdown(full)
                reply = full
                if u:
                    usage_note = f"输入 {u.prompt_tokens} tokens / 输出 {u.completion_tokens} tokens"

            except Exception as e:
                s = str(e)
                if "401" in s or "Unauthorized" in s:
                    reply = "API Key 无效，检查一下环境A变量"
                elif "402" in s or "Insufficient" in s:
                    reply = "余额不足，去 platform.deepseek.com 充值"
                elif "timeout" in s.lower() or "Connection" in s:
                    reply = "网络连不上，检查一下能不能访问 api.deepseek.com"
                else:
                    reply = f"出错了：{s}"
                st.write(reply)

        if usage_note:
            st.caption(usage_note)

    messages.append({"role": "assistant", "content": reply})
    save_conversations()