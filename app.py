import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Gestion de Factures", layout="wide")
st.image("assets/logo.png", width=150)
st.title("Bienvenue sur MABOU-INSTRUMED Facturation")
st.markdown("Sélectionnez une page dans le menu latéral.")

# Connexion DB
conn = sqlite3.connect("data/factures.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS factures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    client TEXT,
    montant REAL,
    date TEXT
)
""")
conn.commit()

# Récupérer l’historique
df = pd.read_sql("SELECT * FROM factures ORDER BY date DESC", conn)

# -------------------------------
# Aperçu analytique
# -------------------------------
st.subheader("📊 Aperçu global")

if not df.empty:
    total_factures = df[df["type"] == "Facture Professionnelle"]["montant"].sum()
    total_recus = df[df["type"] == "Reçu de Paiement"]["montant"].sum()
    total_global = df["montant"].sum()
    nb_docs = len(df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Factures", f"{total_factures:,.0f} FCFA")
    col2.metric("Total Reçus", f"{total_recus:,.0f} FCFA")
    col3.metric("Montant Global", f"{total_global:,.0f} FCFA")
    col4.metric("Documents générés", nb_docs)
else:
    st.info("Aucune donnée disponible pour le moment.")

# -------------------------------
# Historique
# -------------------------------
st.subheader("📑 Historique des factures et reçus")
if not df.empty:
    type_filtre = st.selectbox("Filtrer par type :", ["Tous"] + df["type"].unique().tolist())
    if type_filtre != "Tous":
        df = df[df["type"] == type_filtre]
    st.dataframe(df, use_container_width=True)

    choix_id = st.selectbox("Sélectionnez une facture/reçu :", df["id"].tolist())
    if choix_id:
        facture = df[df["id"] == choix_id].iloc[0]
        st.write(f"""
        **Type :** {facture['type']}  
        **Client :** {facture['client']}  
        **Montant :** {facture['montant']} FCFA  
        **Date :** {facture['date']}
        """)
else:
    st.warning("Aucun historique disponible.")

# -------------------------------
# Cards d’actions
# -------------------------------
st.subheader("⚙️ Actions rapides")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧾 Créer une facture")
    if st.button("➕ Nouvelle Facture"):
        st.switch_page("pages/2_Previsualisation.py")  # redirection vers ta page facture

with col2:
    st.markdown("### 💰 Créer un reçu")
    if st.button("➕ Nouveau Reçu"):
        st.switch_page("pages/2_Previsualisation.py")  # même page mais avec modèle reçu

with col3:
    st.markdown("### 👥 Gestion des utilisateurs")
    if st.button("🔑 Gérer les utilisateurs"):
        st.switch_page("pages/3_Utilisateurs.py")  # page à créer pour gestion utilisateurs
