import streamlit as st
from components.sidebar import sidebar_navigation

st.set_page_config(page_title="Gestion de Factures", layout="wide")

# Menu global
theme = sidebar_navigation()

# Appliquer le thème choisi
if theme == "Clair":
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] { background-color: #ffffff; color: #000000; }
        [data-testid="stSidebar"] { background-color: #f8f9fa; }
        [data-testid="stMetricValue"] { color: #003366; }
        [data-testid="stDataFrame"] { background-color: #ffffff; color: #000000; }
        button { background-color: #003366; color: #ffffff; border-radius: 6px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] { background-color: #1e1e1e; color: #ffffff; }
        [data-testid="stSidebar"] { background-color: #2c2c2c; }
        [data-testid="stMetricValue"] { color: #00ffcc; }
        [data-testid="stDataFrame"] { background-color: #2c2c2c; color: #ffffff; }
        button { background-color: #00ffcc; color: #000000; border-radius: 6px; }
        </style>
    """, unsafe_allow_html=True)

# Contenu principal
st.image("assets/logo.png", width=150)
st.title("Bienvenue sur MABOU-INSTRUMED Facturation")

st.subheader("⚙️ Actions rapides")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧾 Créer une facture")
    if st.button("➕ Nouvelle Facture"):
        st.switch_page("pages/2_Previsualisation.py")

with col2:
    st.markdown("### 💰 Créer un reçu")
    if st.button("➕ Nouveau Reçu"):
        st.switch_page("pages/2_Previsualisation.py")

with col3:
    st.markdown("### 👥 Gestion des utilisateurs")
    if st.button("🔑 Gérer les utilisateurs"):
        st.switch_page("pages/3_Utilisateurs.py")
