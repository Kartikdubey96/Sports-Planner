import streamlit as st
import os
import sys
import re
from datetime import datetime

sys.path.append(os.path.dirname(__file__))

st.set_page_config(
    page_title="SportsCraft AI",
    page_icon="🏟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

/* ── CSS Variables (EGGSHELL CREAM & MATCHA) ── */
:root {
    /* Backgrounds */
    --bg-main:      #f3f0e7; /* Eggshell Cream */
    --bg-card:      #bdc9ac; /* Soft Matcha Green */
    --bg-input:     #d1d9c5; /* Lighter Matcha for inset fields */
    
    /* Typography - Deep Forest Green */
    --text-1:       #233118; /* Main Dark Text */
    --text-2:       #3a4a2b; /* Muted Dark Text */
    --text-3:       #546643; /* Placeholder/Subtext */
    
    /* Neumorphic Shadows for Main BG (#f3f0e7) */
    --sh-main-drk:  #dcd8cf;
    --sh-main-lgt:  #ffffff;
    
    /* Neumorphic Shadows for Card BG (#bdc9ac) */
    --sh-card-drk:  #a6b297;
    --sh-card-lgt:  #d4e0c1;
    
    --radius:       20px;
    --radius-sm:    12px;
}

/* ── Global Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Nunito', sans-serif !important;
    background: var(--bg-main) !important;
    color: var(--text-1) !important;
}

[data-testid="stAppViewContainer"]::before, 
[data-testid="stAppViewContainer"]::after { display: none !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg-main) !important;
    border-right: none !important;
    /* Soft neumorphic ridge separating sidebar */
    box-shadow: 4px 0 15px var(--sh-main-drk) !important;
}
[data-testid="stSidebar"] * { color: var(--text-2) !important; }
[data-testid="stSidebarContent"] { padding: 2.5rem 1.5rem !important; }

/* ── Main block ── */
.main .block-container {
    padding: 3rem 4rem 5rem !important;
    max-width: 1200px !important;
    background: var(--bg-main) !important;
}

/* ── Headings ── */
h1 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 2.8rem !important;
    font-weight: 900 !important;
    letter-spacing: -1px !important;
    color: var(--text-1) !important;
    line-height: 1.1 !important;
}
h2 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    color: var(--text-1) !important;
}
h3 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    color: var(--text-1) !important;
}

/* ── Tabs (Pill Style) ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card) !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 8px !important;
    gap: 8px !important;
    box-shadow: 6px 6px 14px var(--sh-main-drk), -6px -6px 14px var(--sh-main-lgt) !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 800 !important;
    color: var(--text-3) !important;
    border-radius: 50px !important;
    padding: 0.6rem 2rem !important;
    transition: all 0.2s ease !important;
    background: transparent !important;
    border: 2px solid transparent !important;
    box-shadow: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-1) !important;
}
.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: var(--text-1) !important;
    border: 2px solid var(--text-1) !important; 
    box-shadow: none !important;
}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Inputs (INSET SHADOW + RED LINE FIX) ── */
.stTextInput input, .stTextArea textarea {
    background: var(--bg-input) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    /* Soft inset shadow to look pressed in */
    box-shadow: inset 4px 4px 8px #bec6b4, inset -4px -4px 8px #e4ecd6 !important;
    padding: 0.85rem 1.2rem !important;
    transition: all 0.2s ease !important;
}

/* KILLS STREAMLIT RED BORDER WRAPPERS */
.stTextInput > div > div, .stTextArea > div > div {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}
.stTextInput > div > div:focus-within, .stTextArea > div > div:focus-within {
    border: none !important;
    box-shadow: none !important;
}

/* CUSTOM DEEP GREEN FOCUS RING */
.stTextInput input:focus, .stTextArea textarea:focus {
    box-shadow: inset 4px 4px 8px #bec6b4, inset -4px -4px 8px #e4ecd6, 0 0 0 2px var(--text-1) !important;
    border: none !important;
    outline: none !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-3) !important;
    font-weight: 600 !important;
}
*:focus, *:focus-visible { outline: none !important; }

