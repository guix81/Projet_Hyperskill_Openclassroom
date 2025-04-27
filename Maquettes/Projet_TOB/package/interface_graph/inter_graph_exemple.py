import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon premier GUI")
fenetre.geometry("300x150")

# Fonction appelée lors du clic sur le bouton
def dire_bonjour():
    label.config(text="Hello, World!")

# Widget Label (texte)
label = tk.Label(fenetre, text="", font=("Arial", 14))
label.pack(pady=10)

# Widget Bouton
bouton = tk.Button(fenetre, text="Clique moi", command=dire_bonjour)
bouton.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()



fenetre1 = tk.Tk()
fenetre1.title("Texte simple")
fenetre1.geometry("300x100")

# Label avec du texte
label2 = tk.Label(fenetre1, text="Hello, World !", font=("Arial", 14))
label2.pack(pady=20)

fenetre1.mainloop()