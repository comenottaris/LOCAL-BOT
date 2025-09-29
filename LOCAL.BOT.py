import os, threading, time
from pathlib import Path
from typing import Dict, Tuple

# UI imports
try:
    import customtkinter as ctk
    CTK_AVAILABLE = True
except:
    import tkinter as tk
    CTK_AVAILABLE = False

# ---------------- CONFIG MODELS ----------------
RECOMMENDED_MODELS: Dict[str, Tuple[str, str]] = {
    "translation": ("Helsinki-NLP/opus-mt-en-fr", "translation"),
    "embeddings": ("sentence-transformers/all-MiniLM-L6-v2", "feature-extraction"),
    "conversation": ("microsoft/DialoGPT-small", "text-generation"),
    "code": ("Salesforce/codegen-350M-multi", "text-generation"),
    "summarization": ("t5-small", "summarization"),
    "qa": ("distilbert-base-cased-distilled-squad", "question-answering"),
}

# ---------------- Logger ----------------
LOG_MAX_LINES = 400
class Logger:
    def __init__(self):
        self.lines = []

    def write(self, text: str):
        line = f"[{time.strftime('%H:%M:%S')}] {text}"
        self.lines.append(line)
        if len(self.lines) > LOG_MAX_LINES:
            self.lines = self.lines[-LOG_MAX_LINES:]
        print(line)

logger = Logger()
def log(msg): logger.write(msg)

# ---------------- Utils ----------------
def get_cache() -> Path:
    env = os.environ.get("TRANSFORMERS_CACHE")
    return Path(env) if env else Path.home()/".cache"/"huggingface"/"hub"

def ensure_model(repo_id: str) -> bool:
    from huggingface_hub import snapshot_download
    foldername = "models--"+repo_id.replace("/","--")
    path = get_cache()/foldername
    if path.exists(): 
        log(f"{repo_id} déjà installé")
        return True
    try:
        log(f"Téléchargement de {repo_id} ...")
        snapshot_download(repo_id, cache_dir=str(get_cache()))
        log(f"{repo_id} installé")
        return True
    except Exception as e:
        log(f"Erreur téléchargement {repo_id}: {e}")
        return False

def load_pipeline(repo_id: str, task: str):
    try:
        from transformers import pipeline
        return pipeline(task, model=repo_id)  # <-- plus de local_files_only
    except Exception as e:
        log(f"Erreur création pipeline {repo_id} ({task}): {e}")
        return None

# ---------------- CHAT APP ----------------
class AI8BotApp:
    def __init__(self, root):
        self.root = root
        root.title("AI8BOT Chat")
        root.geometry("700x600")

        if CTK_AVAILABLE:
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("dark-blue")
            self.chat_frame = ctk.CTkScrollableFrame(root)
            self.chat_frame.pack(fill="both", expand=True, padx=10, pady=10)
            self.entry_frame = ctk.CTkFrame(root)
            self.entry_frame.pack(fill="x", padx=10, pady=5)
            self.entry = ctk.CTkEntry(self.entry_frame)
            self.entry.pack(side="left", fill="x", expand=True, padx=(0,5))
            self.send_btn = ctk.CTkButton(self.entry_frame, text="Envoyer", command=self.send_message)
            self.send_btn.pack(side="right")
        else:
            self.chat_frame = tk.Frame(root)
            self.chat_frame.pack(fill="both", expand=True, padx=10, pady=10)
            self.scrollbar = tk.Scrollbar(self.chat_frame)
            self.scrollbar.pack(side="right", fill="y")
            self.text_area = tk.Text(self.chat_frame, yscrollcommand=self.scrollbar.set, wrap="word")
            self.text_area.pack(fill="both", expand=True)
            self.scrollbar.config(command=self.text_area.yview)

            self.entry_frame = tk.Frame(root)
            self.entry_frame.pack(fill="x", padx=10, pady=5)
            self.entry = tk.Entry(self.entry_frame)
            self.entry.pack(side="left", fill="x", expand=True, padx=(0,5))
            self.send_btn = tk.Button(self.entry_frame, text="Envoyer", command=self.send_message)
            self.send_btn.pack(side="right")

        self.entry.bind("<Return>", self.send_message)
        self.pipelines: Dict[str, object] = {}

        threading.Thread(target=self.load_models, daemon=True).start()

    def append_bubble(self, sender, msg, user=False):
        if CTK_AVAILABLE:
            bubble = ctk.CTkLabel(self.chat_frame, text=f"{sender}: {msg}", wraplength=500, justify="right" if user else "left",
                                  fg_color="#3a8bcd" if user else "#1f6aa5", corner_radius=10, anchor="e" if user else "w", padx=10, pady=5)
            bubble.pack(anchor="e" if user else "w", pady=5, padx=5)
            self.chat_frame.update_idletasks()
        else:
            self.text_area.insert("end", f"{sender}: {msg}\n")
            self.text_area.see("end")

    def load_models(self):
        self.append_bubble("SYSTEM", "Chargement des modèles, patience...", False)
        log("Chargement des modèles...")
        for key, (repo, task) in RECOMMENDED_MODELS.items():
            if ensure_model(repo):
                pipe = load_pipeline(repo, task)
                if pipe:
                    self.pipelines[key] = pipe
        log("Tous les modèles chargés")
        self.append_bubble("SYSTEM", "Tous les modèles prêts ! Vous pouvez discuter.", False)
        self.entry.configure(state="normal")

    def detect_bot(self, text: str):
        text = text.lower()
        if any(w in text for w in ["comment", "qui", "que", "quand", "où", "quel"]):
            return "qa"
        if any(w in text for w in ["def", "function", "code", "script", "{", "class"]):
            return "code"
        if any(w in text for w in ["résumé", "summarize", "summary"]):
            return "summarization"
        if any(w in text for w in ["bonjour","hello","salut"]):
            return "conversation"
        return "translation"

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if not msg: return
        self.entry.delete(0,"end")
        self.append_bubble("VOUS", msg, user=True)

        bot_key = self.detect_bot(msg)
        bot_model = self.pipelines.get(bot_key)
        if not bot_model:
            self.append_bubble("BOT", "[Bot non disponible]", False)
            return

        try:
            if bot_key in ["conversation","code"]:
                out = bot_model(msg)
                out_text = out[0]["generated_text"] if isinstance(out, list) and "generated_text" in out[0] else str(out)
            elif bot_key == "translation":
                out = bot_model(msg)
                out_text = out[0]["translation_text"] if isinstance(out, list) and "translation_text" in out[0] else str(out)
            elif bot_key == "summarization":
                out = bot_model(msg)
                out_text = out[0]["summary_text"] if isinstance(out, list) and "summary_text" in out[0] else str(out)
            elif bot_key == "qa":
                out = bot_model(question=msg, context=msg)
                out_text = out.get("answer", str(out))
            self.append_bubble(f"BOT ({bot_key.upper()})", out_text, False)
        except Exception as e:
            self.append_bubble("BOT", f"[Erreur]: {e}", False)

# ---------------- MAIN ----------------
def main():
    if CTK_AVAILABLE:
        import customtkinter as ctk
        root = ctk.CTk()
    else:
        import tkinter as tk
        root = tk.Tk()
    app = AI8BotApp(root)
    root.mainloop()

if __name__=="__main__":
    main()
