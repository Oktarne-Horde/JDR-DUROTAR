import streamlit as st
from orc_generator import generer_orc

st.title("🧌 Générateur d'Orc")

# Stockage du résultat
if "orc" not in st.session_state:
    st.session_state.orc = ""

# Bouton
if st.button("🎲 Générer un Orc"):
    st.session_state.orc = generer_orc()

# Affichage
if st.session_state.orc:
    st.code(st.session_state.orc)
    st.download_button(
        "💾 Télécharger la fiche",
        st.session_state.orc,
        file_name="orc.txt"
    )
