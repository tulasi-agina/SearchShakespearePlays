# Inspiration: https://blog.jcharistech.com/2020/07/09/simple-nlp-app-with-spacy-streamlit/

import spacy
import spacy_streamlit
spacy.download('en_core_web_sm')
spacy.download('en_core_web_md')

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
spacy_streamlit.visualize(models, default_text)
