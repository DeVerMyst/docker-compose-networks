import streamlit as st
import requests

st.title("Test POST")

id_value = st.text_input("ID")

if st.button("Envoyer"):
    try:
        response = requests.post("http://localhost:8000/id", data={"id": id_value})
        st.write(f"Réponse: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur: {e}")

# import streamlit as st
# import requests

# def send_post_request(url, id_value):
#     try:
#         response = requests.post(url, data={"id": id_value})
#         st.write(f"Réponse de {url}: {response.text}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"Erreur lors de la requête vers {url}: {e}")

# st.title("Requêtes POST vers localhost")

# id_value = st.text_input("Entrez un chiffre ou des lettres")

# if st.button("Envoyer la requête POST"):
#     if id_value:
#         send_post_request("http://localhost:8000/id", id_value)
#         send_post_request("http://localhost:8001/id", id_value)
#         send_post_request("http://child:8001/id", id_value)
#     else:
#         st.warning("Veuillez entrer une valeur.")