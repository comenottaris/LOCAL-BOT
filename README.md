# Local-Bot Lite

Application légère pour chatter avec plusieurs modèles open-source, 100% local.  
Permet de choisir automatiquement le meilleur modèle pour chaque tâche ou de sélectionner manuellement via l’interface.  
Inclut un bouton pour construire un EXE directement depuis l’application.

---

## Installation

1. Cloner le dépôt

git clone https://github.com/tonpseudo/Local-Bot.git
cd Local-Bot

2. Créer un environnement virtuel (optionnel mais recommandé)

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate

3. Installer les dépendances

pip install -r requirements.txt

---

## Lancer l’application

python local.bot.py

- L’application détecte automatiquement les modèles légers recommandés.  
- Si un modèle manque, il sera téléchargé dans le cache Hugging Face (~/.cache/huggingface/hub).  
- Possibilité de choisir le modèle pour chaque tâche via l’interface ou de laisser la sélection automatique.  
- Permet de chatter avec le bot conversationnel ou d’utiliser les autres modèles pour traduction, résumé, code, embeddings, etc.  
- Les réponses affichent quel modèle a été utilisé pour générer la réponse.

---

## Build EXE

- Un bouton “Construire EXE” est disponible dans l’interface.  
- L’EXE inclut tous les fichiers nécessaires et utilise PyInstaller.  
- Pour un build manuel via le terminal :

python local.bot.py --build-exe

- Assurez-vous que PyInstaller est installé :

pip install pyinstaller

---

## Notes

- Python 3.9+ recommandé  
- 8 GB RAM minimum, environ 20 GB de disque libre pour les modèles.  
- Les modèles plus volumineux peuvent être ajoutés après installation.  
- L’interface propose maintenant un chat en bulles, vos messages alignés à droite et les réponses du bot à gauche avec nom en gras et majuscule.

---

## Dépendances principales

- transformers  
- huggingface-hub  
- sentence-transformers  
- torch  
- customtkinter (optionnel, sinon fallback Tkinter)  
- faiss-cpu (optionnel, pour embeddings rapides)
