import streamlit as st

st.set_page_config(
    page_title="Anushree D K — AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid rgba(255,255,255,0.08);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

pages = {
    "Portfolio": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/experience.py", title="Experience", icon="💼"),
        st.Page("pages/ai_lab.py", title="AI Lab", icon="🧪"),
        st.Page("pages/resume.py", title="Resume", icon="📄"),
        st.Page("pages/contact.py", title="Contact", icon="✉️"),
    ]
}

pg = st.navigation(pages)
pg.run()
