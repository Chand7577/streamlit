import streamlit as st
from openai import OpenAI

st.title('BOT LIKE CHATGPT(Detroit)')

client = OpenAI( 
    api_key="25ed35d2f1a94c5290e4004c4366a403",
    base_url="https://api.aimlapi.com",)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "mistralai/Mistral-7B-Instruct-v0.2"


if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    with st.chat_message(message["avatar"]):
        st.markdown(message["message"])


if prompt := st.chat_input("type something"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.history.append({"avatar": "user", "message": prompt})

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["avatar"], "content": m["message"]}
                for m in st.session_state.history
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.history.append({"avatar": "assistant", "message": prompt})

