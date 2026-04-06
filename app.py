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
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700;800&display=swap');

/* ── CSS Variables ── */
:root {
    --bg:           #1e2130;
    --shadow-dark:  #15181f;
    --shadow-light: #272b3e;
    --text-1:       #e2e8f0;
    --text-2:       #7f8fa6;
    --text-3:       #4a5568;
    --accent:       #6c63ff;
    --accent-glow:  rgba(108, 99, 255, 0.15);
    --neu-out:      8px 8px 16px #15181f, -8px -8px 16px #272b3e;
    --neu-in:       inset 4px 4px 10px #15181f, inset -4px -4px 10px #272b3e;
    --neu-out-sm:   4px 4px 10px #15181f, -4px -4px 10px #272b3e;
    --neu-in-sm:    inset 3px 3px 6px #15181f, inset -3px -3px 6px #272b3e;
    --radius:       16px;
    --radius-sm:    10px;
}

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Nunito', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text-1) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg) !important;
    border-right: none !important;
    box-shadow: 6px 0 20px #15181f !important;
}
[data-testid="stSidebar"] * { color: var(--text-2) !important; }
[data-testid="stSidebarContent"] { padding: 1.8rem 1.2rem !important; }

/* ── Main block ── */
.main .block-container {
    padding: 2.5rem 3rem 5rem !important;
    max-width: 1100px !important;
    background: var(--bg) !important;
}

/* ── Headings ── */
h1 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
    color: var(--text-1) !important;
    line-height: 1.1 !important;
}
h2 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: var(--text-1) !important;
}
h3 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    color: var(--text-1) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 6px !important;
    gap: 6px !important;
    box-shadow: var(--neu-out) !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    color: var(--text-3) !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--text-2) !important;
}
.stTabs [aria-selected="true"] {
    background: var(--bg) !important;
    color: var(--accent) !important;
    box-shadow: var(--neu-in-sm) !important;
    border: none !important;
}

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.9rem !important;
    box-shadow: var(--neu-in) !important;
    transition: box-shadow 0.2s !important;
    padding: 0.75rem 1rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    box-shadow: var(--neu-in), 0 0 0 2px rgba(108,99,255,0.25) !important;
    border: none !important;
    outline: none !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-3) !important;
}

/* ── Selectbox ── */
.stSelectbox div[data-baseweb="select"] > div {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.9rem !important;
    box-shadow: var(--neu-in) !important;
    transition: all 0.2s !important;
}

/* ── Dropdown ── */
div[data-baseweb="popover"],
ul[data-baseweb="menu"],
.st-emotion-cache-11loom0 {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    box-shadow: var(--neu-out) !important;
    padding: 6px !important;
}

li[role="option"],
.st-emotion-cache-17f8zj6,
.st-emotion-cache-15je8ou {
    background: transparent !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-2) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    transition: all 0.15s !important;
    box-shadow: none !important;
}

li[role="option"]:hover,
.st-emotion-cache-17f8zj6:hover {
    background: var(--bg) !important;
    color: var(--accent) !important;
    box-shadow: var(--neu-in-sm) !important;
}

li[aria-selected="true"] {
    background: var(--bg) !important;
    color: var(--accent) !important;
    box-shadow: var(--neu-in-sm) !important;
}

/* ── Primary Button ── */
.stButton > button[kind="primary"] {
    background: var(--bg) !important;
    color: var(--accent) !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.3px !important;
    padding: 0.65rem 1.8rem !important;
    transition: all 0.2s ease !important;
    box-shadow: var(--neu-out) !important;
    text-transform: none !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: var(--neu-out-sm) !important;
    color: var(--accent) !important;
}
.stButton > button[kind="primary"]:active {
    box-shadow: var(--neu-in) !important;
}

/* ── Secondary Button ── */
.stButton > button {
    background: var(--bg) !important;
    color: var(--text-2) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    box-shadow: var(--neu-out-sm) !important;
}
.stButton > button:hover {
    box-shadow: var(--neu-out) !important;
    color: var(--text-1) !important;
}
.stButton > button:active {
    box-shadow: var(--neu-in-sm) !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 1.2rem 1.4rem !important;
    box-shadow: var(--neu-out) !important;
    transition: box-shadow 0.2s !important;
}
[data-testid="stMetric"]:hover {
    box-shadow: var(--neu-out-sm) !important;
}
[data-testid="stMetricLabel"] {
    color: var(--text-3) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
[data-testid="stMetricValue"] {
    color: var(--accent) !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}

/* ── Status ── */
[data-testid="stStatusWidget"] {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    box-shadow: var(--neu-out) !important;
}

/* ── Alerts ── */
.stAlert {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-1) !important;
    box-shadow: var(--neu-out-sm) !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, #15181f, transparent) !important;
    margin: 1.5rem 0 !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    box-shadow: var(--neu-out-sm) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--bg) !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-2) !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    box-shadow: var(--neu-out-sm) !important;
    transition: box-shadow 0.2s !important;
}
.streamlit-expanderHeader:hover {
    box-shadow: var(--neu-in-sm) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--shadow-dark); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-3); }

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Neu card raised ── */
.neu-card {
    background: var(--bg);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem;
    box-shadow: var(--neu-out);
    transition: box-shadow 0.2s;
    margin-bottom: 1.2rem;
}
.neu-card:hover {
    box-shadow: 10px 10px 20px #15181f, -10px -10px 20px #272b3e;
}

