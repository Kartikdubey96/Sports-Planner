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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Variables ── */
:root {
    --bg:           #000000;
    --glass:        rgba(255,255,255,0.04);
    --glass-card:   rgba(255,255,255,0.06);
    --glass-hover:  rgba(255,255,255,0.08);
    --border:       rgba(255,255,255,0.08);
    --border-2:     rgba(255,255,255,0.14);
    --text-1:       #ffffff;
    --text-2:       #888888;
    --text-3:       #444444;
    --accent:       #ffffff;
    --blur:         blur(20px) saturate(160%);
    --radius:       14px;
    --radius-sm:    8px;
}

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text-1) !important;
}

/* ── Remove all focus outlines ── */
*:focus { outline: none !important; }
*:focus-visible { outline: none !important; box-shadow: 0 0 0 1px rgba(255,255,255,0.2) !important; }

/* ── Subtle grid background ── */
[data-testid="stMain"] {
    background-image:
        linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
    background-size: 48px 48px;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(10,10,10,0.95) !important;
    backdrop-filter: var(--blur) !important;
    border-right: 1px solid var(--border) !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] * { color: var(--text-2) !important; }
[data-testid="stSidebarContent"] { padding: 1.8rem 1.2rem !important; }

/* ── Main block ── */
.main .block-container {
    padding: 2.5rem 3rem 5rem !important;
    max-width: 1100px !important;
    position: relative;
    z-index: 1;
}

/* ── Headings ── */
h1 {
    font-family: 'Inter', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.5px !important;
    color: var(--text-1) !important;
    line-height: 1.1 !important;
}
h2 {
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: var(--text-1) !important;
}
h3 {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: var(--text-1) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 5px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--text-3) !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.5rem 1.2rem !important;
    transition: all 0.2s !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-2) !important;
    background: var(--glass-hover) !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(255,255,255,0.1) !important;
    color: var(--text-1) !important;
    border: 1px solid var(--border-2) !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.08) !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    transition: border-color 0.2s !important;
    box-shadow: none !important;
    outline: none !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: rgba(255,255,255,0.25) !important;
    box-shadow: none !important;
    outline: none !important;
    background: rgba(255,255,255,0.06) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-3) !important;
}

/* ── Selectbox ── */
.stSelectbox div[data-baseweb="select"] > div {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    box-shadow: none !important;
    outline: none !important;
    transition: border-color 0.2s !important;
}
.stSelectbox div[data-baseweb="select"] > div:hover {
    border-color: var(--border-2) !important;
}

/* ── Dropdown ── */
div[data-baseweb="popover"],
ul[data-baseweb="menu"],
.st-emotion-cache-11loom0 {
    background: #111111 !important;
    border: 1px solid var(--border-2) !important;
    border-radius: var(--radius) !important;
    box-shadow: 0 16px 48px rgba(0,0,0,0.8) !important;
    padding: 5px !important;
    backdrop-filter: none !important;
}
li[role="option"],
.st-emotion-cache-17f8zj6,
.st-emotion-cache-15je8ou {
    background: transparent !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-2) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 400 !important;
    transition: all 0.15s !important;
    box-shadow: none !important;
}
li[role="option"]:hover,
.st-emotion-cache-17f8zj6:hover {
    background: rgba(255,255,255,0.06) !important;
    color: var(--text-1) !important;
    border-radius: var(--radius-sm) !important;
}
li[aria-selected="true"] {
    background: rgba(255,255,255,0.08) !important;
    color: var(--text-1) !important;
}

/* ── Primary Button ── */
.stButton > button[kind="primary"] {
    background: var(--text-1) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.8rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 0 20px rgba(255,255,255,0.15) !important;
    outline: none !important;
}
.stButton > button[kind="primary"]:hover {
    background: #e8e8e8 !important;
    box-shadow: 0 0 30px rgba(255,255,255,0.25) !important;
}
.stButton > button[kind="primary"]:active {
    background: #cccccc !important;
    box-shadow: none !important;
}
.stButton > button[kind="primary"]:focus { outline: none !important; }

