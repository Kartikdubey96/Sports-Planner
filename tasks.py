from crewai import Task

# ─────────────────────────────────────────────
#  PROMPT ENGINEERING TEMPLATES
#  GAI-10: Sophisticated, structured prompts
#  that enforce tone, format & terminology
# ─────────────────────────────────────────────

CONTENT_SYSTEM_TEMPLATE = """
You are operating as a {role} for a world-class sports media organisation.

PERSONA:
- Voice: {tone} — maintain this tone throughout without deviation
- Expertise: Deep knowledge of {sport} statistics, tactics, and terminology
- Output Quality: Publication-ready, zero tolerance for vague language

STRICT OUTPUT RULES:
1. NEVER hallucinate scores, player names, or statistics
2. ALWAYS use sport-specific professional terminology for {sport}
3. Structure output in clean Markdown with clear section headers
4. If data is unavailable, write "Data Unavailable" — never invent facts
5. Do NOT use <think> tags, filler phrases, or meta-commentary
"""

CONTENT_TYPE_INSTRUCTIONS = {
    "Match Recap": """
FORMAT TEMPLATE FOR MATCH RECAP:
## 🏆 {MATCH TITLE} — Final Score: X–Y
**Date** | **Venue** | **Competition**
### First Half / First Innings
[Key moments, goals/wickets, tactical shifts]
### Second Half / Second Innings  
[Key moments, turning points, standout performers]
### Player of the Match
[Name + specific stats justifying selection]
### Key Statistics
| Metric | Team A | Team B |
|--------|--------|--------|
### Post-Match Analysis
[2–3 sentences on what this result means for standings/series]
""",
    "Player Profile": """
FORMAT TEMPLATE FOR PLAYER PROFILE:
## 👤 {PLAYER NAME} — {ROLE/POSITION}
**Team** | **Nationality** | **Age**
### Career Overview
[Key career milestones, playing style, strengths]
### Current Season Performance
| Metric | Value |
|--------|-------|
### Tactical Analysis
[How the player impacts team structure and strategy]
### Quote / Reputation
[Notable quote or peer recognition — clearly attributed]
""",
    "Pre-Match Analysis": """
FORMAT TEMPLATE FOR PRE-MATCH ANALYSIS:
## 🔍 Preview: {TEAM A} vs {TEAM B}
**Date** | **Venue** | **Stakes**
### Head-to-Head Record
[Recent meetings, home/away splits]
### Form Guide (Last 5)
- {Team A}: W/L/D sequence
- {Team B}: W/L/D sequence
### Key Battles to Watch
1. [Player vs Player / Bowler vs Batsman etc.]
2. [Tactical matchup]
### Predicted Lineup Impact
[Injuries, suspensions, selection dilemmas]
### Verdict
[Confident prediction with reasoning — no hedging]
""",
    "Season Review": """
FORMAT TEMPLATE FOR SEASON REVIEW:
## 📅 {TEAM/LEAGUE} — {SEASON} Season Review
### Season at a Glance
| Metric | Value |
|--------|-------|
### Peak Moments
[Top 3 defining moments of the season with context]
### Player of the Season
[Name + full statistical justification]
### Tactical Evolution
[How the team/competition changed tactically across the season]
### Verdict & Outlook
[Assessment of season success + what comes next]
"""
}


