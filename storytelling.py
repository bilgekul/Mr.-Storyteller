import streamlit as st
from langchain.llms.openai import OpenAI
from langchain.chains import SequentialChain, LLMChain
import os
from dotenv import load_dotenv,find_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.prompts import PromptTemplate

_ = load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(page_title="Mr StoryTeller")