/* ── Selectbox ── */
.stSelectbox div[data-baseweb="select"] > div {
    background: var(--bg-input) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    box-shadow: inset 4px 4px 8px #bec6b4, inset -4px -4px 8px #e4ecd6 !important;
    outline: none !important;
}

/* ── Dropdown Menu (BLACK BACKGROUND FIX) ── */
div[data-baseweb="popover"], ul[data-baseweb="menu"], .st-emotion-cache-11loom0 {
    background: var(--bg-card) !important; /* Forces the menu to be Matcha Green */
    border: none !important;
    border-radius: var(--radius) !important;
    box-shadow: 6px 6px 14px var(--sh-card-drk), -6px -6px 14px var(--sh-card-lgt) !important;
    padding: 8px !important;
}
li[role="option"], .st-emotion-cache-17f8zj6, .st-emotion-cache-15je8ou {
    background: transparent !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}
li[role="option"]:hover, .st-emotion-cache-17f8zj6:hover {
    background: var(--bg-input) !important;
    color: var(--text-1) !important;
}
li[aria-selected="true"] {
    background: var(--text-1) !important;
    color: var(--bg-main) !important;
}
div[data-baseweb="select"] [role="button"] { background: transparent !important; border: none !important; }

/* ── Buttons ── */
.stButton > button, .stButton > button[kind="primary"] {
    background: var(--bg-card) !important;
    color: var(--text-1) !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 800 !important;
    padding: 0.8rem 2rem !important;
    /* Outset shadow to pop off the screen */
    box-shadow: 6px 6px 12px var(--sh-main-drk), -6px -6px 12px var(--sh-main-lgt) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover, .stButton > button[kind="primary"]:hover {
    box-shadow: 4px 4px 8px var(--sh-main-drk), -4px -4px 8px var(--sh-main-lgt) !important;
    transform: translateY(1px);
}
.stButton > button:active, .stButton > button[kind="primary"]:active {
    /* Pressed inward shadow */
    box-shadow: inset 4px 4px 8px var(--sh-card-drk), inset -4px -4px 8px var(--sh-card-lgt) !important;
    transform: translateY(2px);
}

/* ── Custom Sidebar Metrics ── */
.sidebar-metric {
    background: var(--bg-card);
    border-radius: var(--radius-sm);
    padding: 0.8rem 1rem;
    box-shadow: 4px 4px 10px var(--sh-main-drk), -4px -4px 10px var(--sh-main-lgt);
    margin-bottom: 1rem;
}
.sidebar-metric-label {
    color: var(--text-3);
    font-size: 0.65rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
}
.sidebar-metric-value {
    color: var(--text-1);
    font-size: 1.4rem;
    font-weight: 900;
    line-height: 1;
}

/* ── Alerts & Expanders ── */
.stAlert {
    background: var(--bg-card) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    box-shadow: 4px 4px 10px var(--sh-main-drk), -4px -4px 10px var(--sh-main-lgt) !important;
}
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    box-shadow: 4px 4px 10px var(--sh-main-drk), -4px -4px 10px var(--sh-main-lgt) !important;
}

/* ── Raised Matcha Cards ── */
.neu-card {
    background: var(--bg-card);
    border-radius: var(--radius);
    padding: 1.8rem 2rem;
    box-shadow: 8px 8px 16px var(--sh-main-drk), -8px -8px 16px var(--sh-main-lgt);
    margin-bottom: 1.5rem;
}
.result-card {
    background: var(--bg-input);
    border-radius: var(--radius);
    padding: 2rem;
    margin-top: 1rem;
    line-height: 1.8;
    color: var(--text-1);
    font-weight: 600;
    font-size: 1rem;
    font-family: 'Nunito', sans-serif;
    box-shadow: inset 4px 4px 8px #bec6b4, inset -4px -4px 8px #e4ecd6;
}

/* ── Badges, Labels & Dividers ── */
.type-pill {
    display: inline-block;
    background: var(--text-1);
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--bg-main);
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Label for Sidebar (No horizontal line) */
.sidebar-label {
    font-family: 'Nunito', sans-serif;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--text-3);
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}

/* Label for Main Content (With horizontal line) */
.section-label {
    font-family: 'Nunito', sans-serif;
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--text-2);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--sh-main-drk), transparent);
}

hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, var(--sh-main-drk), transparent) !important;
    margin: 1.5rem 0 !important;
}

/* ── UI FIX: Hide junk but KEEP sidebar toggle ── */
#MainMenu, footer { visibility: hidden !important; }
header { background: transparent !important; }
.stDeployButton { display: none !important; }
/* Ensure the button to expand sidebar stays visible */
[data-testid="collapsedControl"] { visibility: visible !important; color: var(--text-1) !important; }
/* ── FIX: Agent Chat Messages & Status Bars ── */

/* 1. Force the status loading bar to be a Matcha Card */
[data-testid="stStatusWidget"] {
    background: var(--bg-card) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: 4px 4px 10px var(--sh-main-drk), -4px -4px 10px var(--sh-main-lgt) !important;
}

/* Force all text inside the status bar to be dark green */
[data-testid="stStatusWidget"] * {
    color: var(--text-1) !important;
}

/* 2. Force all text inside the agent chat logs to be dark green */
[data-testid="stChatMessage"] {
    background: transparent !important;
}
[data-testid="stChatMessage"] * {
    color: var(--text-1) !important;
}

/* Fix the horizontal divider lines inside the chat to match the theme */
[data-testid="stChatMessage"] hr {
    background: linear-gradient(90deg, transparent, var(--sh-main-drk), transparent) !important;
    height: 2px !important;
    border: none !important;
}
/* ── ULTIMATE FIX FOR STATUS WIDGET BLACK BAR ── */

/* 1. Make the outer wrapper transparent */
[data-testid="stStatusWidget"] {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    margin-bottom: 1.5rem !important;
}

/* 2. Force the inner components to use the Soft Matcha Card style */
[data-testid="stStatusWidget"] > div,
[data-testid="stStatusWidget"] details {
    background-color: var(--bg-card) !important;
    background: var(--bg-card) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: 4px 4px 10px var(--sh-main-drk), -4px -4px 10px var(--sh-main-lgt) !important;
}

/* 3. Strip any black backgrounds from the clickable summary header */
[data-testid="stStatusWidget"] summary,
[data-testid="stStatusWidget"] summary:hover,
[data-testid="stStatusWidget"] [data-testid="stExpanderDetails"] {
    background-color: transparent !important;
    background: transparent !important;
}

