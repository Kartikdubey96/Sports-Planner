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
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Outfit:wght@300;400;500;600&display=swap');

/* ── CSS Variables ── */
:root {
    --glass-bg: rgba(255, 255, 255, 0.04);
    --glass-border: rgba(255, 255, 255, 0.10);
    --glass-hover: rgba(255, 255, 255, 0.08);
    --accent: #d97757;
    --accent-soft: rgba(217, 119, 87, 0.15);
    --accent-border: rgba(217, 119, 87, 0.35);
    --bg-1: #0a0f1e;
    --bg-2: #0d1528;
    --bg-3: #111a32;
    --text-primary: #f0f4ff;
    --text-secondary: #94a3c0;
    --text-muted: #4a5578;
    --blur: blur(20px) saturate(180%);
}

/* ── Global Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg-1) !important;
    color: var(--text-primary) !important;
}

/* ── Animated mesh gradient background ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 20% 10%, rgba(217,119,87,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 80% at 80% 90%, rgba(99,102,241,0.10) 0%, transparent 60%),
        radial-gradient(ellipse 50% 50% at 50% 50%, rgba(14,165,233,0.06) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    animation: meshShift 18s ease-in-out infinite alternate;
}

@keyframes meshShift {
    0%   { opacity: 0.8; filter: hue-rotate(0deg); }
    100% { opacity: 1.0; filter: hue-rotate(15deg); }
}

/* ── Floating orbs ── */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    width: 600px; height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(217,119,87,0.06) 0%, transparent 70%);
    top: -200px; right: -200px;
    pointer-events: none;
    z-index: 0;
    animation: orbFloat 12s ease-in-out infinite alternate;
}

@keyframes orbFloat {
    0%   { transform: translate(0, 0) scale(1); }
    100% { transform: translate(-40px, 40px) scale(1.1); }
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(10, 15, 30, 0.85) !important;
    backdrop-filter: var(--blur) !important;
    -webkit-backdrop-filter: var(--blur) !important;
    border-right: 1px solid var(--glass-border) !important;
    box-shadow: 4px 0 32px rgba(0,0,0,0.3) !important;
}
[data-testid="stSidebar"] * { color: var(--text-secondary) !important; }
[data-testid="stSidebarContent"] { padding: 1.5rem 1rem !important; }

/* ── Main block ── */
.main .block-container {
    padding: 2rem 2.5rem 4rem !important;
    max-width: 1200px !important;
    position: relative;
    z-index: 1;
}

/* ── Headings ── */
h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 3rem !important;
    font-weight: 800 !important;
    letter-spacing: -1px !important;
    background: linear-gradient(135deg, #f0f4ff 0%, #d97757 60%, #f97316 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    line-height: 1.05 !important;
    margin-bottom: 0.3rem !important;
}
h2 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
}
h3 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    -webkit-backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 16px !important;
    padding: 6px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    color: var(--text-muted) !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.6rem !important;
    transition: all 0.25s ease !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-secondary) !important;
    background: var(--glass-hover) !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(217,119,87,0.25), rgba(249,115,22,0.15)) !important;
    border: 1px solid var(--accent-border) !important;
    color: #f0f4ff !important;
    box-shadow: 0 4px 16px rgba(217,119,87,0.2), inset 0 1px 0 rgba(255,255,255,0.1) !important;
}

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.95rem !important;
    transition: all 0.2s ease !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05) !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent-border) !important;
    box-shadow: 0 0 0 3px rgba(217,119,87,0.12), inset 0 1px 0 rgba(255,255,255,0.05) !important;
    background: rgba(255,255,255,0.06) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-muted) !important;
}
/* ── Selectbox ── */
.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(15, 22, 45, 0.85) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'Outfit', sans-serif !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05) !important;
    transition: all 0.2s !important;
}
.stSelectbox div[data-baseweb="select"] > div:hover {
    border-color: var(--accent-border) !important;
}

