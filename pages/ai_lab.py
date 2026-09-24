import streamlit as st
import pandas as pd

st.markdown('<div class="label">AI Lab</div><h1>Interactive AI projects.</h1>', unsafe_allow_html=True)
st.write("These are personal demonstrations using synthetic/sample data. Professional systems from Aritrak are described separately under Experience.")

tab1, tab2 = st.tabs(["🏠 PropertyPilot", "📄 Resume Intelligence"])

with tab1:
    st.markdown("## PropertyPilot")
    st.write("An agentic property assistant inspired by the uploaded project: the LLM selects tools, RAG retrieves evidence, listing search finds properties, and Python performs financial calculations.")
    st.markdown("### Try an agent mission")
    mission = st.selectbox("Choose a scenario", [
        "Net yield after service charges",
        "Find 2-bedroom properties under AED 2.2M",
        "Check whether the documents mention a rooftop cinema",
    ])
    if st.button("Run agent mission", type="primary", use_container_width=True):
        st.session_state["mission"] = mission
        st.session_state["run"] = True
    if st.session_state.get("run"):
        q = st.session_state["mission"]
        st.markdown("### 🧠 Agent plan")
        if "yield" in q.lower():
            steps = [
                ("01","find_listings","Locate the requested property"),
                ("02","search_property_documents","Retrieve the relevant service-charge section"),
                ("03","calculate_rental_yield","Calculate net yield with Python"),
                ("04","final_answer","Return a grounded answer with evidence"),
            ]
            answer = "The agent would combine the listing, service-charge evidence and deterministic yield calculation before answering."
        elif "2-bedroom" in q:
            steps = [
                ("01","find_listings","Filter by bedrooms and budget"),
                ("02","find_listings","Sort candidates by yield"),
                ("03","final_answer","Return the matching properties"),
            ]
            answer = "The agent searches the listing table, applies constraints, ranks candidates and returns the matches."
        else:
            steps = [
                ("01","search_property_documents","Search the building documents"),
                ("02","relevance_check","Check whether a supporting passage exists"),
                ("03","final_answer","Refuse to invent information if evidence is absent"),
            ]
            answer = "If the documents do not contain evidence for a rooftop cinema, the agent explicitly says it cannot verify that claim."
        for num,tool,desc in steps:
            st.markdown(f"**{num} · `{tool}`**  \n{desc}")
        st.success(answer)
        st.markdown("### Why this is agentic")
        st.write("The workflow is not a fixed chatbot script: the agent chooses which tool to call, can chain multiple tools, observes their results and then decides whether another tool call is needed. The original project also enforces a six-step ceiling and records every tool call.")
    st.divider()
    st.markdown("### Evaluation")
    a,b,c = st.columns(3)
    a.metric("Retrieval @3","17 / 18")
    b.metric("Hit rate","94%")
    c.metric("Tool rounds","≤ 6")
    st.caption("The 17/18 retrieval result is from the uploaded PropertyPilot evaluation script/README. Agent tool-selection and answer accuracy are evaluated separately when the agent evaluation is run.")
    with st.expander("Architecture"):
        st.code("""User question
      ↓
LLM planner / tool calling
      ↓
┌──────────────┬──────────────┬─────────────────┐
│ Property RAG │ Listing Search│ Python Calculators│
└──────────────┴──────────────┴─────────────────┘
      ↓
Tool results → next decision
      ↓
Grounded answer + agent trace""", language="text")

with tab2:
    st.markdown("## Resume Intelligence")
    st.write("A lightweight portfolio demonstration of structured resume extraction. Upload a PDF and inspect the text plus detected contact/skill signals. No employer data is used.")
    uploaded = st.file_uploader("Upload a sample resume PDF", type=["pdf"])
    if uploaded:
        try:
            from pypdf import PdfReader
            reader = PdfReader(uploaded)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            lower = text.lower()
            import re
            email = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
            phone = re.search(r"(?:\+?\d[\d\s().-]{8,}\d)", text)
            skills = ["Python","FastAPI","RAG","LLM","SQL","Docker","PostgreSQL","PyTorch","TensorFlow","Power BI","Tableau","Hugging Face","Sentence Transformers"]
            found = [s for s in skills if s.lower() in lower]
            c1,c2,c3 = st.columns(3)
            c1.metric("Pages", len(reader.pages))
            c2.metric("Skills detected", len(found))
            c3.metric("Email", "Found" if email else "Not found")
            st.markdown("### Structured signals")
            st.write({"email": email.group(0) if email else None, "phone": phone.group(0) if phone else None, "skills": found})
            with st.expander("Extracted text"):
                st.text(text[:12000])
        except Exception as exc:
            st.error(f"Could not parse this PDF: {type(exc).__name__}")