/* 4. Force ALL text and loading icons inside to be bold dark green */
[data-testid="stStatusWidget"] * {
    color: var(--text-1) !important;
    font-weight: 800 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Imports ──
try:
    from crewai import Crew, Process
    from agents import planner_agent, analyst_agent, reporter_agent, content_writer_agent
    from tasks import create_tasks
    import vector_store as vs
except Exception as e:
    st.error(f"Environment Error: {e}")
    st.stop()

# ─────────────────────────────────────────────
#  CALLBACK
# ─────────────────────────────────────────────
def streamlit_callback(step_output):
    raw_text = str(step_output)
    if "Failed to parse" in raw_text: return
    with st.chat_message("ai", avatar="🤖"):
        thought = re.search(r"thought=['\"](.*?)['\"]", raw_text, re.DOTALL)
        output  = re.search(r"output=['\"](.*?)['\"]",  raw_text, re.DOTALL)
        if thought:
            clean = thought.group(1).replace('\\n', '\n').strip()
            if clean: st.markdown(f"**🔍 Strategy**\n\n{clean}")
        if output:
            clean = output.group(1).replace('\\n', '\n').strip()
            if clean not in ["{}", "{", "None", ""]:
                st.markdown("---")
                st.markdown(f"**✅ Findings**\n\n{clean}")

# ─────────────────────────────────────────────
#  SIDEBAR (PERFECT MATCH TO IMAGE)
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style='padding: 0 0 1.5rem;'>
            <div style='font-family:"Nunito",sans-serif; font-size:1.5rem; font-weight:900;
                        color:var(--text-1); letter-spacing:-0.5px;'>
                SportsCraft AI
            </div>
            <div style='font-size:0.85rem; color:var(--text-3); margin-top:2px; font-weight:700;'>
                GAI-10 · Group 10D5
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">API CONFIG</div>', unsafe_allow_html=True)
    serper_key = st.text_input("Serper API Key", value="", type="password", label_visibility="collapsed", placeholder="Serper API Key")
    os.environ["SERPER_API_KEY"] = serper_key

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">STATUS</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
        <div class="sidebar-metric">
            <div class="sidebar-metric-label">AGENTS</div>
            <div class="sidebar-metric-value">4</div>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
        <div class="sidebar-metric">
            <div class="sidebar-metric-label">SAVED</div>
            <div class="sidebar-metric-value">{vs.get_count()}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">AGENTS</div>', unsafe_allow_html=True)
    
    st.markdown("""
<div style='font-size:0.9rem; line-height:2.2; color:var(--text-2); font-weight:600;'>
    Lead Sports Planner<br>
    Resource Validator<br>
    Chief Sports Editor<br>
    <span style='color:var(--text-1); font-weight:900;'>Elite Content Writer</span><br>
    <span style='font-size:0.65rem; background:var(--text-1);
    color:var(--bg-main); border-radius:12px; padding:3px 10px; margin-top:4px; font-weight:800; display:inline-block;'>NEW</span>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style='padding: 0.5rem 0 2rem;'>
    <h1>SportsCraft AI</h1>
    <p style='color:var(--text-2); font-size:1.1rem; margin-top:0.4rem; font-weight:700;'>
        Intelligent Sports Analysis & Content Generation · Powered by Gemini 2.5 Flash
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab_analysis, tab_generator, tab_vault = st.tabs([
    "Sports Analysis",
    "Content Generator",
    "Content Vault"
])

# ══════════════════════════════════════════════
#  TAB 1 — SPORTS ANALYSIS
# ══════════════════════════════════════════════
with tab_analysis:
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='neu-card'>
    <div style='font-size:1.2rem; font-weight:900; color:var(--text-1); margin-bottom:0.25rem;'>Analysis Request</div>
    <div style='font-size:1rem; color:var(--text-3); font-weight:700;'>Multi-agent AI research powered by real-time web search</div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        user_goal = st.text_input("goal_input", label_visibility="collapsed", placeholder="Analyze India's batting performance...")
    with col2:
        execute = st.button("Analyze", type="primary", use_container_width=True)

    if execute:
        if not user_goal: st.warning("Please enter a goal first.")
        else:
            planner_agent.step_callback = analyst_agent.step_callback = reporter_agent.step_callback = streamlit_callback
            with st.status("Orchestrating agents...", expanded=True) as status:
                try:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    tasks = create_tasks(planner_agent, analyst_agent, reporter_agent)
                    crew = Crew(agents=[planner_agent, analyst_agent, reporter_agent], tasks=tasks)
                    result = crew.kickoff(inputs={'goal': user_goal, 'current_time': now})
                    status.update(label="Analysis complete ✓", state="complete")
                    
                    st.divider()
                    st.markdown("### Executive Summary")
                    final = result.raw if hasattr(result, 'raw') else str(result)
                    st.markdown(f'<div class="result-card">{final}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Analysis Error: {e}")

# ══════════════════════════════════════════════
#  TAB 2 — CONTENT GENERATOR
# ══════════════════════════════════════════════
with tab_generator:
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='neu-card'>
    <div style='font-size:1.2rem; font-weight:900; color:var(--text-1); margin-bottom:0.25rem;'>Sports Content Generator</div>
    <div style='font-size:1rem; color:var(--text-3); font-weight:700;'>Transform topics into publication-ready sports content</div>
</div>
""", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="section-label">Content Type</div>', unsafe_allow_html=True)
        content_type = st.selectbox("content_type", label_visibility="collapsed", options=["Match Recap", "Player Profile", "Season Review"])
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Sport</div>', unsafe_allow_html=True)
        sport = st.selectbox("sport", label_visibility="collapsed", options=["Cricket", "Football", "Basketball", "Tennis"])

    with col_right:
        st.markdown('<div class="section-label">Topic / Match</div>', unsafe_allow_html=True)
        topic = st.text_input("topic", label_visibility="collapsed", placeholder="e.g., India vs Australia — 3rd Test, Brisbane")
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Key Details</div>', unsafe_allow_html=True)
        details = st.text_area("details", label_visibility="collapsed", placeholder="e.g., India won by 6 wickets. Shubman Gill 91*...", height=115)

    st.markdown("---")
    
    gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
    with gen_col2:
        generate = st.button("Generate Content", type="primary", use_container_width=True)

    if generate:
        if not topic.strip(): st.warning("Please enter a topic.")
        else:
            tone = "Analytical" 
            content_writer_agent.step_callback = planner_agent.step_callback = analyst_agent.step_callback = streamlit_callback
            with st.status(f"Writing {content_type}...", expanded=True) as gen_status:
                try:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    tasks = create_tasks(planner_agent, analyst_agent, content_writer_agent, content_type=content_type, topic=f"{topic}: {details}", sport=sport, tone=tone)
                    crew = Crew(agents=[planner_agent, analyst_agent, content_writer_agent], tasks=tasks)
                    result = crew.kickoff(inputs={'current_time': now})
                    gen_status.update(label="Content ready ✓", state="complete")
                    
                    final_content = result.raw if hasattr(result, 'raw') else str(result)
                    st.session_state["last_generated"] = {"content_type": content_type, "topic": topic, "sport": sport, "tone": tone, "body": final_content}
                    
                    st.divider()
                    st.markdown(f'<span class="type-pill">{content_type} · {sport}</span>', unsafe_allow_html=True)
                    st.markdown(f"### {topic}")
                    st.markdown(f'<div class="result-card">{final_content}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Generation Error: {e}")

    if "last_generated" in st.session_state:
        st.markdown("---")
        save_col1, save_col2, save_col3 = st.columns([1, 2, 1])
        with save_col2:
            if st.button("Save to Content Vault", use_container_width=True):
                d = st.session_state["last_generated"]
                vs.save_content(content_type=d["content_type"], topic=d["topic"], sport=d["sport"], tone=d["tone"], body=d["body"])
                st.success("Saved ✓")
                del st.session_state["last_generated"]
                st.rerun()

# ══════════════════════════════════════════════
#  TAB 3 — CONTENT VAULT
# ══════════════════════════════════════════════
with tab_vault:
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='neu-card'>
    <div style='font-size:1.2rem; font-weight:900; color:var(--text-1); margin-bottom:0.25rem;'>Content Vault</div>
    <div style='font-size:1rem; color:var(--text-3); font-weight:700;'>All generated content stored in ChromaDB · Semantic search enabled</div>
</div>
""", unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([5, 1])
    with search_col1:
        search_query = st.text_input("vault_search", label_visibility="collapsed", placeholder="Search saved content...")
    with search_col2:
        do_search = st.button("Search", use_container_width=True)

    st.markdown("---")
    
    items = vs.search_similar(search_query, n_results=5) if (do_search and search_query.strip()) else vs.get_all_saved()
    
    if items:
        if do_search and search_query.strip():
            st.markdown(f"<p style='font-size:1rem; color:var(--text-2); font-weight:800;'>{len(items)} result(s) for <em>{search_query}</em></p>", unsafe_allow_html=True)
        for item in reversed(items):
            m = item.get("meta", item) 
            title = m.get('topic', 'Untitled')
            c_type = m.get('content_type', 'Data')
            with st.expander(f"{c_type} · {title}"):
                st.markdown(f'<span class="type-pill">{c_type} · {m.get("sport","")}</span>', unsafe_allow_html=True)
                st.markdown(item["body"])
                if st.button("Delete", key=f"del_{item['id']}"):
                    vs.delete_content(item["id"])
                    st.rerun()
    else:
        st.markdown("""
        <div style='text-align:center; padding:4rem 1rem;'>
            <div style='font-size:3rem; margin-bottom:1rem; opacity:0.4;'>🗄️</div>
            <p style='font-size:1.1rem; color:var(--text-2); font-weight:800;'>Vault is empty.</p>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div style='text-align:center; padding:3rem 0 1rem; margin-top:2rem;'>
    <div style='font-size:0.85rem; color:var(--text-3); font-weight:800; letter-spacing:0.5px;'>
        SportsCraft AI · GAI-10 · Group 10D5 · Medicaps University · Datagami 2026
    </div>
</div>
""", unsafe_allow_html=True)