# Local-Bot Lite

Application légère pour chatter avec plusieurs modèles open-source, 100% local.

---

## Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/tonpseudo/Local-Bot.git
cd Local-Bot
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

---

## Lancer l’application

```bash
python ai8bot_lite.py
```

- L’appli détecte automatiquement les modèles légers recommandés.  
- Si un modèle manque, il sera téléchargé dans le cache Hugging Face (`~/.cache/huggingface/hub`).  
- Permet de chatter avec le bot conversationnel ou d’utiliser les autres modèles légers pour traduction, code, résumé, etc.

---

## Notes

- **Python 3.9+ recommandé**  
- **8 GB RAM minimum**, environ **20 GB de disque libre** pour les modèles.  
- Les modèles plus volumineux peuvent être ajoutés après installation.  
- Pour créer un EXE Windows depuis l’interface, utilise le bouton “Construire EXE” (PyInstaller doit être installé).

---

## Dépendances principales

- `transformers`  
- `huggingface-hub`  
- `sentence-transformers`  
- `torch`  
- `customtkinter` (optionnel, sinon fallback Tkinter)  
- `faiss-cpu` (optionnel, pour embeddings rapides)
