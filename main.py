import os
from dotenv import load_dotenv
import streamlit as st

# 1. Load the .env file
load_dotenv()

# 2. Get the values and store them in local variables
# This satisfies Pylance because 'api_key' is clearly defined now
api_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

# 3. Validation Check
if not api_key or not serper_key:
    st.error("🚨 Missing API Keys in .env file!")
    st.stop()

# 4. Set the environment variables for CrewAI to find
os.environ["GEMINI_API_KEY"] = api_key
os.environ["SERPER_API_KEY"] = serper_key