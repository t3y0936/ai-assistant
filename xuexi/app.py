import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI 助手", page_icon="🤖", layout="wide")

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

# ===== 2. 历史放在 session_state 里 =====
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": build_system_prompt()}]

# ===== 3. 侧边栏 =====
with st.sidebar:
    st.title("对话")
    if st.button("+ 新建对话", use_container_width=True):
        st.session_state.messages = [{"role": "system", "content": build_system_prompt()}]
        st.rerun()

    st.divider()

    st.subheader("人设配置")
    st.text_input("昵称", key="nickname")
    st.text_area("性格", key="persona", height=110)

    st.caption(f"当前 {len(st.session_state.messages) - 1} 条消息")

# ===== 4. 主区：把历史画出来 =====
st.title("AI 助手")

for msg in st.session_state.messages[1:]:   # 跳过 system
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ===== 5. 输入框 + 调 API =====
user_input = st.chat_input("问点什么…")

if user_input:
    # 用当前设置刷新 system，而不是用历史里那个旧的
    st.session_state.messages[0] = {"role": "system", "content": build_system_prompt()}
    # 先存用户的话，再画出来
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 再问模型，画它的回答
    with st.chat_message("assistant"):
        usage_note = None
        with st.spinner("思考中…"):
            try:
                stream = client.chat.completions.create(  # ← 改动①
                    model="deepseek-chat",
                    messages=st.session_state.messages,
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
                    reply = "API Key 无效，检查一下环境变量"
                elif "402" in s or "Insufficient" in s:
                    reply = "余额不足，去 platform.deepseek.com 充值"
                elif "timeout" in s.lower() or "Connection" in s:
                    reply = "网络连不上，检查一下能不能访问 api.deepseek.com"
                else:
                    reply = f"出错了：{s}"
                st.write(reply)

        if usage_note:
            st.caption(usage_note)

    st.session_state.messages.append({"role": "assistant", "content": reply})