/* ── Secondary Button ── */
.stButton > button {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    color: var(--text-2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
    box-shadow: none !important;
    outline: none !important;
}
.stButton > button:hover {
    border-color: var(--border-2) !important;
    color: var(--text-1) !important;
    background: var(--glass-hover) !important;
}
.stButton > button:focus { outline: none !important; }

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem 1.2rem !important;
    box-shadow: none !important;
    transition: border-color 0.2s !important;
}
[data-testid="stMetric"]:hover { border-color: var(--border-2) !important; }
[data-testid="stMetricLabel"] {
    color: #999999 !important; /* Much more visible against black */
    font-family: 'Inter', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
[data-testid="stMetricValue"] {
    color: var(--text-1) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}

/* ── Status ── */
[data-testid="stStatusWidget"] {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    box-shadow: none !important;
}

/* ── Alerts ── */
.stAlert {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    box-shadow: none !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    box-shadow: none !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--glass) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid rgba(255,255,255,0.2) !important; /* Brighter border */
    border-radius: var(--radius-sm) !important;
    color: #ffffff !important; /* Forced white for readability */
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
    transition: border-color 0.2s !important;
}
.streamlit-expanderHeader:hover {
    border-color: var(--border-2) !important;
    background: var(--glass-hover) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #222; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #444; }

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Glass card ── */
.glass-card {
    background: var(--glass-card);
    backdrop-filter: var(--blur);
    -webkit-backdrop-filter: var(--blur);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.2rem 1.4rem;
    margin-bottom: 1.2rem;
    transition: border-color 0.2s;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
}
.glass-card:hover {
    border-color: var(--border-2);
}

/* ── Result card ── */
.result-card {
    background: var(--glass);
    backdrop-filter: var(--blur);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.8rem;
    margin-top: 1rem;
    line-height: 1.8;
    color: var(--text-2);
    font-size: 0.88rem;
    font-family: 'Inter', sans-serif;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.04);
}

/* ── Type pill ── */
.type-pill {
    display: inline-block;
    background: rgba(255,255,255,0.06);
    border: 1px solid var(--border-2);
    color: var(--text-2);
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.7rem;
    font-weight: 500;
    margin-bottom: 8px;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.3px;
}

/* ── Section label ── */
.section-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    color: #888888; /* Swapped to the lighter grey variable */
    text-transform: uppercase;
    margin-bottom: 0.45rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
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
    if "Failed to parse" in raw_text:
        return
    with st.chat_message("ai", avatar="🤖"):
        thought = re.search(r"thought=['\"](.*?)['\"]", raw_text, re.DOTALL)
        output  = re.search(r"output=['\"](.*?)['\"]",  raw_text, re.DOTALL)
        if thought:
            clean = thought.group(1).replace('\\n', '\n').strip()
            if clean:
                st.markdown(f"**🔍 Strategy**\n\n{clean}")
        if output:
            clean = output.group(1).replace('\\n', '\n').strip()
            if clean not in ["{}", "{", "None", ""]:
                st.markdown("---")
                st.markdown(f"**✅ Findings**\n\n{clean}")

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 2rem;'>
            <div style='font-family:"Inter",sans-serif; font-size:0.95rem; font-weight:700;
                        color:#ffffff; letter-spacing:-0.3px;'>
                🏟️ SportsCraft AI
            </div>
            <div style='font-size:0.7rem; color:#444444; margin-top:4px;
                        letter-spacing:0.5px; font-weight:500;'>
                GAI-10 · Group 10D5
            </div>
        </div>
    """, unsafe_allow_html=True)

    from dotenv import load_dotenv
    load_dotenv() # This loads your real key from the .env file

    st.markdown('<div class="section-label">API Config</div>', unsafe_allow_html=True)
    
    # Grab the real key from the environment
    real_key = os.environ.get("SERPER_API_KEY", "")
    
    serper_key = st.text_input("Serper API Key", value=real_key, type="password",
                               help="Required for real-time web search")
    
    # Only update the environment if the box isn't empty
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key

    st.markdown("---")
    st.markdown('<div class="section-label">System Status</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Agents", "4")
    with col_b:
        st.metric("Saved", str(vs.get_count()))

    st.markdown("---")
    st.markdown('<div class="section-label">Active Agents</div>', unsafe_allow_html=True)
    st.markdown("""
