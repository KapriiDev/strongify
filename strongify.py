import tkinter as tk
import customtkinter as ctk
import re

def check_password_strength():
    password = password_entry.get()
    score = 0
    message = ""

    if len(password) >= 8:
        score += 1
    else:
        message = "Le mot de passe doit contenir au moins 8 caractères."
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        message = "Le mot de passe doit contenir au moins une lettre majuscule."
    if re.search(r'[0-9]', password):
        score += 1
    else:
        message = "Le mot de passe doit contenir au moins un chiffre."
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        message = "Le mot de passe doit contenir au moins un caractère spécial."
    if score == 4:
        message = "Le mot de passe est sécurisé !"
    elif score == 3:
        message = "Le mot de passe est moyen."
    else:
        message = "Le mot de passe est faible."

    result_label.configure(text=message)
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Vérificateur de Sécurité du Mot de Passe")
root.geometry("400x300")
root.resizable(False, False)

title_label = ctk.CTkLabel(root, text="Vérification du mot de passe", font=("Helvetica", 18, "bold"), text_color="white")
title_label.pack(pady=20)

password_label = ctk.CTkLabel(root, text="Entrez votre mot de passe:", font=("Helvetica", 14), text_color="white")
password_label.pack(pady=5)

password_entry = ctk.CTkEntry(root, width=250, font=("Helvetica", 14), show="*", fg_color="white", text_color="black")
password_entry.pack(pady=10)

check_button = ctk.CTkButton(root, text="Vérifier", font=("Helvetica", 14), command=check_password_strength, fg_color="#05b2dc", hover_color="#0392a6")
check_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12), text_color="white")
result_label.pack(pady=20)

root.mainloop()
