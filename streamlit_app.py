
import streamlit as st
import re

st.set_page_config(
    page_title="Anushree D K | AI/ML Engineer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Custom design ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
  --ink: #10131a;
  --muted: #687080;
  --line: rgba(16,19,26,.11);
  --accent: #6757f5;
  --accent2: #9b7cff;
  --soft: #f5f3ff;
}

html, body, [class*="css"] {
  font-family: "DM Sans", sans-serif;
  color: var(--ink);
}

h1,h2,h3,h4 {
  font-family: "Space Grotesk", sans-serif !important;
}

.block-container {
  max-width: 1180px;
  padding: 2rem 2rem 5rem;
}

.hero {
  padding: 5rem 0 3rem;
}

.kicker {
  font-size: .78rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--accent);
}

.hero h1 {
  font-size: clamp(3.1rem, 7vw, 6.7rem) !important;
  line-height: .92 !important;
  letter-spacing: -.07em;
  margin: .65rem 0 1.3rem !important;
}

.hero .lead {
  max-width: 820px;
  font-size: 1.22rem;
  line-height: 1.8;
  color: var(--muted);
}

.badges { margin-top: 1.5rem; }
.badge {
  display:inline-block;
  border:1px solid var(--line);
  border-radius:999px;
  padding:.48rem .78rem;
  margin:.18rem .2rem .18rem 0;
  background:#fff;
  font-size:.83rem;
}

.section {
  padding: 3.7rem 0 1.2rem;
}

.section-label {
  font-size:.76rem;
  letter-spacing:.14em;
  text-transform:uppercase;
  color:var(--accent);
  font-weight:700;
  margin-bottom:.35rem;
}

.card {
  border:1px solid var(--line);
  border-radius:24px;
  padding:1.35rem 1.45rem;
  background:rgba(255,255,255,.78);
  height:100%;
  box-shadow:0 12px 40px rgba(20,20,40,.045);
}

.card:hover {
  border-color:rgba(103,87,245,.3);
}

