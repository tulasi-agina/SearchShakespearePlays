# Inspiration: https://blog.jcharistech.com/2020/07/09/simple-nlp-app-with-spacy-streamlit/

import streamlit as st
import spacy_streamlit
import spacy

models = ["en_core_web_sm", "en_core_web_md"]

"""A Simple NLP app with Spacy-Streamlit"""

st.title("Named Entity Recognition")

import spacy
from spacy_streamlit import visualize_parser

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a text")
visualize_parser(doc)
