import streamlit as st
from openai import OpenAI
import os
import openai

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key="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")
# os.environ.get("OPENAI_API_KEY")

st.title("What to talk about something? Let me know...")

#create a chat history list
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#display messages on app rerun
for message in st.session_state.messages:
    print(type(message))
    print(message)
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
#initialize the model
if "model" not in st.session_state:
    st.session_state.model = "gpt-3.5-turbo"

#user input    
if user_input := st.chat_input("Your input"):
    #display user message
    with st.chat_message("user"):
        st.markdown(user_input)
        
    #add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
 
    #display and store openai responses   
    with st.chat_message("assistant"):
        message_placehodler = st.empty()
        
    #     response = client.ChatCompletion.create(
    #         model=st.session_state.model,
    #         messages = [
    #             {"role": m['role'], "content": m['content']}
    #             for m in st.session_state.messages
    #         ]
    #     )
    #     message_placehodler.markdown(response.choices[0].message.content)
        
    # st.session_state.messages.append({"role": "assistant", "content": response})
    
        stream = client.chat.completions.create(
            model=st.session_state.model,
            messages = [
                {"role": m['role'], "content": m['content']}
                for m in st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
    