/* ── Dropdown portal (solid color approach) ── */
div[data-baseweb="popover"],
ul[data-baseweb="menu"] {
    background: #0d1525 !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 14px !important;
    box-shadow: 0 16px 48px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.07) !important;
    padding: 6px !important;
}

li[role="option"] {
    background: transparent !important;
    border-radius: 8px !important;
    color: #94a3c0 !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
    transition: all 0.15s !important;
    margin: 2px 0 !important;
}

li[role="option"]:hover {
    background: rgba(217,119,87,0.15) !important;
    color: #f0f4ff !important;
}

li[aria-selected="true"] {
    background: linear-gradient(135deg, rgba(217,119,87,0.25), rgba(249,115,22,0.15)) !important;
    color: #f4a47a !important;
}
/* ── Primary Button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #d97757, #f97316) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 0.7rem 2rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(217,119,87,0.35), inset 0 1px 0 rgba(255,255,255,0.2) !important;
    text-transform: uppercase !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #e8845f, #ff8c28) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(217,119,87,0.5), inset 0 1px 0 rgba(255,255,255,0.25) !important;
}
.stButton > button[kind="primary"]:active {
    transform: translateY(0) !important;
}

/* ── Secondary Button ── */
.stButton > button {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    color: var(--text-secondary) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 10px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.85rem !important;
    transition: all 0.2s ease !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05) !important;
}
.stButton > button:hover {
    border-color: var(--accent-border) !important;
    color: var(--accent) !important;
    background: var(--glass-hover) !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 16px !important;
    padding: 1.2rem !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.07), 0 4px 20px rgba(0,0,0,0.2) !important;
    transition: border-color 0.2s !important;
}
[data-testid="stMetric"]:hover {
    border-color: var(--accent-border) !important;
}
[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
[data-testid="stMetricValue"] {
    color: var(--accent) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
}

/* ── Status ── */
[data-testid="stStatusWidget"] {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 16px !important;
}

/* ── Alerts ── */
.stAlert {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 14px !important;
    color: var(--text-primary) !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid var(--glass-border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 18px !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.06) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--glass-bg) !important;
    backdrop-filter: var(--blur) !important;
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
    color: var(--text-secondary) !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.2s !important;
}
.streamlit-expanderHeader:hover {
    border-color: var(--accent-border) !important;
    background: var(--glass-hover) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(217,119,87,0.3); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(217,119,87,0.6); }

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Glass card ── */
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: var(--blur);
    -webkit-backdrop-filter: var(--blur);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 1.8rem;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.08), 0 8px 32px rgba(0,0,0,0.25);
    transition: border-color 0.25s, box-shadow 0.25s;
}
.glass-card:hover {
    border-color: rgba(217,119,87,0.25);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.1), 0 12px 40px rgba(0,0,0,0.3), 0 0 0 1px rgba(217,119,87,0.1);
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, rgba(217,119,87,0.07) 0%, rgba(99,102,241,0.04) 100%);
    backdrop-filter: var(--blur);
    border: 1px solid rgba(217,119,87,0.2);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 1rem;
    line-height: 1.8;
    color: #c8d4f0;
    font-size: 0.95rem;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.07), 0 8px 32px rgba(0,0,0,0.2);
}

/* ── Type pill ── */
.type-pill {
    display: inline-block;
    background: linear-gradient(135deg, rgba(217,119,87,0.18), rgba(249,115,22,0.10));
    border: 1px solid var(--accent-border);
    color: #f4a47a;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    backdrop-filter: blur(8px);
}

/* ── Section label ── */
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--glass-border), transparent);
}

