import streamlit as st
from orc_generator import generer_orc

st.title("Générateur d'Orc")

if st.button("Générer un Orc"):
    resultat = generer_orc()
    st.text(resultat)
