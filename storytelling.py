import streamlit as st
from streamlit import spinner
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio
import os
import time



_ = load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
st.set_page_config(page_title="Mr.StoryTeller", page_icon="🌚")
st.title("🤖Mr.StoryTeller🌚", help=None, anchor=None)
introduction_text1 = "Hello Fellow Adventurer! I am Mr.StoryTeller Wizard Knight 🌚."
introduction_text2 = "I'll tell you the stories you imagine in your mind, hupidi wuuu 🪄."
introduction_text3 = "Please what is imagined in your mind tell me and I'll come make it true 🌈."
st.text(introduction_text1)
time.sleep(3)
st.text(introduction_text2)
time.sleep(3)
st.text(introduction_text3)
languages = ["English","Turkish","French","German","Japanese","Korean"]
language = st.selectbox("Choose a language in which I'll tell the story ❓", languages)
st.write("Please tell words in which I'll fiction for the story ❓")
st.write("You can give only 5 words ❗and when added each word add a comma.")
inputs = st.text_input(label="we'll make a magic with you", placeholder="Gime gime words wizard 🪄.")
input_words = {}
if inputs:
    input_words = {"input_words": inputs.split(",")}
    if len(input_words["input_words"]) != 5:
        st.warning("Please enter exactly 5 words separated by commas.")
    else:
        llm = OpenAI(
            temperature=0.3,
            model="text-davinci-003",
            api_key=api_key,
            max_tokens = 2000
        )
        prompt_template = PromptTemplate(
            input_variables=['input_words', 'language'],
            template="You are a story creator, and your task is to create engaging and educational stories for preschool children. "
                    "The user has provided you with 5 different words in python dict: {input_words}. "
                    "Your challenge is to craft a story using these words. "
                    "The story should consist of a minimum of 8000 and a maximum of 10000 words. "
                    "Design the story in a way that is understandable and enjoyable for young children. "
                    "Create the story in the selected language: {language}"
        )
        lang_codes = {"English":"en","Turkish":"tr","French":"fr","Japanese":"ja","Korean":"ko"}
        with spinner("Hobidi wubidi...🌈"):
            time.sleep(3)
            chain = LLMChain(llm=llm, prompt=prompt_template)
            response = chain.run({**input_words, 'language': language})
        st.write(response)
        time.sleep(10)
        with spinner("I'll voice the story for you, wait a minute, captain...🪄"):
            time.sleep(10)
            tts = gTTS(text=response, lang=lang_codes[language], slow=False)
            audio_bytes_io = BytesIO()
            tts.save("temp.mp3")
            with open("temp.mp3", "rb") as f:
                audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3")











