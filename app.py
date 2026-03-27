import streamlit as st
import os
import sys
import re
from datetime import datetime

# 1. Path Setup
sys.path.append(os.path.dirname(__file__))

# 2. Modern UI Config
st.set_page_config(
    page_title="DeepSeek Sports Analyst", 
    page_icon="🏏", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN NEUBRUNCHISM + GLASS UI (2024 EDITION) ---
st.markdown("""
    <style>
    /* Import Modern Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&display=swap');
    
    /* Global Reset & Base */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Animated Gradient Background */
    [data-testid="stAppViewMain"] {
        background: linear-gradient(-45deg, #0a0c10, #111827, #0f172a, #1e1b4b);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Modern Glass Cards with Border Animation */
    [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: rgba(17, 25, 40, 0.75) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border-radius: 28px !important;
        border: 1px solid rgba(255, 255, 255, 0.125) !important;
        padding: 2rem !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.05) inset !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    
    [data-testid="stVerticalBlock"] > div:has(div.stMarkdown):hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1) inset !important;
    }
    
    /* Sleek Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(10, 14, 23, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.3) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    /* Modern Input Fields */
    div[data-baseweb="input"] {
        border-radius: 16px !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-baseweb="input"]:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    }
    
    .stTextInput input {
        background: transparent !important;
        color: #f1f5f9 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1rem !important;
    }
    
    /* Gradient Button */
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6) !important;
        border: none !important;
        color: white !important;
        border-radius: 40px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4) !important;
        background: linear-gradient(135deg, #2563eb, #7c3aed) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Status Widget */
    [data-testid="stStatusWidget"] {
        background: rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Typography */
    h1 {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #f0f9ff, #e2e8f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.02em !important;
    }
    
    h2, h3 {
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
        background: linear-gradient(135deg, #f1f5f9, #cbd5e1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Status Messages */
    .stAlert {
        background: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
    }
    
    /* Divider Styling */
    hr {
        margin: 2rem 0 !important;
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent) !important;
    }
    
    /* Caption Styling */
    .stCaption, caption {
        color: #94a3b8 !important;
        font-size: 0.85rem !important;
    }
    
    /* Chat Message Styling */
    [data-testid="stChatMessage"] {
        background: rgba(30, 41, 59, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(59, 130, 246, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(59, 130, 246, 0.8);
    }
    
    /* Metrics/Label Styling */
    .stMetric {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 20px !important;
        padding: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 16px;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6) !important;
        color: white !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Stable Imports
try:
    from crewai import Crew, Process
    from agents import planner_agent, analyst_agent, reporter_agent
    from tasks import create_tasks
except Exception as e:
    st.error(f"Environment Error: {e}")
    st.stop()

# --- THE CLEAN CALLBACK ---
def streamlit_callback(step_output):
    raw_text = str(step_output)
    if "Failed to parse" in raw_text:
        return

    with st.chat_message("ai", avatar="🤖"):
        thought = re.search(r"thought=['\"](.*?)['\"]", raw_text, re.DOTALL)
        output = re.search(r"output=['\"](.*?)['\"]", raw_text, re.DOTALL)
        
        if thought:
            clean_thought = thought.group(1).replace('\\n', '\n').strip()
            if clean_thought:
                st.markdown(f"#### 🔍 Strategy\n{clean_thought}")

        if output:
            clean_output = output.group(1).replace('\\n', '\n').strip()
            if clean_output not in ["{}", "{", "None", ""]:
                st.markdown("---")
                st.markdown(f"#### ✅ Findings\n{clean_output}")

# --- MODERN UI CONTENT ---
# Hero Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0 2rem 0;'>
            <span style='font-size: 4rem;'>🏏</span>
            <h1 style='margin-top: 0.5rem;'>Sports Intelligence</h1>
            <p style='color: #94a3b8; font-size: 1.1rem;'>Powered by DeepSeek-R1 • Real-time Analysis • Agentic Workflow</p>
        </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    # Modern Sidebar Header
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0 1.5rem 0;'>
            <span style='font-size: 2rem;'>⚙️</span>
            <h3 style='margin-top: 0.5rem;'>System Control</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # API Key Input with icon
    st.markdown("#### 🔑 API Configuration")
    serper_key = st.text_input("Serper API Key", value="HIDDEN", type="password", 
                               help="Enter your Serper API key for web search capabilities")
    os.environ["SERPER_API_KEY"] = serper_key
    
    st.markdown("---")
    
    # System Stats in a modern card
    st.markdown("#### 📊 System Status")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Active Agents", "3", delta=None)
    with col_b:
        st.metric("Model", "8B", delta=None)
    
    st.markdown("---")
    
    # Feature list
    st.markdown("#### ✨ Features")
    st.markdown("""
        - 🧠 Multi-Agent Collaboration
        - 🔍 Real-time Web Search
        - 📈 Advanced Analytics
        - 🤖 DeepSeek-R1 Powered
        - 🎯 Strategic Insights
    """)
    
    st.markdown("---")
    st.caption("Built with CrewAI • Streamlit • DeepSeek")

# Main Interaction Area
with st.container():
    # Modern Input Section
    st.markdown("""
        <div style='margin-bottom: 1rem;'>
            <h3>🎯 Analysis Request</h3>
            <p style='color: #94a3b8;'>Describe what you want to analyze in detail</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    with col1:
        user_goal = st.text_input("", placeholder="e.g., Analyze India's batting performance in T20 World Cup 2024, focusing on strike rates and partnership patterns", 
                                  label_visibility="collapsed")
    with col2:
        st.markdown("<div style='height: 0.25rem;'></div>", unsafe_allow_html=True)
        execute = st.button("🚀 Analyze Now", use_container_width=True)

# --- EXECUTION ---
if execute:
    if not user_goal:
        st.warning("Please enter a goal first.")
    else:
        planner_agent.step_callback = streamlit_callback
        analyst_agent.step_callback = streamlit_callback
        reporter_agent.step_callback = streamlit_callback

        with st.status("🧠 Orchestrating Agents...", expanded=True) as status:
            try:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                my_tasks = create_tasks(planner_agent, analyst_agent, reporter_agent)
                
                sports_crew = Crew(
                    agents=[planner_agent, analyst_agent, reporter_agent],
                    tasks=my_tasks,
                    process=Process.sequential,
                    verbose=True
                )
                
                # Add a spinner for better UX
                with st.spinner("Agents are analyzing your request..."):
                    result = sports_crew.kickoff(inputs={'goal': user_goal, 'current_time': now})
                
                status.update(label="Analysis Complete! 🎉", state="complete")

                st.divider()
                
                # Modern Results Section
                st.markdown("""
                    <div style='text-align: center; margin: 2rem 0 1rem 0;'>
                        <span style='font-size: 2rem;'>📋</span>
                        <h2>Executive Summary</h2>
                    </div>
                """, unsafe_allow_html=True)
                
                final_report = result.raw if hasattr(result, 'raw') else str(result)
                
                # Enhanced glass card for results
                st.markdown(f"""
                    <div style='
                        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
                        padding: 2rem;
                        border-radius: 28px;
                        border: 1px solid rgba(59, 130, 246, 0.3);
                        backdrop-filter: blur(10px);
                        margin: 1rem 0;
                    '>
                        <div style='
                            font-family: "Inter", monospace;
                            color: #f1f5f9;
                            line-height: 1.6;
                            font-size: 1rem;
                        '>
                            {final_report.strip('`')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Quick Actions
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                with col2:
                    if st.button("📤 Export Report", use_container_width=True):
                        st.info("Export functionality coming soon!")
                
            except Exception as e:
                st.error(f"Analysis Error: {e}")

# Footer with gradient
st.markdown("""
    <div style='text-align: center; padding: 2rem 0 1rem 0;'>
        <div style='height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent); margin: 1rem 0;'></div>
        <p style='color: #64748b; font-size: 0.85rem;'>Designed for Modern Analytics • DeepSeek-R1 • CrewAI Framework</p>
    </div>
""", unsafe_allow_html=True)