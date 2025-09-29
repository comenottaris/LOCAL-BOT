# build_exe.py
import os
import subprocess
import sys
from pathlib import Path

# ---------------- CONFIG ----------------
SCRIPT_NAME = "local.bot.py"  # fichier principal
DIST_DIR = "dist"
BUILD_DIR = "build"
MODELS = [
    "translation",
    "embeddings",
    "conversation",
    "code",
    "summarization",
    "qa"
]

def choose_models():
    print("Sélectionnez les modèles à inclure (séparer par des virgules) :")
    for i, m in enumerate(MODELS, start=1):
        print(f"{i}: {m}")
    choice = input("Exemple: 1,3,5 (ou ENTER pour tous): ").strip()
    if not choice:
        return MODELS
    selected = []
    for i in choice.split(","):
        try:
            idx = int(i)-1
            if 0 <= idx < len(MODELS):
                selected.append(MODELS[idx])
        except:
            pass
    return selected

def main():
    selected_models = choose_models()
    print("Modèles sélectionnés :", selected_models)

    # Construire la commande PyInstaller
    cmd = [
        sys.executable,
        "-m", "PyInstaller",
        "--onefile",           # tout dans un seul exe
        "--noconsole",         # supprime la console (optionnel)
        "--name", "AI8Bot",
        SCRIPT_NAME
    ]

    # Ajouter des options pour inclure les modèles
    # Ici on peut copier les dossiers des modèles dans le package si besoin
    # Exemple : --add-data "path_to_model;models/translation"
    # Pour simplifier, on suppose que le script gère le téléchargement local des modèles

    print("Lancement de la génération de l'exécutable...")
    subprocess.run(cmd)
    print(f"EXE généré dans le dossier {DIST_DIR}")

if __name__ == "__main__":
    main()