.project-card {
  border:1px solid var(--line);
  border-radius:26px;
  padding:1.5rem;
  background:linear-gradient(135deg,#fff 0%,#faf9ff 100%);
  min-height:250px;
}

.project-tag {
  font-size:.74rem;
  font-weight:700;
  color:var(--accent);
  text-transform:uppercase;
  letter-spacing:.09em;
}

.project-card h3 { margin:.55rem 0 .65rem; }

.muted { color:var(--muted); line-height:1.7; }

.big-number {
  font-family:"Space Grotesk",sans-serif;
  font-size:2.2rem;
  font-weight:700;
  line-height:1;
}

.stat-label { color:var(--muted); font-size:.86rem; margin-top:.4rem; }

.arch {
  padding:1.1rem;
  border-radius:18px;
  background:#11131a;
  color:#fff;
  font-family:monospace;
  line-height:1.9;
  overflow-x:auto;
}

.arch .a { color:#b7adff; }
.arch .b { color:#ffffff; }
.arch .c { color:#9ea7b8; }

.timeline {
  border-left:2px solid rgba(103,87,245,.2);
  padding-left:1.3rem;
  margin-left:.3rem;
}

.timeline-item { margin-bottom:1.8rem; }
.timeline-item:before {
  content:"";
  display:block;
  width:10px;
  height:10px;
  border-radius:50%;
  background:var(--accent);
  position:relative;
  left:-1.68rem;
  top:1.1rem;
}

.quote {
  border-left:4px solid var(--accent);
  padding:.8rem 1rem;
  background:var(--soft);
  border-radius:0 14px 14px 0;
  color:#343044;
}

div[data-testid="stTabs"] button {
  font-weight:600;
}

footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<section class="hero">
<div class="kicker">AI / ML SOFTWARE ENGINEER</div>
<h1>Anushree<br>D K<span style="color:#6757f5">.</span></h1>
<p class="lead">
I build production-oriented AI applications across <b>LLMs, RAG, semantic search,
structured extraction and Python APIs</b> — with an emphasis on grounded,
explainable and reliable AI.
</p>
<div class="badges">
<span class="badge">Python</span>
<span class="badge">RAG</span>
<span class="badge">LLM APIs</span>
<span class="badge">FastAPI</span>
<span class="badge">Embeddings</span>
<span class="badge">PyTorch</span>
<span class="badge">Docker</span>
</div>
</section>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.link_button("LinkedIn ↗","https://linkedin.com/in/anushree-dk-644516220",use_container_width=True)
with c2: st.link_button("GitHub ↗","https://github.com/Anushree-DK",use_container_width=True)
with c3: st.link_button("Email ↗","mailto:anugowda612@gmail.com",use_container_width=True)
with c4: st.link_button("Open to relocation ↗","https://linkedin.com/in/anushree-dk-644516220",use_container_width=True)

# ---------- Snapshot ----------
st.markdown('<div class="section"><div class="section-label">01 — Snapshot</div><h2>AI engineering, end to end.</h2></div>', unsafe_allow_html=True)
cols=st.columns(4)
stats=[("96%","name-extraction accuracy"),("2","production LLM modules"),("Mistral-7B","LoRA fine-tuning"),("M.Tech","Automation & Robotics")]
for col,(num,label) in zip(cols,stats):
    with col:
        st.markdown(f'<div class="card"><div class="big-number">{num}</div><div class="stat-label">{label}</div></div>',unsafe_allow_html=True)

# ---------- About ----------
st.markdown('<div class="section"><div class="section-label">02 — About</div><h2>From model calls to usable systems.</h2></div>', unsafe_allow_html=True)
a,b=st.columns([1.35,1])
with a:
    st.markdown("""
    <div class="card">
    <p class="muted">
    My work sits at the intersection of <b>applied machine learning and software engineering</b>.
    I have built LLM modules for enterprise intelligence and recruiting workflows, including
    self-hosted inference, RAG, semantic retrieval, structured extraction, classification,
    fine-tuning and API-driven services.
    </p>
    <p class="muted">
    I care about the parts that make AI useful in real products: keeping sensitive data in-house,
    making outputs explainable, constraining hallucinations, preserving human edits and choosing
    models based on latency and cost.
    </p>
    <div class="quote">Personal portfolio work is kept separate from employer-confidential code and data.</div>
    </div>
    """,unsafe_allow_html=True)
with b:
    st.markdown("""
    <div class="card">
    <h3>Core strengths</h3>
    <p>LLM application engineering</p>
    <p>RAG & semantic search</p>
    <p>Structured extraction</p>
    <p>Python / FastAPI backends</p>
    <p>Self-hosted LLM workflows</p>
    <p>LLM evaluation & prompt design</p>
    <p>LoRA fine-tuning</p>
    <p>Production-oriented Docker services</p>
    </div>
    """,unsafe_allow_html=True)

# ---------- Experience ----------
st.markdown('<div class="section"><div class="section-label">03 — Experience</div><h2>Professional work</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="timeline">',unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
<h3>Aritrak Technologies Pvt Ltd</h3>
<b>AI/ML Software Engineer · Nov 2025 – Present</b>
<p class="muted">Build LLM modules for EIOS and Smart Recruit.</p>
<ul>
<li>Deployed self-hosted Ollama across production modules for embeddings, extraction, summarisation, classification and generation.</li>
<li>Built RAG from scratch using semantic chunking, embeddings and cosine-similarity retrieval with anti-hallucination prompting.</li>
<li>Designed dual-source answers using internal RAG and live web search while keeping sources separate.</li>
<li>Built hybrid candidate scoring using embedding similarity plus deterministic keyword matching for explainability.</li>
<li>Built strict-JSON resume extraction, length-capped summaries and an LLM email reply-intent classifier.</li>
<li>Built Smart Recruit with FastAPI, Celery, PostgreSQL/pgvector, Redis and Docker Compose; Groq parsing with an Ollama fallback reached 96% name-extraction accuracy.</li>
<li>Built a LoRA fine-tuning pipeline for Mistral-7B on RunPod with API orchestration and MongoDB job tracking.</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="timeline-item">
<h3>Tescom Technologies Pvt Ltd</h3>
<b>AI/ML Intern · May 2025 – Sep 2025</b>
<p class="muted">Worked on educational AI applications and Python/ML training.</p>
<ul>
<li>Integrated Anthropic Claude API in Python for question answering, explanations and content summarisation.</li>
<li>Designed structured prompts and evaluated outputs for relevance, accuracy and consistency.</li>
<li>Delivered Python and machine learning labs and mentored students on computer vision and NLP.</li>
</ul>
</div>
""",unsafe_allow_html=True)
st.markdown('</div>',unsafe_allow_html=True)

# ---------- Featured demo ----------
st.markdown('<div class="section"><div class="section-label">04 — Interactive demo</div><h2>Property Intelligence Assistant</h2></div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
<p class="muted">
A <b>personal portfolio prototype</b> showing how a property-document assistant can
retrieve evidence before answering. This is not employer code and uses synthetic sample content.
</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="arch">
<span class="a">PROPERTY PDF</span>
&nbsp;→&nbsp; <span class="b">TEXT EXTRACTION</span>
&nbsp;→&nbsp; <span class="b">SEMANTIC CHUNKS</span>
&nbsp;→&nbsp; <span class="b">EMBEDDINGS</span>
&nbsp;→&nbsp; <span class="b">RETRIEVAL</span>
&nbsp;→&nbsp; <span class="a">GROUNDED ANSWER</span>
</div>
""",unsafe_allow_html=True)

sample=[
("Payment milestones","The sample purchase price is payable in four milestones: 10% on reservation, 20% on signing, 30% at the construction milestone, and 40% on handover."),
("Handover","The expected handover window in the sample document is Q4 2027, subject to the agreement's stated conditions."),
("Service charges","Estimated annual service charges for the sample property are AED 18,000. Actual charges may vary by unit and community."),
("Required documents","The sample onboarding checklist requests passport identification, proof of address and signed reservation documentation."),
("Early termination","Early termination is subject to the conditions and notice period defined in the sample agreement.")
]
questions=[
"What are the payment milestones?",
"When is the expected handover?",
"What are the service charges?",
"What documents are required?",
"What happens if I terminate early?"
]
q=st.selectbox("Ask the assistant",questions)
if st.button("Retrieve evidence & answer",type="primary"):
    terms=re.findall(r"[a-zA-Z]{4,}",q.lower())
    scored=[]
    for title,body in sample:
        score=sum(1 for t in terms if t in (title+" "+body).lower())
        scored.append((score,title,body))
    scored=sorted(scored,reverse=True)
    hits=[x for x in scored if x[0]>0][:2]
    if hits:
        st.success(" ".join(x[2] for x in hits))
        st.markdown("**Retrieved evidence**")
        for _,title,body in hits:
            st.markdown(f'<div class="quote"><b>{title}</b><br>{body}</div>',unsafe_allow_html=True)
    else:
        st.warning("No supporting evidence found. The assistant should not guess.")

# ---------- Project cards ----------
st.markdown('<div class="section"><div class="section-label">05 — Selected projects</div><h2>What I like building</h2></div>', unsafe_allow_html=True)
p1,p2=st.columns(2)
with p1:
    st.markdown("""
    <div class="project-card">
    <div class="project-tag">LLM / NLP</div>
    <h3>NLP Preference Prediction & LLM Evaluation</h3>
    <p class="muted">Prompt–response datasets, evaluation labels and response-quality metrics designed to make LLM behavior measurable.</p>
    <b>Python · Hugging Face · Evaluation</b>
    </div>
    """,unsafe_allow_html=True)
with p2:
    st.markdown("""
    <div class="project-card">
    <div class="project-tag">Computer Vision</div>
    <h3>Real-time Background Removal</h3>
    <p class="muted">MODNet-based segmentation tested on custom datasets for real-time background removal.</p>
    <b>PyTorch · OpenCV · MODNet</b>
    </div>
    """,unsafe_allow_html=True)

# ---------- Architecture ----------
st.markdown('<div class="section"><div class="section-label">06 — Engineering patterns</div><h2>How I approach reliable AI</h2></div>', unsafe_allow_html=True)
x1,x2,x3=st.columns(3)
for col,title,body in [
    (x1,"Grounding","Retrieve first. Generate from evidence. Keep unsupported claims out of the answer."),
    (x2,"Explainability","Prefer deterministic scoring where a transparent, repeatable score matters."),
    (x3,"Production thinking","Consider privacy, latency, cost, fallbacks, structured outputs and human edits.")
]:
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p class="muted">{body}</p></div>',unsafe_allow_html=True)

# ---------- Stack ----------
st.markdown('<div class="section"><div class="section-label">07 — Toolkit</div><h2>Technical stack</h2></div>',unsafe_allow_html=True)
stack = {
"LLM / GenAI":"Anthropic Claude · Groq · Ollama · Mistral-7B · Llama-3.1-8B · Qwen2.5 · RAG · Prompt Engineering · Structured JSON · Embeddings · Semantic Search · LLM Evaluation · LoRA / Unsloth",
"Backend":"Python · SQL · FastAPI · REST APIs · Celery · Redis · Nginx · Docker · Docker Compose",
"Data / Vector":"PostgreSQL + pgvector · FAISS · ChromaDB · MongoDB · Pandas · NumPy",
"ML / Tools":"PyTorch · TensorFlow · Scikit-learn · Hugging Face · Sentence Transformers · OpenCV · Git · RunPod"
}
for title,body in stack.items():
    st.markdown(f'<div class="card" style="margin-bottom:12px"><b>{title}</b><p class="muted">{body}</p></div>',unsafe_allow_html=True)

# ---------- Education ----------
st.markdown('<div class="section"><div class="section-label">08 — Education</div><h2>Education & certifications</h2></div>',unsafe_allow_html=True)
e1,e2=st.columns(2)
with e1:
    st.markdown("""
    <div class="card">
    <h3>M.Tech, Automation & Robotics</h3>
    <p class="muted">Manipal Institute of Technology, MAHE · 2024–2026</p>
    <h3>B.E., Electronics & Communication Engineering</h3>
    <p class="muted">Sai Vidya Institute of Technology, VTU · 2020–2024</p>
    </div>
    """,unsafe_allow_html=True)
with e2:
    st.markdown("""
    <div class="card">
    <h3>Certifications</h3>
    <p class="muted">IBM AI Engineering Professional Certificate<br>Certified Data Analyst — ExcelR</p>
    <h3>Languages</h3>
    <p class="muted">English · Kannada · Hindi</p>
    </div>
    """,unsafe_allow_html=True)

# ---------- Contact ----------
st.markdown('<div class="section"><div class="section-label">09 — Contact</div><h2>Let's build something useful.</h2></div>',unsafe_allow_html=True)
st.markdown("""
<div class="card">
<p class="muted">
Open to AI/ML and LLM engineering opportunities, including relocation.
For professional opportunities: <b>anugowda612@gmail.com</b>
</p>
</div>
""",unsafe_allow_html=True)
cc1,cc2=st.columns(2)
with cc1: st.link_button("Email Anushree ↗","mailto:anugowda612@gmail.com",use_container_width=True)
with cc2: st.link_button("LinkedIn ↗","https://linkedin.com/in/anushree-dk-644516220",use_container_width=True)

st.divider()
st.caption("© Anushree D K · Personal portfolio · Professional project descriptions are intentionally high-level to protect employer-confidential information.")
