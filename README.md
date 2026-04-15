<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-Community-32CD32?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-008080?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CLIP-Multimodal-FF6B6B?style=for-the-badge" />
</p>
 
<h1 align="center">🧠 Advanced Hybrid RAG Orchestrator</h1>
 
<p align="center">
  <b>Un agent IA avancé avec architecture RAG Hybride Multi-Modale</b><br>
  <i>Capable de résoudre des tâches documentaires complexes grâce à un raisonnement multi-étapes, une planification adaptative et des mécanismes anti-hallucinations rigoureux.</i>
</p>
 
<p align="center">
  <a href="#-démarrage-rapide">🚀 Démarrage Rapide</a> •
  <a href="#-architecture">🏗️ Architecture</a> •
  <a href="#-fonctionnalités">✨ Fonctionnalités</a> •
  <a href="#-documentation">📚 Documentation</a> •
  <a href="#-docker-deployment">🐳 Docker</a>
</p>
 
---
 
## 📋 Table des Matières
 
- [Vue d'ensemble](#-vue-densemble)
- [Architecture Hybride](#-architecture-hybride)
- [Fonctionnalités Clés](#-fonctionnalités-clés)
- [Stack Technique](#-stack-technique)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Docker Deployment](#-docker-deployment)
- [Cas d'Usage](#-cas-dusage)
- [Structure du Projet](#-structure-du-projet)
- [Roadmap](#-roadmap)
- [Citation](#-citation)
- [Contact](#-contact)
 
---
 
## 🎯 Vue d'ensemble
 
**Advanced Hybrid RAG Orchestrator** est un système de Retrieval-Augmented Generation (RAG) de nouvelle génération qui combine le traitement multi-modal (texte + images) avec une orchestration intelligente. Contrairement aux systèmes RAG traditionnels, cet agent peut :
 
- 🖼️ **Comprendre les images** grâce à CLIP (schémas, graphiques, captures d'écran)
- 📄 **Traiter des documents complexes** (PDF avec mise en page riche)
- 🧠 **Raisonner en plusieurs étapes** avec planification adaptative
- 🛡️ **Garantir la fiabilité** via des mécanismes anti-hallucination
 
## 🎬 Demo

![Demo GIF](assets/demo.gif)

**Scénario**: Analyse d'un PDF technique avec figures  
**Question**: *"Compare les performances des modèles A et B selon le graphique page 15"*

 
---
 
## 🏗️ Architecture Hybride
 
### 🔄 Pipeline Complet
 
## 🏗️ Architecture

```mermaid
flowchart TB
    subgraph Input["📥 Input Layer"]
        PDF[PDF Documents]
        IMG[Images]
    end
    
    subgraph Process["🔧 Processing"]
        PYM[PyMuPDF Extractor]
        SPLIT[Text Splitter]
        CLIP[CLIP Encoder]
    end
    
    subgraph Store["🗄️ Vector Store"]
        FAISS[(FAISS Index)]
    end
    
    subgraph Agent["🤖 RAG Agent"]
        RET[Retriever]
        RERANK[Reranker]
        GEN[Generator]
    end
    
    PDF --> PYM
    PYM --> SPLIT
    PYM --> IMG
    IMG --> CLIP
    SPLIT --> FAISS
    CLIP --> FAISS
    FAISS --> RET
    RET --> RERANK
    RERANK --> GEN
 
### 🧩 Composants Clés
 
| Composant | Fichier | Description |
|-----------|---------|-------------|
| **Core Pipeline** | `functions_for_pipeline.py` | Fonctions d'extraction, chunking, embedding |
| **Helper Utils** | `helper_functionality.py` | Utilitaires et wrappers |
| **Orchestrated Agent** | `orchestrated_rag_agent_heavy_profile.ipynb` | Notebook principal avec l'agent complet |
| **Graph Visualizer** | `full_graph_visualization.ipynb` | Visualisation du flux de données |
| **Simulation** | `simulatz_agent.ipynb` | Tests et simulation de scénarios |
| **Fixup Tools** | `fixup.py`, `fixup.ipynb` | Debugging et corrections |
 
---
 
## ✨ Fonctionnalités Clés
 
### 🎯 Multi-Modal Intelligence
- ✅ **Text + Image Understanding** : CLIP pour encoder visuel et textuel dans le même espace
- ✅ **Cross-Modal Retrieval** : Chercher du texte avec une image ou vice-versa
- ✅ **Figure/Chart Analysis** : Comprendre les schémas techniques
 
### 🧠 Orchestration Avancée
- ✅ **Query Planning** : Décompose les questions complexes en sous-tâches
- ✅ **Adaptive Retrieval** : Ajuste dynamiquement la stratégie de recherche
- ✅ **Multi-Step Reasoning** : Chaîne de pensée pour réponses complexes
 
### 🛡️ Anti-Hallucination
- ✅ **Source Grounding** : Toute information doit provenir du document
- ✅ **Citation Enforcement** : [Source: Doc.pdf, Page 12, Chunk 3]
- ✅ **Confidence Scoring** : Score de fiabilité par réponse
- ✅ **Transparency Mode** : Affiche les chunks utilisés
 
### ⚡ Performance & Scalability
- ✅ **Fast Indexing** : ~100 pages/minute
- ✅ **Sub-second Search** : <500ms retrieval avec FAISS CPU
- ✅ **Docker Ready** : Déploiement containerisé
- ✅ **Batch Processing** : Traitement par lots de documents
 
---
 
## 🛠️ Stack Technique
 
<p align="center">
  <img src="https://img.shields.io/badge/PyMuPDF-1.27+-green?style=flat-square&logo=adobe&logoColor=white" />
  <img src="https://img.shields.io/badge/CLIP-OpenAI-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/FAISS-1.13+-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/LangChain-0.4+-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Transformers-4.36+-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/PyTorch-2.0+-red?style=flat-square&logo=pytorch" />
</p>
 
| Couche | Technologie | Rôle |
|--------|-------------|------|
| **Document Parsing** | PyMuPDF (fitz) | Extraction texte, images, métadonnées |
| **Text Processing** | LangChain Text Splitters | Chunking intelligent |
| **Image Processing** | CLIP (ViT-B/32) | Embeddings visuels |
| **Text Embeddings** | SentenceTransformers | Encodage sémantique |
| **Vector Store** | FAISS (CPU) | Indexation et recherche rapide |
| **Orchestration** | LangChain + Custom Logic | Flux RAG avancé |
| **Containerization** | Docker + Compose | Déploiement portable |
 
---
 
## 🚀 Installation
 
### Option 1 : Local (Conda/Recommended)
 
```bash
# Cloner le repo
git clone https://github.com/WahabHammoud/Advanced-Hybrid-RAG-Orchestrator.git
cd Advanced-Hybrid-RAG-Orchestrator
 
# Créer l'environnement
conda create -n rag-orchestrator python=3.9
conda activate rag-orchestrator
 
# Installer les dépendances
pip install -r requirements.txt
Option 2 : Docker (Production)
bash
# Build et run avec Docker Compose
docker-compose up -d
 
# Ou build manuel
docker build -t rag-orchestrator .
docker run -p 8888:8888 -v ./data:/app/data rag-orchestrator
📋 Requirements
txt
pymupdf>=1.27.0
langchain>=0.4.0
langchain-community>=0.4.0
langchain-text-splitters>=1.1.0
faiss-cpu>=1.13.0
transformers>=4.36.0
torch>=2.0.0
pillow>=10.0.0
scikit-learn>=1.3.0
numpy>=1.24.0
pandas>=2.0.0
💻 Utilisation
📝 Notebook Principal
bash
jupyter notebook orchestrated_rag_agent_heavy_profile.ipynb
🔧 Pipeline Rapide
python
from functions_for_pipeline import HybridRAGPipeline
 
# Initialiser le pipeline
pipeline = HybridRAGPipeline(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    clip_model="openai/clip-vit-base-patch32",
    chunk_size=1000,
    chunk_overlap=200
)
 
# Indexer un document
pipeline.index_document("document.pdf")
 
# Query
response = pipeline.query(
    question="Explique le schéma de la figure 3 et son impact sur le système",
    return_sources=True,
    confidence_threshold=0.7
)
 
print(response.answer)
print(response.sources)  # Citations avec pages
🐳 Docker Deployment
bash
# Démarrer tous les services
docker-compose up -d
 
# Accéder au Jupyter
open http://localhost:8888
 
# Vérifier les logs
docker-compose logs -f
📁 Structure du Projet
Advanced-Hybrid-RAG-Orchestrator/
│
├── 📓 Notebooks/
│   ├── orchestrated_rag_agent_heavy_profile.ipynb  ⭐ Main Agent
│   ├── full_graph_visualization.ipynb              📊 Data Flow Viz
│   ├── simulatz_agent.ipynb                        🧪 Testing & Sim
│   └── fixup.ipynb                                 🔧 Debug Tool
│
├── 🐍 Python Modules/
│   ├── functions_for_pipeline.py                   🔧 Core Functions
│   ├── helper_functionality.py                   🛠️ Utilities
│   └── fixup.py                                   🔨 Quick Fixes
│
├── 🐳 Deployment/
│   ├── docker-compose.yml                          🌐 Multi-service
│   └── dockerfile                                  📦 Container
│
├── 📄 Documentation/
│   ├── README.md                                   📖 This File
│   ├── ARCHITECTURE.md                             🏗️ Deep Dive
│   └── CONTRIBUTING.md                             🤝 Guidelines
│
└── 🔧 Config/
    ├── requirements.txt                            📦 Dependencies
    └── .gitignore                                  🚫 Ignore Rules
🎯 Cas d'Usage
1️⃣ Documentation Technique
Scenario: Manuel de 500 pages avec schémas techniques
Query: "Comment configurer le protocole de communication selon la figure 4.2?"
Result: Réponse avec citation exacte + image de la figure

2️⃣ Analyse Scientifique
Scenario: Papiers de recherche avec graphiques et tableaux
Query: "Compare les résultats des expériences A et B visuellement"
Result: Analyse comparative basée sur les figures extraites

3️⃣ Juridique & Conformité
Scenario: Contrats avec signatures, logos, tampons
Query: "Quelles clauses modifient les conditions de paiement?"
Result: Extraction précise avec références aux articles

4️⃣ Enterprise Knowledge Base
Scenario: Base de connaissances multi-modale (PDF, images, scans)
Query: "Trouve-moi tous les documents mentionnant le produit X avec son logo"
Result: Recherche hybride texte + image

🗺️ Roadmap
Core Multi-Modal RAG Pipeline
CLIP Integration for Images
FAISS Vector Store
Docker Support
Anti-Hallucination Mechanisms
🔄 Web Interface (Gradio/Streamlit)
🔄 API REST (FastAPI)
🔄 Async Processing (Celery)
🔄 Cloud Deployment (AWS/GCP/Azure)
🔄 Fine-tuning Support
🔄 Multi-language Support (FR, EN, AR)
📖 Citation
Si vous utilisez ce projet dans votre recherche ou travail :

bibtex
@software{wahab_hybrid_rag_2026,
  author = {Hammoud, Wahab},
  title = {Advanced Hybrid RAG Orchestrator},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/WahabHammoud/Advanced-Hybrid-RAG-Orchestrator}},
  keywords = {RAG, Multimodal, CLIP, FAISS, LangChain, Document AI}
}
📧 Contact & Support
🐛 Issues & Contributions
🐛 Bug Report: Open an Issue
💡 Feature Request: Discussions
🤝 Contribute: Voir CONTRIBUTING.md
