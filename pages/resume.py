import streamlit as st
st.markdown('<div class="label">Resume</div><h1>AI/ML Software Engineer</h1>', unsafe_allow_html=True)
st.write("")

st.markdown("""
<div class="card">
<h2>Anushree D K</h2>
<div class="small">AI/ML Software Engineer · LLMs · RAG · NLP · Python · FastAPI</div>
<br>
<span class="pill">Bengaluru, India</span>
<span class="pill">Open to relocation</span>
</div>
""", unsafe_allow_html=True)

st.markdown("### Core strengths")
st.markdown(" ".join(f'<span class="pill">{x}</span>' for x in [
    "LLM Applications","RAG","Semantic Search","Structured Extraction","Tool Calling",
    "Python","FastAPI","PostgreSQL + pgvector","Ollama","Claude","Groq","Mistral","LoRA","Docker"
]), unsafe_allow_html=True)

st.markdown("### Education")
st.write("M.Tech — Industrial Automation & Robotics, Manipal Institute of Technology")
st.write("B.E. — Electronics & Communication Engineering")

st.markdown("### Certifications")
st.write("IBM AI Engineering Professional Certificate · Certified Data Analyst (Excelr) · Google AI/ML coursework")

st.markdown("### Contact")
st.write("Email: anugowda612@gmail.com")
st.write("LinkedIn: linkedin.com/in/anushree-dk-644516220")
st.write("GitHub: github.com/Anushree-DK")
