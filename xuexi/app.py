from openai import OpenAI
import os
import streamlit as st

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

text = st.text_input("问点什么：")
if st.button("发送") and text:
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": text}],
    )
    st.write(resp.choices[0].message.content)