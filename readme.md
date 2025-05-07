# 🚀 Déploiement Kubernetes : Frontend Vue.js + Backend Spring Boot

Ce dépôt contient la configuration Kubernetes nécessaire pour déployer une application composée de deux conteneurs Docker :

- **Frontend** : une application Vue.js stylisée avec **Tailwind CSS**, affichant un CV interactif et capable de **streamer une vidéo** depuis le backend.
- **Backend** : une API développée en **Spring Boot**, responsable du streaming vidéo.

## 📦 Structure du projet

├── k8s/
│ ├── frontend-deployment.yaml
│ ├── backend-deployment.yaml
│ ├── frontend-service.yaml
│ ├── backend-service.yaml
│ └── ...
├── frontend/ # Code Vue.js + Tailwind CSS
└── backend/ # Code Spring Boot

## 🛠 Technologies utilisées

- 🖼 **Vue.js** pour le frontend
- 🎨 **Tailwind CSS** pour le style
- ⚙️ **Spring Boot** pour le backend
- 🐳 **Docker** pour le conteneurisation
- ☸️ **Kubernetes** pour l’orchestration des services

## 🚚 Lancement (avec `kubectl`)

1. **Construire les images Docker** (dans `frontend/` et `backend/`) et les pousser vers un registre (DockerHub, GitHub Container Registry, etc.)

2. **Déployer sur Kubernetes** :

