import streamlit as st
from model.joke_generator import NasreddinHocaGenerator

st.set_page_config(page_title="Nasreddin Hoca Fıkra Üretici", page_icon="🧠")
st.title("🧠 Nasreddin Hoca Fıkra Üretici")
st.caption("Fine-tune edilmiş LLM ile gerçek Nasreddin Hoca fıkraları üretin!")

if "generator" not in st.session_state:
    st.session_state.generator = NasreddinHocaGenerator()

if st.button("🎲 Fıkra Üret"):
    with st.spinner("Fıkra hazırlanıyor..."):
        joke = st.session_state.generator.generate_joke()
        st.success(joke)
