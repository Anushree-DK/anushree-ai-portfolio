import streamlit as st

st.markdown(
    '<div class="label">PROFESSIONAL EXPERIENCE</div>'
    '<h1>Building AI systems in production.</h1>'
    '<div class="small" style="max-width:760px;margin-bottom:36px;">'
    'Production-focused work across LLM applications, RAG, semantic search, '
    'structured extraction and AI backend systems.'
    '</div>',
    unsafe_allow_html=True,
)

# ARITRAK
st.markdown(
    '''
    <div class="card" style="padding:28px;margin-bottom:22px;">
        <div class="label">NOV 2025 — PRESENT</div>
        <h2 style="margin-bottom:4px;">AI/ML Software Engineer</h2>
        <div style="color:#8ab4ff;font-weight:700;margin-bottom:12px;">ARITRAK TECHNOLOGIES</div>
        <div class="small">
            Production-oriented LLM modules spanning retrieval, extraction,
            classification, summarization and generation.
        </div>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.markdown("### EIOS")
st.markdown(
    '<div class="small" style="max-width:900px;margin-bottom:18px;">'
    'Built LLM/RAG modules with self-hosted Ollama for sensitive enterprise '
    'workflows, including semantic retrieval, grounded answers and a dual-source '
    'architecture that keeps internal retrieval and live web information separate.'
    '</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
for col, title, body in [
    (c1, "01 · Grounded RAG", "Semantic chunking → embeddings → similarity retrieval → anti-hallucination prompting."),
    (c2, "02 · Dual-source answers", "Parallel internal retrieval + live web search with source separation."),
    (c3, "03 · Private inference", "Self-hosted Ollama for embeddings, extraction, summarization, classification and generation."),
]:
    with col:
        st.markdown(
            f'<div class="card" style="min-height:170px;">'
            f'<div class="label">EIOS</div><h3>{title}</h3>'
            f'<div class="small">{body}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Smart Recruit")
st.markdown(
    '<div class="small" style="max-width:900px;margin-bottom:18px;">'
    'Developed the FastAPI/Celery/PostgreSQL/pgvector/Redis pipeline for resume '
    'parsing and semantic candidate search, including structured extraction, '
    'embedding-based retrieval and a Groq parser with Ollama fallback.'
    '</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
for col, title, body in [
    (c1, "96%", "Name extraction accuracy in the production parser."),
    (c2, "Hybrid ranking", "Embedding similarity + deterministic keyword matching for explainable candidate scores."),
    (c3, "Reliable extraction", "Strict JSON outputs, length-capped summaries and model fallback architecture."),
]:
    with col:
        st.markdown(
            f'<div class="card" style="min-height:170px;">'
            f'<div class="label">SMART RECRUIT</div><h3>{title}</h3>'
            f'<div class="small">{body}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<div class="card">'
    '<div class="label">MODEL ENGINEERING</div>'
    '<h3>LoRA fine-tuning around Mistral-7B</h3>'
    '<div class="small">'
    'Built a LoRA fine-tuning workflow around Mistral-7B using Unsloth/RunPod, '
    'with Node.js → Python → RunPod API orchestration and MongoDB job tracking.'
    '</div></div>',
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# TESCOM
st.markdown(
    '''
    <div class="card" style="padding:28px;margin-bottom:22px;">
        <div class="label">MAY 2025 — SEP 2025</div>
        <h2 style="margin-bottom:4px;">AI/ML Intern</h2>
        <div style="color:#8ab4ff;font-weight:700;margin-bottom:12px;">TESCOM TECHNOLOGIES</div>
        <div class="small">Applied LLM development in an educational AI application.</div>
    </div>
    ''',
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        '<div class="card" style="min-height:150px;">'
        '<div class="label">LLM INTEGRATION</div><h3>Anthropic Claude API</h3>'
        '<div class="small">Integrated Claude API for question answering, explanations and summaries.</div>'
        '</div>',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        '<div class="card" style="min-height:150px;">'
        '<div class="label">EVALUATION</div><h3>Structured prompting</h3>'
        '<div class="small">Structured prompts and evaluated outputs for relevance, accuracy and consistency.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="section"><div class="label">ENGINEERING PRINCIPLE</div>'
    '<h2>Use the model where reasoning helps. Keep deterministic work deterministic.</h2></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="small" style="max-width:900px;">'
    'That principle appears across the work: grounded retrieval instead of unsupported '
    'generation, deterministic candidate scoring where explainability matters, and '
    'Python calculators instead of asking an LLM to perform financial arithmetic.'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<div class="label">TECHNOLOGIES</div><div style="margin-top:8px;">'
    + " ".join(
        f'<span class="pill">{x}</span>'
        for x in [
            "Python", "LLMs", "RAG", "FastAPI", "PostgreSQL", "pgvector",
            "Redis", "Celery", "Docker", "Ollama", "Claude", "Groq",
            "Mistral", "LoRA", "Hugging Face", "Sentence Transformers"
        ]
    )
    + "</div>",
    unsafe_allow_html=True,
)