<div style='font-size:0.78rem; line-height:2.4; color:#444444;
            font-family:"Inter",sans-serif; font-weight:400;'>
    🔍 &nbsp;Lead Sports Planner<br>
    ✅ &nbsp;Resource Validator<br>
    📝 &nbsp;Chief Sports Editor<br>
    ✍️ &nbsp;<span style='color:#888888;'>Elite Content Writer</span>
    <span style='font-size:0.62rem; background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.14); color:#888888;
    border-radius:4px; padding:1px 6px; margin-left:4px;'>NEW</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.7rem; color:#333333; line-height:2;
            font-family:"Inter",sans-serif; font-weight:400;'>
    CrewAI · Gemini 1.5 Flash<br>
    ChromaDB · Streamlit<br>
    Docker · AWS EC2
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style='padding: 0.5rem 0 2rem;'>
    <h1>SportsCraft AI</h1>
    <p style='color:#444444; font-size:0.82rem; margin-top:0.4rem; font-weight:400;
              font-family:"Inter",sans-serif; letter-spacing:0.1px;'>
        Intelligent Sports Analysis & Content Generation &nbsp;·&nbsp; Powered by Gemini 1.5 Flash
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab_analysis, tab_generator, tab_vault = st.tabs([
    "⚡ Sports Analysis",
    "✍️ Content Generator",
    "🗄️ Content Vault"
])

# ══════════════════════════════════════════════
#  TAB 1 — SPORTS ANALYSIS
# ══════════════════════════════════════════════
with tab_analysis:
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card'>
    <div style='font-family:"Inter",sans-serif; font-size:0.88rem; font-weight:600;
                color:#ffffff; margin-bottom:0.2rem;'>🎯 Analysis Request</div>
    <div style='font-size:0.78rem; color:#555555; font-family:"Inter",sans-serif;'>
        Multi-agent AI research powered by real-time web search
    </div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        user_goal = st.text_input(
            "goal_input", label_visibility="collapsed",
            placeholder="Analyze India's batting performance in the 2024 T20 World Cup..."
        )
    with col2:
        execute = st.button("Analyze", type="primary", use_container_width=True)

    if execute:
        if not user_goal:
            st.warning("Please enter a goal first.")
        else:
            planner_agent.step_callback  = streamlit_callback
            analyst_agent.step_callback  = streamlit_callback
            reporter_agent.step_callback = streamlit_callback

            with st.status("Orchestrating agents...", expanded=True) as status:
                try:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    tasks = create_tasks(planner_agent, analyst_agent, reporter_agent)
                    crew  = Crew(
                        agents=[planner_agent, analyst_agent, reporter_agent],
                        tasks=tasks,
                        process=Process.sequential,
                        verbose=True
                    )
                    with st.spinner("Agents are analysing your request..."):
                        result = crew.kickoff(inputs={'goal': user_goal, 'current_time': now})
                    status.update(label="Analysis complete ✓", state="complete")

                    st.divider()
                    st.markdown("### 📋 Executive Summary")
                    final = result.raw if hasattr(result, 'raw') else str(result)
                    st.markdown(f'<div class="result-card">{final}</div>', unsafe_allow_html=True)

                    col_x, col_y, col_z = st.columns(3)
                    with col_y:
                        if st.button("📤 Export Report", use_container_width=True):
                            st.info("Export coming soon!")
                except Exception as e:
                    st.error(f"Analysis Error: {e}")

