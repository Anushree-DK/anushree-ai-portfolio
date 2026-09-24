import streamlit as st

st.set_page_config(
    page_title="Anushree D K | AI/ML Software Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
:root { --ink:#f5f7fb; --muted:#9aa4b2; --line:#252b36; --card:#121720; --accent:#8ab4ff; }
html, body, [data-testid="stAppViewContainer"] { background:#080b10; color:var(--ink); }
[data-testid="stHeader"] { background:rgba(8,11,16,.88); }
.block-container { max-width:1180px; padding:42px 34px 80px; }
[data-testid="stSidebar"] { background:#0b0f15; }
h1,h2,h3 { letter-spacing:-.035em; }
.hero-kicker { color:var(--accent); font-weight:700; letter-spacing:.16em; font-size:.78rem; text-transform:uppercase; }
.hero-title { font-size:clamp(3rem,7vw,6.8rem); line-height:.92; font-weight:800; margin:.25rem 0 1rem; }
.hero-sub { color:#c7ced9; font-size:1.2rem; max-width:760px; line-height:1.65; }
.pill { display:inline-block; border:1px solid var(--line); background:#0e131b; padding:7px 11px; border-radius:999px; margin:4px 5px 4px 0; color:#cbd3df; font-size:.86rem; }
.card { background:linear-gradient(180deg,#121720,#0e131a); border:1px solid var(--line); border-radius:18px; padding:24px; height:100%; }
.card h3 { margin-top:0; }
.label { color:var(--muted); text-transform:uppercase; letter-spacing:.13em; font-size:.72rem; font-weight:700; }
.metric { font-size:2rem; font-weight:800; margin-top:5px; }
.small { color:var(--muted); line-height:1.6; }
.section { margin-top:72px; margin-bottom:22px; }
a { color:var(--accent) !important; text-decoration:none; }
[data-testid="stPageLink"] a { color:inherit !important; }
div[data-testid="stButton"] > button { border-radius:12px; }
hr { border-color:var(--line); }
</style>
""", unsafe_allow_html=True)

pg = st.navigation({
    "Portfolio": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/experience.py", title="Experience", icon="💼"),
        st.Page("pages/ai_lab.py", title="AI Lab", icon="🧪"),
        st.Page("pages/resume.py", title="Resume", icon="📄"),
        st.Page("pages/contact.py", title="Contact", icon="↗"),
    ]
})
pg.run()
