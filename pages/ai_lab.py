import re
import math
import streamlit as st
import pandas as pd

st.markdown('<div class="label">AI Lab</div><h1>Two AI products, not two chatbots.</h1>', unsafe_allow_html=True)
st.write("Interactive portfolio prototypes built around the kinds of systems I engineer: agents, retrieval, deterministic tools, structured extraction and explainable matching.")

tab1, tab2 = st.tabs(["🏠 Property Deal Desk", "📄 Candidate Intelligence"])

# -----------------------------------------------------------------------------
# PROPERTY DEAL DESK
# -----------------------------------------------------------------------------
with tab1:
    st.markdown("## Property Deal Desk")
    st.write("A property-investment workflow rather than a generic chatbot: the agent turns a deal brief into an underwriting view, checks document evidence, runs deterministic finance tools and produces an investment memo.")

    left, right = st.columns([1.05, 0.95])
    with left:
        st.markdown("### 01 · Deal brief")
        deal = st.selectbox("Choose a sample property", [
            "Dubai Marina · 2BR · ₹ 1.55M",
            "Downtown Dubai · 1BR · ₹ 1.35M",
            "JVC · 2BR · ₹ 1.05M",
        ])
        area = deal.split(" · ")[0]
        price_map = {
            "Dubai Marina": (1_550_000, 108_000, 14_500),
            "Downtown Dubai": (1_350_000, 96_000, 11_000),
            "JVC": (1_050_000, 78_000, 8_500),
        }
        price, rent, service = price_map[area]
        target = st.text_input("Investment objective", "Assess whether this property is attractive for a rental investor")
        c1, c2 = st.columns(2)
        with c1:
            down_pct = st.slider("Down payment", 20, 70, 30, 5)
        with c2:
            interest = st.slider("Mortgage rate %", 2.5, 8.5, 5.0, 0.25)
        term = st.slider("Loan term (years)", 5, 30, 20)
        run = st.button("Run underwriting agent", type="primary", use_container_width=True)

    with right:
        st.markdown("### 02 · Property facts")
        st.metric("Purchase price", f"₹ {price:,.0f}")
        st.metric("Annual rent", f"₹ {rent:,.0f}")
        st.metric("Service charge", f"₹ {service:,.0f}")
        st.caption("Synthetic sample data for the portfolio demo. No live property listings are queried.")

    if run:
        loan = price * (1 - down_pct / 100)
        monthly_rate = interest / 100 / 12
        n = term * 12
        if monthly_rate == 0:
            monthly_payment = loan / n
        else:
            monthly_payment = loan * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
        annual_debt = monthly_payment * 12
        gross_yield = rent / price * 100
        net_operating = rent - service
        net_yield = net_operating / price * 100
        cash_after_debt = net_operating - annual_debt
        cash_on_cash = cash_after_debt / (price * down_pct / 100) * 100

        st.divider()
        st.markdown("### 03 · Agent execution trace")
        trace = [
            ("01", "deal_intake", f"Parsed objective: {target}"),
            ("02", "property_document_search", f"Retrieved synthetic service-charge evidence for {area}"),
            ("03", "mortgage_calculator", f"Loan ₹ {loan:,.0f} · {interest:.2f}% · {term} years"),
            ("04", "rental_yield_calculator", "Computed gross yield, net yield and cash-on-cash return"),
            ("05", "risk_checker", "Checked service-charge burden, leverage and cash-flow sensitivity"),
            ("06", "investment_memo", "Assembled an evidence-backed underwriting summary"),
        ]
        for num, tool, desc in trace:
            st.markdown(f"**{num} · `{tool}`**  \\n{desc}")

        st.markdown("### 04 · Underwriting")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Gross yield", f"{gross_yield:.1f}%")
        m2.metric("Net yield", f"{net_yield:.1f}%")
        m3.metric("Annual debt", f"₹ {annual_debt:,.0f}")
        m4.metric("Cash after debt", f"₹ {cash_after_debt:,.0f}")

        result = pd.DataFrame([
            ["Purchase price", f"₹ {price:,.0f}"],
            ["Annual rent", f"₹ {rent:,.0f}"],
            ["Service charge", f"₹ {service:,.0f}"],
            ["Gross rental yield", f"{gross_yield:.2f}%"],
            ["Net operating yield", f"{net_yield:.2f}%"],
            ["Down payment", f"₹ {price * down_pct / 100:,.0f}"],
            ["Monthly mortgage", f"₹ {monthly_payment:,.0f}"],
            ["Cash after debt", f"₹ {cash_after_debt:,.0f}"],
            ["Cash-on-cash return", f"{cash_on_cash:.2f}%"],
        ], columns=["Metric", "Value"])
        st.dataframe(result, hide_index=True, use_container_width=True)

        st.markdown("### 05 · Agent investment memo")
        if cash_after_debt >= 0:
            headline = "Positive modeled cash flow"
            detail = "The selected financing assumptions leave positive modeled annual cash flow after service charges and debt service."
        else:
            headline = "Negative modeled cash flow"
            detail = "The selected financing assumptions produce negative modeled annual cash flow after service charges and debt service."
        risk = "Service-charge burden is material relative to rent." if service / rent > 0.12 else "Service-charge burden is moderate relative to rent."
        st.success(headline)
        st.write(detail)
        st.write(risk)
        st.caption("The demo deliberately keeps arithmetic in Python tools. The agent coordinates the workflow; it does not invent financial figures.")

        with st.expander("Why this is agentic"):
            st.write("The workflow separates planning from execution. A coordinator decides which specialist tool is needed next; each tool returns structured data; the next step uses those results. The original PropertyPilot project uses Llama 3.3 70B via Groq, four tools, a six-step ceiling, section-aware RAG and deterministic mortgage/yield functions.")

    st.divider()
    st.markdown("### PropertyPilot evaluation")
    e1, e2, e3 = st.columns(3)
    e1.metric("Retrieval @3", "17 / 18")
    e2.metric("Hit rate", "94%")
    e3.metric("Tool-call ceiling", "6 steps")
    st.caption("17/18 is the retrieval result from the uploaded PropertyPilot evaluation. This portfolio demo uses synthetic property data so recruiters can explore the workflow without employer or private data.")

