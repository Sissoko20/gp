# components/sidebar.py
import streamlit as st

def sidebar_navigation():
    st.sidebar.image("assets/logo.png", width=100)
    st.sidebar.title("📌 Navigation")

    if st.sidebar.button("🏠 Accueil", key="home"):
        st.switch_page("app.py")
    if st.sidebar.button("🧾 Facture", key="facture"):
        st.switch_page("pages/2_Previsualisation.py")
    if st.sidebar.button("💰 Reçu", key="recu"):
        st.switch_page("pages/2_Previsualisation.py")
    if st.sidebar.button("📊 Dashboard", key="dashboard"):
        st.switch_page("pages/Dashboard.py")
    if st.sidebar.button("👥 Utilisateurs", key="users"):
        st.switch_page("pages/3_Utilisateurs.py")