/* ── Result card pressed ── */
.result-card {
    background: var(--bg);
    border-radius: var(--radius);
    padding: 1.8rem;
    margin-top: 1rem;
    line-height: 1.8;
    color: var(--text-2);
    font-size: 0.9rem;
    font-family: 'Nunito', sans-serif;
    box-shadow: var(--neu-in);
}

/* ── Type pill ── */
.type-pill {
    display: inline-block;
    background: var(--bg);
    border-radius: 20px;
    padding: 3px 14px;
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 8px;
    font-family: 'Nunito', sans-serif;
    box-shadow: var(--neu-out-sm);
    letter-spacing: 0.3px;
}

/* ── Section label ── */
.section-label {
    font-family: 'Nunito', sans-serif;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: var(--text-3);
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
    background: linear-gradient(90deg, #15181f, transparent);
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
            <div style='font-family:"Nunito",sans-serif; font-size:1.1rem; font-weight:800;
                        color:#e2e8f0; letter-spacing:-0.3px;'>
                🏟️ SportsCraft AI
            </div>
            <div style='font-size:0.72rem; color:#4a5568; margin-top:4px;
                        letter-spacing:0.5px; font-weight:600;'>
                GAI-10 · Group 10D5
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">API Config</div>', unsafe_allow_html=True)
    serper_key = st.text_input("Serper API Key", value="HIDDEN", type="password",
                               help="Required for real-time web search")
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
<div style='font-size:0.8rem; line-height:2.4; color:#4a5568;
            font-family:"Nunito",sans-serif; font-weight:600;'>
    🔍 Lead Sports Planner<br>
    ✅ Resource Validator<br>
    📝 Chief Sports Editor<br>
    ✍️ <span style='color:#6c63ff;'>Elite Content Writer</span>
    <span style='font-size:0.65rem; background:#1e2130;
    box-shadow:2px 2px 4px #15181f,-2px -2px 4px #272b3e;
    color:#6c63ff; border-radius:6px; padding:1px 7px; margin-left:4px;'>NEW</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.72rem; color:#4a5568; line-height:2;
            font-family:"Nunito",sans-serif; font-weight:600;'>
    CrewAI · Gemini 2.5 Flash<br>
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
    <p style='color:#4a5568; font-size:0.85rem; margin-top:0.4rem; font-weight:600;
              font-family:"Nunito",sans-serif; letter-spacing:0.2px;'>
        Intelligent Sports Analysis & Content Generation &nbsp;·&nbsp; Powered by Gemini 2.5 Flash
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
<div class='neu-card'>
    <div style='font-family:"Nunito",sans-serif; font-size:0.9rem; font-weight:800;
                color:#e2e8f0; margin-bottom:0.25rem;'>🎯 Analysis Request</div>
    <div style='font-size:0.8rem; color:#4a5568; font-family:"Nunito",sans-serif; font-weight:600;'>
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
<div class='neu-card'>
    <div style='font-family:"Nunito",sans-serif; font-size:0.9rem; font-weight:800;
                color:#e2e8f0; margin-bottom:0.25rem;'>✍️ Sports Content Generator</div>
    <div style='font-size:0.8rem; color:#4a5568; font-family:"Nunito",sans-serif; font-weight:600;'>
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
                        verbose=True
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
<div class='neu-card'>
    <div style='font-family:"Nunito",sans-serif; font-size:0.9rem; font-weight:800;
                color:#e2e8f0; margin-bottom:0.25rem;'>🗄️ Content Vault</div>
    <div style='font-size:0.8rem; color:#4a5568; font-family:"Nunito",sans-serif; font-weight:600;'>
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
            st.markdown(f"<p style='font-size:0.8rem; color:#4a5568; font-weight:600;'>{len(results)} result(s) for <em>{search_query}</em></p>", unsafe_allow_html=True)
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
    <div style='font-size:2.5rem; margin-bottom:1rem; opacity:0.15;'>🗄️</div>
    <p style='font-size:0.85rem; color:#4a5568; font-family:"Nunito",sans-serif;
              font-weight:600; line-height:1.8;'>
        No content saved yet.<br>
        Generate content and click <strong style='color:#6c63ff;'>Save to Content Vault</strong>.
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
<div style='text-align:center; padding:3rem 0 1rem; margin-top:2rem;'>
    <div style='font-size:0.72rem; color:#4a5568; font-family:"Nunito",sans-serif;
                font-weight:700; letter-spacing:0.5px;'>
        SportsCraft AI · GAI-10 · Group 10D5 · Medicaps University · Datagami 2026
    </div>
</div>
""", unsafe_allow_html=True)