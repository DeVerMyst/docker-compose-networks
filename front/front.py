import requests
import streamlit as st

st.title("Test Communication Inter-Services")

id_value = st.text_input("Entrez un ID à envoyer")

if st.button("Envoyer via Mother API"):
    try:
        # Le front est "dehors", il utilise localhost
        response = requests.post("http://localhost:8000/id", data={"id": id_value})
        st.success(f"Réponse de Mother : {response.json()}")
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")