/* ── Glow accent line ── */
.accent-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    border-radius: 2px;
    margin: 0.3rem 0 1.2rem;
    opacity: 0.6;
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
        <div style='text-align:center; padding: 0.8rem 0 2rem;'>
            <div style='
                width:64px; height:64px; border-radius:18px; margin:0 auto 0.8rem;
                background:linear-gradient(135deg,rgba(217,119,87,0.25),rgba(249,115,22,0.12));
                border:1px solid rgba(217,119,87,0.35);
                backdrop-filter:blur(12px);
                display:flex; align-items:center; justify-content:center;
                font-size:1.8rem;
                box-shadow: 0 8px 24px rgba(217,119,87,0.2), inset 0 1px 0 rgba(255,255,255,0.1);
            '>🏟️</div>
            <div style='font-family:"Syne",sans-serif; font-size:1.2rem; font-weight:800; letter-spacing:1px;
                        background:linear-gradient(135deg,#f0f4ff,#d97757);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;'>
                SportsCraft AI
            </div>
            <div style='font-size:0.72rem; color:#4a5578; margin-top:6px; letter-spacing:1.5px; font-weight:500;'>
                GAI-10 · GROUP 10D5
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">⚙️ API Config</div>', unsafe_allow_html=True)
    serper_key = st.text_input("Serper API Key", value="HIDDEN", type="password",
                               help="Required for real-time web search")
    os.environ["SERPER_API_KEY"] = serper_key

    st.markdown("---")
    st.markdown('<div class="section-label">📊 System Status</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Agents", "4")
    with col_b:
        st.metric("Saved", str(vs.get_count()))

    st.markdown("---")
    st.markdown('<div class="section-label">🤖 Active Agents</div>', unsafe_allow_html=True)
    st.markdown("""
<div style='font-size:0.82rem; line-height:2.2; color:#4a5578; font-family:"Outfit",sans-serif;'>
    🔍 &nbsp;Lead Sports Planner<br>
    ✅ &nbsp;Resource Validator<br>
    📝 &nbsp;Chief Sports Editor<br>
    ✍️ &nbsp;<span style='color:#d97757; font-weight:600;'>Elite Content Writer</span>
    <span style='font-size:0.65rem; background:linear-gradient(135deg,rgba(217,119,87,0.2),rgba(249,115,22,0.1));
    border:1px solid rgba(217,119,87,0.35); color:#f4a47a; border-radius:6px; padding:1px 7px; margin-left:4px;'>NEW</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.72rem; color:#2a3350; text-align:center; line-height:2; letter-spacing:0.5px;'>
    CrewAI &nbsp;·&nbsp; Gemini 2.5 Flash<br>
    ChromaDB &nbsp;·&nbsp; Streamlit<br>
    Docker &nbsp;·&nbsp; AWS EC2
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style='padding: 0.5rem 0 0.3rem;'>
    <h1>SportsCraft AI</h1>
    <div class='accent-line'></div>
    <p style='color:#6b7fa3; font-size:0.95rem; margin:0; font-weight:400; font-family:"Outfit",sans-serif; letter-spacing:0.3px;'>
        Intelligent Sports Analysis &amp; Content Generation &nbsp;·&nbsp; Powered by Gemini 2.5 Flash
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab_analysis, tab_generator, tab_vault = st.tabs([
    "⚡  Sports Analysis",
    "✍️  Content Generator",
    "🗄️  Content Vault"
])

# ══════════════════════════════════════════════
#  TAB 1 — SPORTS ANALYSIS
# ══════════════════════════════════════════════
with tab_analysis:
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card' style='margin-bottom:1.5rem;'>
    <div style='font-family:"Syne",sans-serif; font-size:1rem; font-weight:700; color:#f0f4ff; margin-bottom:0.3rem;'>
        🎯 Analysis Request
    </div>
    <div style='font-size:0.83rem; color:#4a5578; font-family:"Outfit",sans-serif;'>
        Multi-agent AI research powered by real-time web search
    </div>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        user_goal = st.text_input(
            "goal_input", label_visibility="collapsed",
            placeholder="e.g., Analyze India's batting performance in the 2024 T20 World Cup"
        )
    with col2:
        execute = st.button("🚀 Analyze", type="primary", use_container_width=True)

    if execute:
        if not user_goal:
            st.warning("Please enter a goal first.")
        else:
            planner_agent.step_callback  = streamlit_callback
            analyst_agent.step_callback  = streamlit_callback
            reporter_agent.step_callback = streamlit_callback

            with st.status("🧠 Orchestrating Agents...", expanded=True) as status:
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
                    status.update(label="✅ Analysis Complete!", state="complete")

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
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card' style='margin-bottom:1.5rem;'>
    <div style='font-family:"Syne",sans-serif; font-size:1rem; font-weight:700; color:#f0f4ff; margin-bottom:0.3rem;'>
        ✍️ Sports Content Generator
    </div>
    <div style='font-size:0.83rem; color:#4a5578; font-family:"Outfit",sans-serif;'>
        Transform topics into publication-ready sports content using advanced prompt engineering
    </div>
</div>
""", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="section-label">📌 Content Type</div>', unsafe_allow_html=True)
        content_type = st.selectbox(
            "content_type", label_visibility="collapsed",
            options=["Match Recap", "Player Profile", "Pre-Match Analysis", "Season Review"],
            format_func=lambda x: {
                "Match Recap": "⚽  Match Recap",
                "Player Profile": "🏃  Player Profile",
                "Pre-Match Analysis": "📊  Pre-Match Analysis",
                "Season Review": "🏆  Season Review"
            }[x]
        )

        st.markdown('<div class="section-label" style="margin-top:1.2rem;">🏅 Sport</div>', unsafe_allow_html=True)
        sport = st.selectbox(
            "sport", label_visibility="collapsed",
            options=["Cricket", "Football (Soccer)", "Basketball", "Tennis", "Hockey", "Rugby", "Kabaddi", "Baseball"]
        )

        st.markdown('<div class="section-label" style="margin-top:1.2rem;">🎙️ Tone</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            "tone", label_visibility="collapsed",
            options=["Dramatic", "Journalistic", "Analytical", "Casual"],
            format_func=lambda x: {
                "Dramatic": "⚡  Dramatic",
                "Journalistic": "📰  Journalistic",
                "Analytical": "📋  Analytical",
                "Casual": "😄  Casual"
            }[x]
        )

    with col_right:
        st.markdown('<div class="section-label">🎯 Topic / Match</div>', unsafe_allow_html=True)
        topic = st.text_input(
            "topic", label_visibility="collapsed",
            placeholder="e.g., India vs Australia — 3rd Test, Brisbane"
        )

        st.markdown('<div class="section-label" style="margin-top:1.2rem;">📝 Key Details / Stats</div>', unsafe_allow_html=True)
        details = st.text_area(
            "details", label_visibility="collapsed",
            placeholder="e.g., India won by 6 wickets. Shubman Gill scored 91*, Bumrah took 5/72. Australia were bowled out for 212.",
            height=140
        )

    st.markdown("---")
    gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
    with gen_col2:
        generate = st.button("⚡  GENERATE CONTENT", type="primary", use_container_width=True)

    if generate:
        if not topic.strip():
            st.warning("Please enter a topic or match name.")
        else:
            content_writer_agent.step_callback = streamlit_callback
            planner_agent.step_callback         = streamlit_callback
            analyst_agent.step_callback         = streamlit_callback

            with st.status(f"✍️ Writing {content_type}...", expanded=True) as gen_status:
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
                        verbose=True
                    )
                    with st.spinner("Agents are crafting your content..."):
                        result = crew.kickoff(inputs={'current_time': now})
                    gen_status.update(label="✅ Content Ready!", state="complete")

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
                        st.markdown(f'<span class="type-pill">{content_type} &nbsp;·&nbsp; {sport} &nbsp;·&nbsp; {tone}</span>', unsafe_allow_html=True)
                        st.markdown(f"### {topic}")
                    with head_col2:
                        word_count = len(final_content.split())
                        st.metric("Words", word_count)

                    st.markdown(f'<div class="result-card">{final_content}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Generation Error: {e}")

    if "last_generated" in st.session_state:
        st.markdown("---")
        save_col1, save_col2, save_col3 = st.columns([1, 2, 1])
        with save_col2:
            if st.button("💾  Save to Content Vault", use_container_width=True):
                data = st.session_state["last_generated"]
                doc_id = vs.save_content(
                    content_type=data["content_type"],
                    topic=data["topic"],
                    sport=data["sport"],
                    tone=data["tone"],
                    body=data["body"]
                )
                st.success(f"✅ Saved to Content Vault! ID: `{doc_id}`")
                del st.session_state["last_generated"]
                st.rerun()

# ══════════════════════════════════════════════
#  TAB 3 — CONTENT VAULT
# ══════════════════════════════════════════════
with tab_vault:
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
<div class='glass-card' style='margin-bottom:1.5rem;'>
    <div style='font-family:"Syne",sans-serif; font-size:1rem; font-weight:700; color:#f0f4ff; margin-bottom:0.3rem;'>
        🗄️ Content Vault
    </div>
    <div style='font-size:0.83rem; color:#4a5578; font-family:"Outfit",sans-serif;'>
        All generated content stored in ChromaDB · Semantic search enabled
    </div>
</div>
""", unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([5, 1])
    with search_col1:
        search_query = st.text_input(
            "vault_search", label_visibility="collapsed",
            placeholder="🔍  Search saved content semantically... e.g. 'India batting collapse'"
        )
    with search_col2:
        do_search = st.button("Search", use_container_width=True)

    st.markdown("---")

    if do_search and search_query.strip():
        results = vs.search_similar(search_query, n_results=5)
        if results:
            st.markdown(f"**{len(results)} result(s) for:** *{search_query}*")
            for r in results:
                m = r["meta"]
                with st.expander(f"📄  {m.get('content_type','—')}  ·  {m.get('topic','—')}  ·  {m.get('created_at','—')}"):
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
<div style='text-align:center; padding:3.5rem 1rem;'>
    <div style='
        width:80px; height:80px; border-radius:24px; margin:0 auto 1.2rem;
        background:linear-gradient(135deg,rgba(217,119,87,0.1),rgba(99,102,241,0.08));
        border:1px solid rgba(217,119,87,0.2);
        display:flex; align-items:center; justify-content:center;
        font-size:2rem;
        backdrop-filter:blur(12px);
    '>🗄️</div>
    <p style='font-size:1rem; color:#4a5578; font-family:"Outfit",sans-serif; line-height:1.7;'>
        No content saved yet.<br>
        Generate content and click <strong style='color:#cbd5e1;'>Save to Content Vault</strong>.
    </p>
</div>
""", unsafe_allow_html=True)
        else:
            for item in reversed(saved):
                m = item["meta"]
                with st.expander(f"📄  {m.get('content_type','—')}  ·  {m.get('topic','—')}  ·  {m.get('created_at','—')}"):
                    st.markdown(f'<span class="type-pill">{m.get("content_type")} · {m.get("sport")} · {m.get("tone")}</span>', unsafe_allow_html=True)
                    st.markdown(item["body"])
                    if st.button("🗑️ Delete this entry", key=f"del_{item['id']}"):
                        vs.delete_content(item["id"])
                        st.rerun()

# ── Footer ──
st.markdown("""
<div style='text-align:center; padding:2.5rem 0 1rem; margin-top:2rem;
            border-top:1px solid rgba(255,255,255,0.05);'>
    <div style='font-size:0.72rem; color:#2a3350; font-family:"Syne",sans-serif;
                letter-spacing:3px; font-weight:600; text-transform:uppercase;'>
        SportsCraft AI &nbsp;·&nbsp; GAI-10 &nbsp;·&nbsp; Group 10D5 &nbsp;·&nbsp; Medicaps University &nbsp;·&nbsp; Datagami 2026
    </div>
</div>
""", unsafe_allow_html=True)