# Inspiration: https://blog.jcharistech.com/2020/07/09/simple-nlp-app-with-spacy-streamlit/

import streamlit as st
import spacy_streamlit
import spacy

models = ["en_core_web_sm", "en_core_web_md"]

"""A Simple NLP app with Spacy-Streamlit"""

st.title("Named Entity Recognition")

menu = ["Home","NER"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
	st.subheader("Tokenization")
	raw_text = st.text_area("Your Text","Enter Text Here")
	if st.button("Tokenize"):
		spacy_streamlit.visualize(models, raw_text)

	elif choice == "NER":
		st.subheader("Named Entity Recognition")
		raw_text = st.text_area("Your Text","Enter Text Here")
		docx = nlp(raw_text)
		spacy_streamlit.visualize_ner(raw_text,labels=nlp.get_pipe('ner').labels)
