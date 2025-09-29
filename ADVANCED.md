# Documentation avancée – Local-Bot Lite

## Structure du projet

- `local.bot.py` : script principal, lance l’interface et gère les modèles.
- `build_exe.py` : script pour construire l’exécutable Windows avec PyInstaller.
- `requirements.txt` : dépendances Python nécessaires.
- `.gitignore` : fichiers à ignorer lors du commit.
- `assets/` : captures d’écran ou fichiers graphiques.
- `docs/` : documentation détaillée (ce fichier, etc.).
- `tests/` : scripts pour tester les fonctionnalités de l’application.

## Pipelines et modèles

| Nom du modèle       | Répertoire | Tâche Hugging Face             | Description |
|--------------------|-----------|--------------------------------|-------------|
| translation         | `Helsinki-NLP/opus-mt-en-fr` | translation | Traduction anglais → français |
| embeddings          | `sentence-transformers/all-MiniLM-L6-v2` | feature-extraction | Extraction d’embeddings pour recherche de similarité |
| conversation        | `microsoft/DialoGPT-small` | text-generation | Chatbot conversationnel |
| code                | `Salesforce/codegen-350M-multi` | text-generation | Génération de code |
| summarization       | `t5-small` | summarization | Résumé de texte |
| qa                  | `distilbert-base-cased-distilled-squad` | question-answering | Questions / réponses sur un contexte |

## Ajouter un nouveau modèle

1. Ajouter l’ID Hugging Face dans `RECOMMENDED_MODELS` dans `local.bot.py`.
2. Spécifier la tâche compatible (`text-generation`, `translation`, `summarization`, etc.).
3. Recharger l’application : le modèle sera téléchargé et prêt à l’usage.

## Paramètres utilisateur

- Cache des modèles : `~/.cache/huggingface/hub` par défaut.
- Interface : CustomTkinter si disponible, sinon Tkinter.
- EXE : bouton “Construire EXE” dans l’interface, nécessite PyInstaller installé.

## Conseils

- Pour éviter des warnings sur `max_length` ou `pad_token_id`, passe explicitement les arguments aux pipelines.
- Pour les modèles volumineux, prévoir 8 GB+ RAM et 20 GB de disque.
- Peut être utilisé 100% offline après téléchargement des modèles.

