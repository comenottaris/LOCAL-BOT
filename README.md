# Local-Bot Lite

Application légère pour chatter avec plusieurs modèles open-source, 100% local.

---

## Installation

1. **Cloner le dépôt**

git clone https://github.com/tonpseudo/Local-Bot.git
cd Local-Bot

2. **Créer un environnement virtuel (optionnel mais recommandé)**

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate

3. **Installer les dépendances**

pip install -r requirements.txt

---

## Lancer l’application

python local.bot.py

- L’application détecte automatiquement les modèles légers recommandés.  
- Si un modèle manque, il sera téléchargé dans le cache Hugging Face (`~/.cache/huggingface/hub`).  
- Permet de chatter avec le bot conversationnel ou d’utiliser les autres modèles pour traduction, code, résumé, etc.  
- Vous pouvez sélectionner quel modèle utiliser via le menu dans l’interface.  
- Une option “Auto” permet de choisir automatiquement le meilleur modèle selon la requête.

---

## Construire un EXE Windows

python build_exe.py

- L’interface propose un bouton “Construire EXE”.  
- PyInstaller doit être installé (`pip install pyinstaller`).  
- Vous pouvez choisir quels modèles inclure dans l’EXE pour réduire la taille.

---

## Notes

- **Python 3.9+ recommandé**  
- **8 GB RAM minimum**, environ **20 GB de disque libre** pour les modèles.  
- Les modèles plus volumineux peuvent être ajoutés après installation.  
- L’interface utilise CustomTkinter si disponible, sinon Tkinter standard.  
- Les réponses du bot indiquent le modèle utilisé au début pour plus de clarté.

---

## Dépendances principales

- transformers  
- huggingface-hub  
- sentence-transformers  
- torch  
- customtkinter (optionnel)  
- faiss-cpu (optionnel, pour embeddings rapides)
# Local-Bot Lite

Local-Bot Lite est une application légère qui vous permet de chatter avec plusieurs modèles open-source, entièrement en local.  
Elle est conçue pour fonctionner sans connexion Internet après téléchargement des modèles, garantissant confidentialité et rapidité.

---

## Installation

Voici les étapes pour installer Local-Bot Lite et préparer votre environnement :

### 1. Cloner le dépôt

Tout d'abord, récupérez le code source depuis GitHub :

git clone https://github.com/tonpseudo/Local-Bot.git
cd Local-Bot

### 2. Créer un environnement virtuel (optionnel mais recommandé)

Créer un environnement virtuel permet d'isoler les dépendances et d'éviter les conflits avec d'autres projets Python :

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate

### 3. Installer les dépendances

Installez toutes les bibliothèques nécessaires pour faire fonctionner l'application :

pip install -r requirements.txt

Cette étape va installer `transformers`, `huggingface-hub`, `torch`, `sentence-transformers`, `customtkinter` (optionnel) et d'autres outils utiles pour les modèles.

---

## Lancer l’application

Pour démarrer l’application, exécutez :

python local.bot.py

À l'ouverture :

- L’application détecte automatiquement les modèles recommandés et vérifie s’ils sont déjà présents sur votre machine.  
- Si un modèle est manquant, il sera téléchargé et placé dans le cache Hugging Face (`~/.cache/huggingface/hub`).  
- Une fois tous les modèles prêts, vous pouvez chatter avec le bot conversationnel ou utiliser les autres modèles pour traduire, générer du code, résumer des textes, ou répondre à des questions.  
- L’interface vous permet de choisir le modèle pour chaque message ou d’utiliser l’option “Auto”, qui sélectionne automatiquement le modèle le plus approprié à votre requête.  
- Chaque réponse indique clairement quel modèle a été utilisé.

---

## Construire un EXE Windows

Si vous souhaitez partager votre application ou l’exécuter sans Python, vous pouvez créer un fichier exécutable Windows :

python build_exe.py

- L’interface propose un bouton “Construire EXE” pour générer l’exécutable.  
- PyInstaller doit être installé (`pip install pyinstaller`).  
- Vous pouvez choisir quels modèles inclure dans l’EXE pour réduire sa taille.  
- L’EXE conserve l’interface complète, y compris la sélection automatique des modèles.

---

## Notes importantes

- **Python 3.9+ est recommandé** pour garantir la compatibilité avec les dernières versions des bibliothèques.  
- Prévoir **au moins 8 GB de RAM** et environ **20 GB d’espace disque** pour stocker les modèles téléchargés.  
- Les modèles plus volumineux peuvent être ajoutés après l’installation si nécessaire.  
- L’interface utilise CustomTkinter si disponible, sinon Tkinter standard.  
- Toutes les réponses du bot affichent le modèle utilisé au début, pour plus de clarté dans vos échanges.  

---

## Dépendances principales

- transformers  
- huggingface-hub  
- sentence-transformers  
- torch  
- customtkinter (optionnel)  
- faiss-cpu (optionnel, pour accélérer les embeddings)
