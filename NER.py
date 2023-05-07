# Inspiration: https://blog.jcharistech.com/2020/07/09/simple-nlp-app-with-spacy-streamlit/

import streamlit as st
import spacy_streamlit
import spacy

nlp = spacy.load('en')

def main():
	"""A Simple NLP app with Spacy-Streamlit"""

	st.title("Named Entity Recognition")

	menu = ["Home","NER"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Tokenization")
		raw_text = st.text_area("Your Text","Enter Text Here")
		docx = nlp(raw_text)
		if st.button("Tokenize"):
			spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])

	elif choice == "NER":
		st.subheader("Named Entity Recognition")
		raw_text = st.text_area("Your Text","Enter Text Here")
		docx = nlp(raw_text)
		spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)


if __name__ == '__main__':
	main()
