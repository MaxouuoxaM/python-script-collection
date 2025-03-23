import tkinter as tk
from tkinter import scrolledtext
import cohere
from dotenv import load_dotenv
import os

load_dotenv()  # charge les variables du fichier .env
API_KEY = os.getenv("COHERE_API_KEY")
# Initialise Cohere avec ta clé
co = cohere.Client(API_KEY)
# Fonction d'envoi du message
def envoyer_message():
    user_input = entree.get()
    if user_input.strip() == "":
        return

    afficher_message("👤 Toi", user_input)
    entree.delete(0, tk.END)

    try:
        reponse = co.chat(
            message=user_input,
            model="command-r-plus"
        )
        afficher_message("🤖 MaxouBot", reponse.text)
    except Exception as e:
        afficher_message("⚠️ Erreur", str(e))

#Affiche un message dans la zone de chat
def afficher_message(auteur, message):
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"{auteur} : {message}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

# Fenêtre principale
root = tk.Tk()
root.title("Cohere Chatbot")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Zone de chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Champ d'entrée utilisateur
entree = tk.Entry(root, font=("Arial", 12))
entree.pack(padx=10, pady=(0, 10), fill=tk.X)
entree.bind("<Return>", lambda event: envoyer_message())

#  Bouton envoyer
bouton_envoyer = tk.Button(root, text="Envoyer", command=envoyer_message, font=("Arial", 12))
bouton_envoyer.pack(pady=(0, 10))

# Lancer l'appli
root.mainloop()