# ══════════════════════════════════════════════
#  TAB 2 — CONTENT GENERATOR
# ══════════════════════════════════════════════
with tab_generator:
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card'>
    <div style='font-family:"Inter",sans-serif; font-size:0.88rem; font-weight:600;
                color:#ffffff; margin-bottom:0.2rem;'>✍️ Sports Content Generator</div>
    <div style='font-size:0.78rem; color:#555555; font-family:"Inter",sans-serif;'>
        Transform topics into publication-ready sports content using advanced prompt engineering
    </div>
</div>
""", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="section-label">Content Type</div>', unsafe_allow_html=True)
        content_type = st.selectbox(
            "content_type", label_visibility="collapsed",
            options=["Match Recap", "Player Profile", "Pre-Match Analysis", "Season Review"],
        )
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Sport</div>', unsafe_allow_html=True)
        sport = st.selectbox(
            "sport", label_visibility="collapsed",
            options=["Cricket", "Football (Soccer)", "Basketball", "Tennis", "Hockey", "Rugby", "Kabaddi", "Baseball"]
        )
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Tone</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            "tone", label_visibility="collapsed",
            options=["Dramatic", "Journalistic", "Analytical", "Casual"],
        )

    with col_right:
        st.markdown('<div class="section-label">Topic / Match</div>', unsafe_allow_html=True)
        topic = st.text_input(
            "topic", label_visibility="collapsed",
            placeholder="e.g., India vs Australia — 3rd Test, Brisbane"
        )
        st.markdown('<div class="section-label" style="margin-top:1.2rem;">Key Details / Stats</div>', unsafe_allow_html=True)
        details = st.text_area(
            "details", label_visibility="collapsed",
            placeholder="e.g., India won by 6 wickets. Shubman Gill scored 91*, Bumrah took 5/72...",
            height=140
        )

    st.markdown("---")
    gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
    with gen_col2:
        generate = st.button("⚡ Generate Content", type="primary", use_container_width=True)

    if generate:
        if not topic.strip():
            st.warning("Please enter a topic or match name.")
        else:
            content_writer_agent.step_callback = streamlit_callback
            planner_agent.step_callback         = streamlit_callback
            analyst_agent.step_callback         = streamlit_callback

            with st.status(f"Writing {content_type}...", expanded=True) as gen_status:
                try:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    full_topic = f"{topic}. Additional details: {details}" if details.strip() else topic

                    tasks = create_tasks(
                        planner_agent, analyst_agent, content_writer_agent,
                        content_type=content_type,
                        topic=full_topic,
                        sport=sport,
                        tone=tone
                    )
                    crew = Crew(
                        agents=[planner_agent, analyst_agent, content_writer_agent],
                        tasks=tasks,
                        process=Process.sequential,
                        verbose=True,
                        max_rpm=10
                    )
                    with st.spinner("Agents are crafting your content..."):
                        result = crew.kickoff(inputs={'current_time': now})
                    gen_status.update(label="Content ready ✓", state="complete")

                    final_content = result.raw if hasattr(result, 'raw') else str(result)

                    st.session_state["last_generated"] = {
                        "content_type": content_type,
                        "topic": topic,
                        "sport": sport,
                        "tone": tone,
                        "body": final_content
                    }

                    st.divider()

                    head_col1, head_col2 = st.columns([3, 1])
                    with head_col1:
                        st.markdown(f'<span class="type-pill">{content_type} · {sport} · {tone}</span>', unsafe_allow_html=True)
                        st.markdown(f"### {topic}")
                    with head_col2:
                        st.metric("Words", len(final_content.split()))

                    st.markdown(f'<div class="result-card">{final_content}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Generation Error: {e}")

    if "last_generated" in st.session_state:
        st.markdown("---")
        save_col1, save_col2, save_col3 = st.columns([1, 2, 1])
        with save_col2:
            if st.button("💾 Save to Content Vault", use_container_width=True):
                data = st.session_state["last_generated"]
                doc_id = vs.save_content(
                    content_type=data["content_type"],
                    topic=data["topic"],
                    sport=data["sport"],
                    tone=data["tone"],
                    body=data["body"]
                )
                st.success(f"Saved ✓  ID: `{doc_id}`")
                del st.session_state["last_generated"]
                st.rerun()

# ══════════════════════════════════════════════
#  TAB 3 — CONTENT VAULT
# ══════════════════════════════════════════════
with tab_vault:
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card'>
    <div style='font-family:"Inter",sans-serif; font-size:0.88rem; font-weight:600;
                color:#ffffff; margin-bottom:0.2rem;'>🗄️ Content Vault</div>
    <div style='font-size:0.78rem; color:#aaaaaa; font-family:"Inter",sans-serif;'>
        All generated content stored in ChromaDB · Semantic search enabled
    </div>
</div>
""", unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([5, 1])
    with search_col1:
        search_query = st.text_input(
            "vault_search", label_visibility="collapsed",
            placeholder="Search saved content... e.g. 'India batting collapse'"
        )
    with search_col2:
        do_search = st.button("Search", use_container_width=True)

    st.markdown("---")

    if do_search and search_query.strip():
        results = vs.search_similar(search_query, n_results=5)
        if results:
            st.markdown(f"<p style='font-size:0.78rem; color:#555555;'>{len(results)} result(s) for <em>{search_query}</em></p>", unsafe_allow_html=True)
            for r in results:
                m = r["meta"]
                with st.expander(f"{m.get('content_type','—')} · {m.get('topic','—')} · {m.get('created_at','—')}"):
                    st.markdown(f'<span class="type-pill">{m.get("content_type")} · {m.get("sport")} · {m.get("tone")}</span>', unsafe_allow_html=True)
                    st.markdown(r["body"])
                    if st.button("🗑️ Delete", key=f"del_{r['id']}"):
                        vs.delete_content(r["id"])
                        st.rerun()
        else:
            st.info("No matching content found.")
    else:
        saved = vs.get_all_saved()
        total = vs.get_count()

        v_col1, v_col2, v_col3 = st.columns(3)
        with v_col1: st.metric("Total Saved", total)
        with v_col2:
            types = list(set(s["meta"].get("content_type", "") for s in saved)) if saved else []
            st.metric("Content Types", len(types))
        with v_col3:
            sports = list(set(s["meta"].get("sport", "") for s in saved)) if saved else []
            st.metric("Sports Covered", len(sports))

        st.markdown("---")

        if not saved:
            st.markdown("""
<div style='text-align:center; padding:4rem 1rem;'>
    <div style='font-size:2rem; margin-bottom:1rem; opacity:0.15;'>🗄️</div>
    <p style='font-size:0.82rem; color:#444444; font-family:"Inter",sans-serif;
              font-weight:400; line-height:1.8;'>
        No content saved yet.<br>
        Generate content and click
        <strong style='color:#888888;'>Save to Content Vault</strong>.
    </p>
</div>
""", unsafe_allow_html=True)
        else:
            for item in reversed(saved):
                m = item["meta"]
                with st.expander(f"{m.get('content_type','—')} · {m.get('topic','—')} · {m.get('created_at','—')}"):
                    st.markdown(f'<span class="type-pill">{m.get("content_type")} · {m.get("sport")} · {m.get("tone")}</span>', unsafe_allow_html=True)
                    st.markdown(item["body"])
                    if st.button("🗑️ Delete", key=f"del_{item['id']}"):
                        vs.delete_content(item["id"])
                        st.rerun()

# ── Footer ──
st.markdown("""
<div style='text-align:center; padding:3rem 0 1rem; margin-top:2rem;
            border-top:1px solid rgba(255,255,255,0.05);'>
    <div style='font-size:0.68rem; color:#333333; font-family:"Inter",sans-serif;
                font-weight:500; letter-spacing:0.5px;'>
        SportsCraft AI · GAI-10 · Group 10D5 · Medicaps University · Datagami 2026
    </div>
</div>
""", unsafe_allow_html=True)