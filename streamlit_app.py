import streamlit as st

st.set_page_config(
    page_title="Anushree D K — AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Global portfolio styling
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        .block-container {
            max-width: 1180px;
            padding-top: 2.5rem;
            padding-bottom: 5rem;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 2rem;
        }

        /* Clean typography */
        h1, h2, h3 {
            letter-spacing: -0.03em;
        }

        /* Buttons */
        .stButton > button,
        .stLinkButton > a {
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.14);
            padding: 0.55rem 1rem;
        }

        /* Cards / bordered containers */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 18px;
        }

        /* Tags */
        .tag {
            display: inline-block;
            padding: 6px 10px;
            margin: 4px 4px 4px 0;
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 999px;
            font-size: 0.82rem;
            background: rgba(255,255,255,0.035);
        }

        /* Mobile spacing */
        @media (max-width: 700px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1.5rem;
            }

            h1 {
                font-size: 2.35rem !important;
            }

            h2 {
                font-size: 1.75rem !important;
            }
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
