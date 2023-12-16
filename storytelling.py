import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os
from dotenv import load_dotenv
import time

_ = load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
st.set_page_config(page_title="Mr.StoryTeller", page_icon="🌚")
st.title("🤖Mr.StoryTeller🌚", help=None, anchor=None)
introduction_text1 = "Hello Fellow Adventurer! I am Mr.StoryTeller Wizard Knight 🌚."
introduction_text2 = "I'll tell you the stories you imagine in your mind, hupidi wuuu 🪄."
introduction_text3 = "Please what is imagined in your mind tell me and I'll came make it true 🌈."
st.text(introduction_text1)
time.sleep(3)
st.text(introduction_text2)
time.sleep(3)
st.text(introduction_text3)
languages = ["Turkish", "English", "French", "German", "Japanese", "Korean"]
language = st.selectbox("Choose a language in which I'll tell the story ❓", languages)
st.write("Please tell words in which I'll fiction for the story ❓")
st.write("You can give only 5 words ❗and when added each word add comma.")
inputs = st.chat_input(placeholder="Gime gime words wizard 🪄.")
input_list = []
if inputs:
    input_list = inputs.split(",")
    if len(input_list) != 5:
        st.warning("Please enter exactly 5 words separated by commas.")
    else:
        llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-3.5-turbo",
            api_key=api_key,
        )
        template = ChatPromptTemplate.from_messages(
        [
        ("system", "You are a story creator, and your task is to create engaging and educational stories for preschool children."
        "The user will provide you with 5 different words, and your challenge is to craft a story using these words."
            "The story should consist of a minimum of 8000 and a maximum of 20000 words. Design the story in a way that is understandable and enjoyable for young children."),
        ("human", "{input_list}")
        ]
        )

        messages = template.format_messages(
            input_list = input_list
        )
        response = llm(template)
        st.write("Wait the story adventurer hobidi wubidi...")    
        time.sleep(10)
        st.write(response.content)


