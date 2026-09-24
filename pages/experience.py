import streamlit as st

st.markdown('<div class="label">Professional Experience</div><h1>Building AI systems in production.</h1>', unsafe_allow_html=True)
st.write("")

st.markdown("""
<div class="card">
<div class="label">ARITRAK TECHNOLOGIES · AI/ML SOFTWARE ENGINEER · NOV 2025 — PRESENT</div>
<h2>EIOS + Smart Recruit</h2>
<div class="small">Production-oriented LLM modules spanning retrieval, extraction, classification, summarization and generation.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### EIOS")
st.write("Built LLM/RAG modules with self-hosted Ollama for sensitive enterprise workflows, including semantic retrieval, grounded answers and a dual-source architecture that keeps internal retrieval and live web information separate.")

c1,c2,c3 = st.columns(3)
for col,title,body in [
    (c1,"Grounded RAG","Semantic chunking → embeddings → similarity retrieval → anti-hallucination prompting."),
    (c2,"Dual-source answers","Parallel internal retrieval + live web search with source separation."),
    (c3,"Private inference","Self-hosted Ollama for embeddings, extraction, summarization, classification and generation."),
]:
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><div class="small">{body}</div></div>', unsafe_allow_html=True)

st.markdown("### Smart Recruit")
st.write("Developed the FastAPI/Celery/PostgreSQL/pgvector/Redis pipeline for resume parsing and semantic candidate search, including structured extraction, embedding-based retrieval and a Groq parser with Ollama fallback.")

c1,c2,c3 = st.columns(3)
for col,title,body in [
    (c1,"96%","Name extraction accuracy in the production parser."),
    (c2,"Hybrid ranking","Embedding similarity + deterministic keyword matching for explainable candidate scores."),
    (c3,"Reliable extraction","Strict JSON outputs, length-capped summaries and model fallback architecture."),
]:
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><div class="small">{body}</div></div>', unsafe_allow_html=True)

st.markdown("### Fine-tuning pipeline")
st.write("Built a LoRA fine-tuning workflow around Mistral-7B using Unsloth/RunPod, with Node.js → Python → RunPod API orchestration and MongoDB job tracking.")

st.divider()

st.markdown("""
<div class="card">
<div class="label">TESCOM TECHNOLOGIES · AI/ML INTERN · MAY 2025 — SEP 2025</div>
<h2>Applied LLM development</h2>
<div class="small">Integrated Anthropic Claude API into an educational AI application for question answering, explanations and summaries; structured prompts and evaluated outputs for relevance, accuracy and consistency.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section"><div class="label">Engineering principle</div><h2>Use the model where reasoning helps. Keep deterministic work deterministic.</h2></div>', unsafe_allow_html=True)
st.write("That principle appears across the work: grounded retrieval instead of unsupported generation, deterministic candidate scoring where explainability matters, and Python calculators instead of asking an LLM to perform financial arithmetic.")
