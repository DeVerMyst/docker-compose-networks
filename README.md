# Communication Inter-Services (Mother-Child-Front)

Ce code démontre une architecture micro-services utilisant Docker Compose, FastAPI et Streamlit. L'objectif est d'illustrer la communication entre services dans un réseau isolé (bridge) et l'exposition sélective de ports.

## Structure du Projet

```plaintext
docker-compose-networks\
├── docker-compose.yml        # Orchestration globale des services
├── child_api/                # Micro-service récepteur (interne uniquement)
│   ├── child_api.py
│   ├── pyproject.toml
│   ├── Dockerfile
│   └── uv.lock
├── mother_api/               # Micro-service passerelle (exposé)
│   ├── mother_api.py
│   ├── pyproject.toml
│   ├── Dockerfile
│   └── uv.lock
└── front/                    # Interface utilisateur Streamlit
    ├── app_front.py
    ├── pyproject.toml
    └── uv.lock

```

## Architecture Réseau

1. **Front (Streamlit)** : S'exécute sur l'hôte et communique avec la Mother API via `http://localhost:8000`.
2. **Mother API (FastAPI)** : Sert de passerelle. Elle reçoit les requêtes du Front et les transmet à la Child API via le réseau interne Docker.
3. **Child API (FastAPI)** : Service privé. Il n'est pas accessible depuis l'hôte (navigateur) mais répond aux requêtes de la Mother API sur `http://child:8001`.

## Installation et Lancement

### Construction et démarrage

Utilisez Docker Compose pour builder les images (en ignorant le cache pour garantir l'installation de `python-multipart`) et lancer les conteneurs :

```bash
docker-compose build --no-cache
docker-compose up

```

## Utilisation

1. **Interface Streamlit** : Ouvrez votre navigateur sur `http://localhost:8501`.
2. **Envoi de données** : Saisissez un ID dans le champ texte et validez.
3. **Flux de données** :
* Le Front envoie un POST vers `localhost:8000/id`.
* La Mother API reçoit le formulaire et effectue un POST interne vers `child:8001/receive_id`.
* La Child API enregistre l'ID (visible dans les logs du terminal).
