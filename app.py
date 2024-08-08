import  streamlit as st

st.title('Namaste Sahil beteh,neeche kuch type kar')
base="blue"
if "history" not in st.session_state:
    st.session_state.history=[]


for message in st.session_state.history:
    with st.chat_message(message["avatar"]):
        st.markdown(message["message"])



if prompt:=st.chat_input("type something"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.history.append({"avatar":"user","message":prompt})

    response=f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.history.append({"avatar":"assistant","message":prompt})


