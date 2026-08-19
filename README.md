# 🤖 Smart ChatOps Assistant

Un agent d'intelligence artificielle intégré à **Discord**, capable de diagnostiquer et d'agir sur une infrastructure — **Kubernetes** et **AWS** — directement en langage naturel.

Projet réalisé dans le cadre d'un stage d'été chez **Talan**.

---

## 📌 Le problème

Aujourd'hui, diagnostiquer une panne ou gérer une ressource cloud demande de jongler entre plusieurs outils : commandes `kubectl`, console AWS, logs à croiser manuellement... sous pression, avec un vrai risque d'erreur humaine.

**Smart ChatOps Assistant** simplifie tout ça : un seul point d'entrée (Discord), une question en langage naturel, et l'agent s'occupe du reste — diagnostic **et** action.

---

## ⚙️ Fonctionnalités

- 💬 Interrogation de l'infrastructure en langage naturel depuis Discord
- 🔎 Diagnostic automatique des pannes (analyse de logs, état des pods, etc.)
- ☁️ Consultation **et action** sur les ressources AWS (ex : buckets S3)
- 🧠 Agent basé sur une véritable boucle de raisonnement (LangGraph), pas un simple chatbot
- 🔐 Séparation stricte décision / exécution : l'IA ne touche jamais l'infrastructure directement
- 🗂️ Historique des conversations conservé (SQLite)

---

## 🏗️ Architecture

```
Discord ──(WebSocket)──▶ Backend FastAPI ──▶ LangGraph + LLM (Ollama)
                              │                        │
                              │◀── décide de l'action ──┘
                              ▼
                    Kubernetes (kubectl / client Python)
                    AWS (boto3 / LocalStack en local)
```

1. L'utilisateur pose sa question sur Discord
2. Le backend FastAPI transmet la demande à l'agent (LangGraph + LLM via Ollama)
3. L'agent décide de l'action nécessaire (ex : `get_logs`)
4. Le backend exécute concrètement l'action sur l'infrastructure (Kubernetes / AWS)
5. Les résultats bruts remontent à l'agent, qui les analyse
6. L'agent renvoie une réponse claire (explication + solution) affichée sur Discord

> L'IA ne fait jamais qu'observer et décider. C'est toujours le backend qui exécute, trace et sécurise chaque action.

---

## 🧰 Stack technique

| Composant         | Technologie                  |
|-------------------|-------------------------------|
| Interface         | Discord                      |
| Communication     | WebSocket                    |
| Backend           | FastAPI (Python)             |
| Historique        | SQLite                       |
| Agent             | LangGraph                    |
| Raisonnement      | LLM via Ollama (Phi-3)       |
| Kubernetes        | Kubernetes Python Client     |
| AWS               | boto3                        |
| Simulation AWS    | LocalStack                   |
| Cluster local      | Minikube                     |
| Conteneurisation  | Docker                       |

---

## 📁 Structure du projet

```
.
├── agent.py            # Logique de l'agent (LangGraph + LLM)
├── bot.py               # Bot Discord
├── main.py               # Point d'entrée de l'application
├── deployment.yaml        # Déploiement Kubernetes
├── docker-compose.yml      # Orchestration des services en local
├── localstack/             # Config de simulation AWS
├── k8s/                    # Manifests Kubernetes (dont service.yaml)
└── README.md
```

---

## 🚀 Lancer le projet en local

### Prérequis
- Docker & Docker Compose
- Minikube (pour simuler un cluster Kubernetes local)
- Un bot Discord configuré (token à fournir)

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/<ton-org>/ChatOps.git
cd ChatOps

# 2. Démarrer Minikube
minikube start

# 3. Lancer les services avec Docker Compose
docker-compose up --build

# 4. Déployer sur Kubernetes (optionnel)
kubectl apply -f k8s/
kubectl apply -f deployment.yaml
```

---

## 💡 Exemple d'utilisation

```
Utilisateur : !chat est-ce que mes pods tournent correctement ?

Smart ChatOps Assistant :
D'après les données du cluster Kubernetes, tous vos pods sont en état "Running".
Cela indique qu'ils sont opérationnels. Nous pourrions examiner le trafic réseau
ou les performances des services pour aller plus loin.
```

---

## 🗺️ Roadmap

- [ ] Intégration Prometheus pour enrichir le diagnostic avec des métriques temps réel
- [ ] Connexion à Jira pour automatiser la création de tickets d'incident

---

## 👤 Auteur

Projet réalisé par **[Ton nom]** dans le cadre d'un stage d'été chez Talan.