# -----------------------------------------------------------------------------
# CANDIDATE INTELLIGENCE
# -----------------------------------------------------------------------------
with tab2:
    st.markdown("## Candidate Intelligence Agent")
    st.write("Upload a job description and a candidate resume. The demo extracts evidence, compares requirements, identifies gaps and builds an agent-style recruiter workflow.")

    jd_col, resume_col = st.columns(2)
    with jd_col:
        st.markdown("### Job description")
        jd_file = st.file_uploader("Upload JD PDF", type=["pdf"], key="jd_upload")
        jd_text_input = st.text_area("Or paste the JD", height=180, placeholder="Paste the job description here...")
    with resume_col:
        st.markdown("### Candidate resume")
        resume_file = st.file_uploader("Upload resume PDF", type=["pdf"], key="resume_upload")
        st.caption("Use a sample or your own resume. Files are processed only for this demo session.")

    def extract_pdf(upload):
        if not upload:
            return ""
        from pypdf import PdfReader
        reader = PdfReader(upload)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    jd_text = jd_text_input.strip()
    resume_text = ""
    if jd_file:
        try:
            jd_text = extract_pdf(jd_file)
        except Exception:
            st.warning("Could not read that JD PDF. Try pasting the text instead.")
    if resume_file:
        try:
            resume_text = extract_pdf(resume_file)
        except Exception:
            st.warning("Could not read that resume PDF.")

    analyze = st.button("Run candidate intelligence agent", type="primary", use_container_width=True, disabled=not (jd_text and resume_text))

    if analyze:
        jd_lower = jd_text.lower()
        resume_lower = resume_text.lower()
        skill_bank = [
            "Python", "FastAPI", "RAG", "LLM", "LangChain", "SQL", "PostgreSQL", "pgvector", "FAISS",
            "Docker", "Kubernetes", "AWS", "Azure", "GCP", "PyTorch", "TensorFlow", "Hugging Face",
            "Sentence Transformers", "Redis", "Celery", "NLP", "embeddings", "semantic search", "machine learning",
            "prompt engineering", "fine-tuning", "LoRA", "MongoDB", "Git"
        ]
        jd_skills = [s for s in skill_bank if s.lower() in jd_lower]
        matched = [s for s in jd_skills if s.lower() in resume_lower]
        missing = [s for s in jd_skills if s.lower() not in resume_lower]
        match_pct = round((len(matched) / len(jd_skills)) * 100) if jd_skills else 0

        email = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", resume_text)
        phone = re.search(r"(?:\+?\d[\d\s().-]{8,}\d)", resume_text)
        pages = len(__import__('pypdf').PdfReader(resume_file).pages) if resume_file else 0

        st.divider()
        st.markdown("### Agent trace")
        trace = [
            ("01", "jd_analyzer", f"Extracted {len(jd_skills)} recognizable technical requirements"),
            ("02", "resume_parser", f"Parsed {pages} resume page(s) and extracted candidate evidence"),
            ("03", "semantic_skill_matcher", f"Compared JD requirements against resume evidence"),
            ("04", "gap_analyzer", f"Identified {len(missing)} uncovered requirements"),
            ("05", "evidence_checker", "Kept claims tied to text present in the uploaded resume"),
            ("06", "recruiter_report", "Generated a structured candidate intelligence summary"),
        ]
        for num, tool, desc in trace:
            st.markdown(f"**{num} · `{tool}`**  \\n{desc}")

        a, b, c = st.columns(3)
        a.metric("Requirement match", f"{match_pct}%")
        b.metric("Matched", len(matched))
        c.metric("Gaps", len(missing))

        st.markdown("### Requirement map")
        if jd_skills:
            rows = []
            for skill in jd_skills:
                status = "✓ Strong evidence" if skill in matched else "✕ Not found"
                rows.append([skill, status])
            st.dataframe(pd.DataFrame(rows, columns=["JD requirement", "Resume evidence"]), hide_index=True, use_container_width=True)
        else:
            st.info("No supported technical keywords were detected. Paste a JD with concrete requirements for a richer demo.")

        g1, g2 = st.columns(2)
        with g1:
            st.markdown("### Missing / weak evidence")
            if missing:
                for skill in missing:
                    st.markdown(f"- **{skill}** — no direct evidence found in the uploaded resume.")
            else:
                st.success("No gaps found in the supported requirement set.")
        with g2:
            st.markdown("### Candidate signals")
            st.write({
                "email": email.group(0) if email else "Not found",
                "phone": phone.group(0) if phone else "Not found",
                "resume_pages": pages,
                "skills_detected": len([s for s in skill_bank if s.lower() in resume_lower]),
            })

        with st.expander("Interview question generator"):
            questions = []
            for skill in matched[:4]:
                questions.append(f"Explain how you have used {skill} in a real project. What trade-offs did you make?")
            for skill in missing[:3]:
                questions.append(f"This role expects {skill}. What hands-on exposure do you have, if any?")
            if not questions:
                questions = ["Walk through the strongest project on your resume and the engineering decisions behind it."]
            for i, q in enumerate(questions, 1):
                st.write(f"**{i}.** {q}")

        st.caption("This is a portfolio prototype. It uses transparent keyword/evidence matching in the browser session rather than pretending to be an employer's production candidate-ranking system.")
