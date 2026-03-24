import os
from dotenv import load_dotenv
import streamlit as st
st.write("DEBUG 1: Script started") # Add this

load_dotenv()
st.write("DEBUG 2: Dotenv loaded") # Add this

api_key = os.getenv("GEMINI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

st.write(f"DEBUG 3: Keys found? API: {bool(api_key)}, Serper: {bool(serper_key)}") # Add this

if not api_key or not serper_key:
    st.error("🚨 Missing API Keys in .env file!")
    st.stop()

st.write("DEBUG 4: Past the stop point") # Add this

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
os.environ["GOOGLE_API_KEY"] = api_key
os.environ["SERPER_API_KEY"] = serper_key

st.title("⚽ Sports Planner AI")
st.header("Ready to Plan!")

# This is where you bring in your other files
try:
    from agents import SportsAgents
    from tasks import SportsTasks
    from crewai import Crew

    st.success("Agents and Tasks loaded successfully!")
    
    # Simple input to test the UI
    user_input = st.text_input("Enter a sports event to plan:")
    
    if st.button("Start Planning"):
        st.info(f"Starting plan for: {user_input}...")
        # Your CrewAI logic will go here
except ImportError:
    st.warning("⚠️ Could not find agents.py or tasks.py in this folder.")