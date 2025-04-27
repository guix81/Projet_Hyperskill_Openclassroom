import tkinter as tk         # Importation du module Tkinter pour l'interface graphique
import subprocess            # Importation du module subprocess pour exécuter des commandes système

# Fonction qui sera appelée lorsqu'on clique sur le bouton
def lancer_ping():
    # Définition de la commande ping (pour Linux/Mac). Pour Windows, remplace "-c" par "-n"
    commande = ["ping", "-c", "4", "google.com"]
    
    try:
        # Exécution de la commande avec subprocess.run
        # capture_output=True : on capture la sortie (stdout et stderr)
        # text=True : on récupère la sortie en tant que texte (pas en binaire)
        # check=True : lève une exception si la commande échoue
        resultat = subprocess.run(commande, capture_output=True, text=True, check=True)
        
        # On vide la zone de texte avant d'afficher le nouveau résultat
        zone_texte.delete(1.0, tk.END)
        # On insère le résultat dans la zone de texte
        zone_texte.insert(tk.END, resultat.stdout)
    
    except subprocess.CalledProcessError as e:
        # En cas d'erreur, on affiche l'erreur dans la zone de texte
        zone_texte.delete(1.0, tk.END)
        zone_texte.insert(tk.END, f"Erreur : {e}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Test Ping")         # Titre de la fenêtre
fenetre.geometry("500x300")        # Dimensions de la fenêtre

# Création d’un bouton pour lancer le ping
bouton = tk.Button(fenetre, text="Lancer ping", command=lancer_ping)
bouton.pack(pady=10)               # On l'affiche avec un petit espace vertical

# Création d'une zone de texte pour afficher le résultat du ping
zone_texte = tk.Text(fenetre, wrap="word")  # wrap="word" pour éviter que les mots soient coupés
zone_texte.pack(expand=True, fill="both", padx=10, pady=10)  # S'étend avec la fenêtre, marges internes

# Boucle principale Tkinter (affiche la fenêtre et attend les actions utilisateur)
fenetre.mainloop()