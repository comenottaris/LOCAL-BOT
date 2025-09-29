# Changelog – Local-Bot Lite

## [1.0.0] – 2025-09-29
### Ajouté
- Interface conversationnelle avec bulles et couleurs pour chat.
- Détection automatique et téléchargement des modèles recommandés.
- Support complet : traduction, embeddings, conversation, code, résumé, QA.
- Bouton “Construire EXE” intégré à l’interface.
- Option “auto” pour choisir le modèle adapté à la requête.
- Pipelines fonctionnels 100% local.
- Logger interne avec timestamps.

### Modifié
- Gestion des warnings `pad_token_id` et `max_length` pour pipelines.
- Interface CustomTkinter améliorée, fallback Tkinter.
- Requête utilisateur alignée à droite, réponse du bot à gauche.
- Nom des interlocuteurs affiché en gras et majuscules.

### Corrigé
- Erreurs liées à `local_files_only` dans pipelines.
- Scroll automatique dans chat correctement implémenté.
- Chargement des modèles en thread sans bloquer l’UI.

