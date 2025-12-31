import streamlit as st
from firebase_utils import create_user, get_user_role

st.set_page_config(page_title="User Manager", layout="wide")

# Initialiser session_state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["role"] = None

# Si déjà connecté → redirection
if st.session_state["authenticated"]:
    st.success(f"✅ Vous êtes connecté en tant que {st.session_state['role']}")
    st.experimental_set_query_params(page="app")
    st.stop()

st.title("👥 Gestion des utilisateurs")

# -------------------------------
# Création de compte
# -------------------------------
st.subheader("🧾 Créer un compte")

with st.form("create_account"):
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    role = st.selectbox("Rôle", ["user", "admin"])
    submit = st.form_submit_button("Créer le compte")

    if submit:
        try:
            uid = create_user(email, password, role)
            st.success(f"✅ Compte créé avec UID: {uid} et rôle: {role}")
        except Exception as e:
            if "EMAIL_EXISTS" in str(e):
                st.warning("⚠️ Cet email existe déjà. Essayez de vous connecter ci-dessous.")
            else:
                st.error(f"❌ Erreur lors de la création: {e}")

# -------------------------------
# Connexion
# -------------------------------
st.subheader("🔑 Se connecter")

with st.form("login"):
    login_email = st.text_input("Email (connexion)")
    login_password = st.text_input("Mot de passe (connexion)", type="password")
    login_submit = st.form_submit_button("Se connecter")

    if login_submit:
        role = get_user_role(login_email)
        if role:
            st.success(f"✅ Connecté en tant que {role}")
            st.session_state["authenticated"] = True
            st.session_state["role"] = role
            st.experimental_set_query_params(page="app")
            st.rerun()
        else:
            st.error("❌ Utilisateur introuvable")