def create_tasks(planner, analyst, reporter, content_type=None, topic=None, sport=None, tone=None):
    """
    Creates CrewAI tasks.
    - If content_type is provided: runs Content Generation pipeline (GAI-10)
    - Otherwise: runs Sports Analysis pipeline (existing feature)
    """

    if content_type and topic and sport and tone:
        # ── GAI-10: CONTENT GENERATION PIPELINE ──
        format_template = CONTENT_TYPE_INSTRUCTIONS.get(content_type, "")
        system_context = CONTENT_SYSTEM_TEMPLATE.format(
            role="Senior Sports Journalist",
            tone=tone,
            sport=sport
        )

        research_task = Task(
            description=f"""
{system_context}

YOUR TASK: Research task for generating a {content_type}.

1. Search the web for the most recent, accurate information about: "{topic}" in {sport}
2. Collect: current scores, player stats, recent form, key events, and quotes
3. Verify all data from at least 2 sources before including it
4. Compile a structured data brief — DO NOT write the final article yet

TOPIC: {topic}
SPORT: {sport}
CONTENT TYPE: {content_type}
CURRENT TIME: {{current_time}}

OUTPUT: A structured data brief with verified facts, statistics, and key talking points.
""",
            expected_output=f"A structured data brief with verified facts and statistics for a {content_type} about {topic} in {sport}.",
            agent=planner
        )

        validation_task = Task(
            description=f"""
{system_context}

YOUR TASK: Validate data quality and check resource availability.

1. Review the research brief from the Planner
2. Use check_resource tool to verify 'MatchStats_DB' is ONLINE
3. Flag any unverified claims or data gaps
4. Confirm the brief is ready for content generation
5. Prepare a final validated brief with confidence scores for each data point

SCHEDULED TIME: {{current_time}}
""",
            expected_output="A validated data brief with resource status and confidence scores for each data point.",
            agent=analyst
        )

        reporting_task = Task(
            description=f"""
{system_context}

YOUR TASK: Write a professional {content_type} about "{topic}" in {sport}.

TONE: {tone} — Every sentence must reflect this tone.
SPORT TERMINOLOGY: Use professional {sport}-specific language throughout.

MANDATORY FORMAT — follow this template exactly:
{format_template}

CRITICAL RULES:
- Use ONLY facts from the validated research brief
- If any data point is missing, write "Data Unavailable" — never invent
- Maintain {tone} tone from first word to last
- Minimum 300 words, maximum 600 words
- End with a punchy closing line that a reader will remember

TOPIC: {topic}
""",
            expected_output=f"A publication-ready {content_type} in {tone} tone about {topic}, formatted in clean Markdown.",
            agent=reporter,
            context=[research_task, validation_task]
        )

        return [research_task, validation_task, reporting_task]

    else:
        # ── ORIGINAL: SPORTS ANALYSIS PIPELINE ──
        research_task = Task(
            description="""
ROLE: Lead Sports Analyst
TASK: Research and plan sports analysis.

1. Use the search tool to find the latest live score and match 
   summary for {goal} on Cricbuzz or similar sites.
2. Based on the real-time data found, break down the next steps 
   for a full statistical analysis (including player form and key partnerships).

RULES:
- Only use verified data from search results
- Do not hallucinate scores or player names
- Current time: {current_time}
""",
            expected_output="A detailed report containing the current live score, match summary, and a 5-step technical plan for deep match analysis.",
            agent=planner
        )

        validation_task = Task(
            description="""
ROLE: Technical Validator
TASK: Validate resources and create execution schedule.

1. Review the analysis plan and match data from the Lead Planner
2. Use the check_resource tool to verify 'MatchStats_DB' is ONLINE
3. Create a realistic 30-minute execution schedule starting at: {current_time}

RULES:
- Adhere strictly to tool call format
- Do not loop or repeat actions
""",
            expected_output="A confirmation of database status and a finalized 30-minute execution timeline starting from {current_time}.",
            agent=analyst
        )

        reporting_task = Task(
            description="""
ROLE: Chief Sports Editor
TASK: Combine all research into a single Executive Report.

Review the match stats from the Planner and the timeline from the Analyst.
Combine into one cohesive markdown report.

CRITICAL: DO NOT invent or hallucinate any sports data.
If match stats are missing, explicitly state 'Data Unavailable'.
""",
            expected_output="""A beautifully formatted Markdown report containing:
1. 🏏 MATCH SUMMARY (exact scores and player names from research)
2. ⚙️ TECHNICAL PLAN (the 5-step analysis plan)
3. 🗄️ DATABASE & TIMELINE (DB status and real-time schedule)""",
            agent=reporter,
            context=[research_task, validation_task]
        )

        return [research_task, validation_task, reporting_task]