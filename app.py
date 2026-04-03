import streamlit as st
import os
import sys
import re
from datetime import datetime

sys.path.append(os.path.dirname(__file__))

# ── Page Config ──
st.set_page_config(
    page_title="SportsCraft AI",
    page_icon="🏟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
#  PREMIUM DARK SPORTS UI
#  Aesthetic: Editorial Sports Magazine
#  Font: Bebas Neue (display) + DM Sans (body)
#  Palette: Near-black bg, amber accent, red alert
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #080b10 !important;
    color: #e2e8f2 !important;
}

/* ── Animated noise texture overlay ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
}

/* ── Grid background ── */
[data-testid="stMain"] {
    background-image:
        linear-gradient(rgba(245,185,50,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(245,185,50,0.04) 1px, transparent 1px);
    background-size: 44px 44px;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid #1e2530 !important;
}
[data-testid="stSidebar"] * { color: #c8cfe0 !important; }
[data-testid="stSidebarContent"] { padding: 1.5rem 1rem !important; }

/* ── Main content padding ── */
.main .block-container {
    padding: 2rem 2.5rem 4rem !important;
    max-width: 1200px !important;
}

/* ── Headings ── */
h1 {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 3.2rem !important;
    letter-spacing: 3px !important;
    color: #f5b932 !important;
    line-height: 1 !important;
    margin-bottom: 0.2rem !important;
    text-shadow: 0 0 40px rgba(245,185,50,0.25) !important;
}
h2 {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.6rem !important;
    letter-spacing: 2px !important;
    color: #e2e8f2 !important;
}
h3 {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.2rem !important;
    letter-spacing: 1.5px !important;
    color: #94a3b8 !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 12px !important;
    padding: 6px !important;
    gap: 6px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1rem !important;
    letter-spacing: 2px !important;
    color: #64748b !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.8rem !important;
    transition: all 0.2s !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: #f5b932 !important;
    color: #080b10 !important;
}

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 10px !important;
    color: #e2e8f2 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    transition: border-color 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #f5b932 !important;
    box-shadow: 0 0 0 3px rgba(245,185,50,0.12) !important;
}

/* ── Primary Button ── */
.stButton > button[kind="primary"], button[kind="primary"] {
    background: #f5b932 !important;
    color: #080b10 !important;
    border: none !important;
    border-radius: 40px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 2px !important;
    padding: 0.65rem 2rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 16px rgba(245,185,50,0.2) !important;
}
.stButton > button[kind="primary"]:hover {
    background: #ffd060 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(245,185,50,0.35) !important;
}

/* ── Secondary Button ── */
.stButton > button {
    background: #131920 !important;
    color: #94a3b8 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    border-color: #f5b932 !important;
    color: #f5b932 !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}
[data-testid="stMetricLabel"] { color: #64748b !important; font-size: 0.8rem !important; }
[data-testid="stMetricValue"] { color: #f5b932 !important; font-family: 'Bebas Neue', sans-serif !important; font-size: 1.8rem !important; letter-spacing: 1px !important; }

/* ── Status / Spinner ── */
[data-testid="stStatusWidget"] {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 14px !important;
}

/* ── Alerts ── */
.stAlert {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 12px !important;
    color: #e2e8f2 !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid #1e2530 !important;
    margin: 1.5rem 0 !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 16px !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #0d1117 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 10px !important;
    color: #94a3b8 !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #1e2530; border-radius: 6px; }
::-webkit-scrollbar-thumb:hover { background: #f5b932; }

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, rgba(245,185,50,0.06), rgba(232,75,58,0.04));
    border: 1px solid rgba(245,185,50,0.2);
    border-radius: 16px;
    padding: 1.8rem;
    margin-top: 1rem;
    line-height: 1.75;
    color: #c8cfe0;
    font-size: 0.95rem;
}

/* ── Saved item card ── */
.saved-card {
    background: #0d1117;
    border: 1px solid #1e2530;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.75rem;
    transition: border-color 0.2s;
}
.saved-card:hover { border-color: rgba(245,185,50,0.3); }

/* ── Type pill ── */
.type-pill {
    display: inline-block;
    background: rgba(245,185,50,0.12);
    border: 1px solid rgba(245,185,50,0.3);
    color: #f5b932;
    border-radius: 20px;
    padding: 2px 12px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}

/* ── Section label ── */
.section-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 2px;
    color: #475569;
    margin-bottom: 0.4rem;
    display: flex;
    align-items: center;
    gap: 6px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e2530;
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
        <div style='text-align:center; padding: 0.5rem 0 1.5rem;'>
            <div style='font-size:2.8rem; margin-bottom:0.3rem;'>🏟️</div>
            <div style='font-family:"Bebas Neue",sans-serif; font-size:1.5rem; letter-spacing:3px; color:#f5b932;'>SportsCraft AI</div>
            <div style='font-size:0.75rem; color:#475569; margin-top:4px;'>GAI-10 · Group 10D5</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">⚙️ API CONFIG</div>', unsafe_allow_html=True)
    serper_key = st.text_input("Serper API Key", value="HIDDEN", type="password",
                               help="Required for real-time web search")
    os.environ["SERPER_API_KEY"] = serper_key

    st.markdown("---")
    st.markdown('<div class="section-label">📊 SYSTEM STATUS</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Agents", "4")
    with col_b:
        st.metric("Saved", str(vs.get_count()))

    st.markdown("---")
    st.markdown('<div class="section-label">🤖 ACTIVE AGENTS</div>', unsafe_allow_html=True)
    st.markdown("""
<div style='font-size:0.82rem; line-height:2; color:#64748b;'>
🔍 &nbsp;Lead Sports Planner<br>
✅ &nbsp;Resource Validator<br>
📝 &nbsp;Chief Sports Editor<br>
✍️ &nbsp;<span style='color:#f5b932;'>Elite Content Writer</span> <span style='font-size:0.7rem; background:rgba(245,185,50,0.1); border:1px solid rgba(245,185,50,0.3); color:#f5b932; border-radius:4px; padding:1px 6px;'>NEW</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.75rem; color:#334155; text-align:center; line-height:1.8;'>
CrewAI · Gemini 2.5 Flash<br>ChromaDB · Streamlit<br>Docker · AWS EC2
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div style='padding: 0.5rem 0 1.5rem;'>
    <h1>SportsCraft AI</h1>
    <p style='color:#475569; font-size:0.95rem; margin:0; font-weight:300;'>
        Intelligent Sports Analysis &amp; Content Generation &nbsp;·&nbsp; Powered by Gemini 2.5 Flash
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab_analysis, tab_generator, tab_vault = st.tabs([
    "⚡  SPORTS ANALYSIS",
    "✍️  CONTENT GENERATOR",
    "🗄️  CONTENT VAULT"
])

# ══════════════════════════════════════════════
#  TAB 1 — SPORTS ANALYSIS (original feature)
# ══════════════════════════════════════════════
with tab_analysis:
    st.markdown("### 🎯 Analysis Request")
    st.markdown('<p style="color:#64748b; font-size:0.88rem; margin-top:-0.5rem;">Multi-agent AI research powered by real-time web search</p>', unsafe_allow_html=True)

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
#  TAB 2 — CONTENT GENERATOR (GAI-10 feature)
# ══════════════════════════════════════════════
with tab_generator:
    st.markdown("### ✍️ Sports Content Generator")
    st.markdown('<p style="color:#64748b; font-size:0.88rem; margin-top:-0.5rem;">Transform topics into publication-ready sports content using advanced prompt engineering</p>', unsafe_allow_html=True)

    # ── Controls ──
    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div class="section-label">📌 CONTENT TYPE</div>', unsafe_allow_html=True)
        content_type = st.selectbox(
            "content_type", label_visibility="collapsed",
            options=["Match Recap", "Player Profile", "Pre-Match Analysis", "Season Review"],
            format_func=lambda x: {
                "Match Recap": "⚽ Match Recap",
                "Player Profile": "🏃 Player Profile",
                "Pre-Match Analysis": "📊 Pre-Match Analysis",
                "Season Review": "🏆 Season Review"
            }[x]
        )

        st.markdown('<div class="section-label" style="margin-top:1rem;">🏅 SPORT</div>', unsafe_allow_html=True)
        sport = st.selectbox(
            "sport", label_visibility="collapsed",
            options=["Cricket", "Football (Soccer)", "Basketball", "Tennis", "Hockey", "Rugby", "Kabaddi", "Baseball"]
        )

        st.markdown('<div class="section-label" style="margin-top:1rem;">🎙️ TONE</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            "tone", label_visibility="collapsed",
            options=["Dramatic", "Journalistic", "Analytical", "Casual"],
            format_func=lambda x: {
                "Dramatic": "⚡ Dramatic",
                "Journalistic": "📰 Journalistic",
                "Analytical": "📋 Analytical",
                "Casual": "😄 Casual"
            }[x]
        )

    with col_right:
        st.markdown('<div class="section-label">🎯 TOPIC / MATCH</div>', unsafe_allow_html=True)
        topic = st.text_input(
            "topic", label_visibility="collapsed",
            placeholder="e.g., India vs Australia — 3rd Test, Brisbane"
        )

        st.markdown('<div class="section-label" style="margin-top:1rem;">📝 KEY DETAILS / STATS</div>', unsafe_allow_html=True)
        details = st.text_area(
            "details", label_visibility="collapsed",
            placeholder="e.g., India won by 6 wickets. Shubman Gill scored 91*, Bumrah took 5/72. Australia were bowled out for 212.",
            height=120
        )

    st.markdown("---")
    gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
    with gen_col2:
        generate = st.button("⚡ GENERATE CONTENT", type="primary", use_container_width=True)

    # ── Generation ──
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

                    # Store in session for save button
                    st.session_state["last_generated"] = {
                        "content_type": content_type,
                        "topic": topic,
                        "sport": sport,
                        "tone": tone,
                        "body": final_content
                    }

                    st.divider()

                    # Header row
                    head_col1, head_col2 = st.columns([3, 1])
                    with head_col1:
                        st.markdown(f"""
<span class="type-pill">{content_type} · {sport} · {tone}</span>
""", unsafe_allow_html=True)
                        st.markdown(f"### {topic}")
                    with head_col2:
                        word_count = len(final_content.split())
                        st.metric("Words", word_count)

                    st.markdown(f'<div class="result-card">{final_content}</div>', unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Generation Error: {e}")

    # ── Save to Vector DB ──
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
                st.success(f"✅ Saved to Content Vault! ID: `{doc_id}`")
                del st.session_state["last_generated"]
                st.rerun()

# ══════════════════════════════════════════════
#  TAB 3 — CONTENT VAULT (Vector DB viewer)
# ══════════════════════════════════════════════
with tab_vault:
    st.markdown("### 🗄️ Content Vault")
    st.markdown('<p style="color:#64748b; font-size:0.88rem; margin-top:-0.5rem;">All generated content stored in ChromaDB · Semantic search enabled</p>', unsafe_allow_html=True)

    # ── Search ──
    search_col1, search_col2 = st.columns([5, 1])
    with search_col1:
        search_query = st.text_input(
            "vault_search", label_visibility="collapsed",
            placeholder="🔍 Search saved content semantically... e.g. 'India batting collapse'"
        )
    with search_col2:
        do_search = st.button("Search", use_container_width=True)

    st.markdown("---")

    # ── Results ──
    if do_search and search_query.strip():
        results = vs.search_similar(search_query, n_results=5)
        if results:
            st.markdown(f"**{len(results)} result(s) for:** *{search_query}*")
            for r in results:
                m = r["meta"]
                with st.expander(f"📄 {m.get('content_type','—')} · {m.get('topic','—')} · {m.get('created_at','—')}"):
                    st.markdown(f'<span class="type-pill">{m.get("content_type")} · {m.get("sport")} · {m.get("tone")}</span>', unsafe_allow_html=True)
                    st.markdown(r["body"])
                    if st.button(f"🗑️ Delete", key=f"del_{r['id']}"):
                        vs.delete_content(r["id"])
                        st.rerun()
        else:
            st.info("No matching content found.")
    else:
        # ── Show all saved ──
        saved = vs.get_all_saved()
        total = vs.get_count()

        v_col1, v_col2, v_col3 = st.columns(3)
        with v_col1: st.metric("Total Saved", total)
        with v_col2:
            types = list(set(s["meta"].get("content_type","") for s in saved)) if saved else []
            st.metric("Content Types", len(types))
        with v_col3:
            sports = list(set(s["meta"].get("sport","") for s in saved)) if saved else []
            st.metric("Sports Covered", len(sports))

        st.markdown("---")

        if not saved:
            st.markdown("""
<div style='text-align:center; padding:3rem; color:#334155;'>
    <div style='font-size:3rem; margin-bottom:1rem;'>🗄️</div>
    <p style='font-size:1rem;'>No content saved yet.<br>Generate content and click <strong style='color:#f5b932;'>Save to Content Vault</strong>.</p>
</div>
""", unsafe_allow_html=True)
        else:
            for item in reversed(saved):
                m = item["meta"]
                with st.expander(f"📄  {m.get('content_type','—')}  ·  {m.get('topic','—')}  ·  {m.get('created_at','—')}"):
                    st.markdown(f'<span class="type-pill">{m.get("content_type")} · {m.get("sport")} · {m.get("tone")}</span>', unsafe_allow_html=True)
                    st.markdown(item["body"])
                    if st.button(f"🗑️ Delete this entry", key=f"del_{item['id']}"):
                        vs.delete_content(item["id"])
                        st.rerun()

# ── Footer ──
st.markdown("""
<div style='text-align:center; padding:2rem 0 1rem; border-top:1px solid #1e2530; margin-top:2rem;'>
    <p style='color:#1e2530; font-size:0.8rem; font-family:"Bebas Neue",sans-serif; letter-spacing:2px;'>
        SPORTSCRAFT AI · GAI-10 · GROUP 10D5 · MEDICAPS UNIVERSITY · DATAGAMI 2026
    </p>
</div>
""", unsafe_allow_html=True)