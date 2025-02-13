import fitz
import os
import tkinter as tk
from tkinter import messagebox
import sys

# Dossier contenant les PDFs
DOSSIER_PDF = os.path.dirname(os.path.abspath(__file__))
DOSSIER_SORTIE = os.path.join(DOSSIER_PDF, "MODIFIES")

# Crée un dossier de sortie s'il n'existe pas
os.makedirs(DOSSIER_SORTIE, exist_ok=True)

# Texte à supprimer
TEXTE_A_SUPPRIMER = "Produit d'éducation SOLIDWORKS – A titre éducatif uniquement."

# Décalage pour abaisser la zone de suppression
DECALAGE_Y = 2.5  # Décalage vertical vers le bas
DECALAGE_X = 1.75  # Décalage horizontal

# Listes pour stocker les fichiers modifiés et ceux en erreur
fichiers_modifies = []
fichiers_erreurs = []

# Liste des fichiers PDF
pdf_files = [f for f in os.listdir(DOSSIER_PDF) if f.endswith(".pdf")]

# Vérifier s'il y a des fichiers PDF à traiter
if not pdf_files:
    print("❌ Aucun fichier PDF trouvé dans le dossier.")
    messagebox.showerror("Erreur", "Aucun fichier PDF trouvé dans le dossier.")
    sys.exit(0)  # Quitter immédiatement

print("\n🔍 Début du traitement des fichiers PDF...\n")

# Traitement de chaque PDF dans le dossier
for fichier in pdf_files:
    chemin_pdf = os.path.join(DOSSIER_PDF, fichier)
    chemin_pdf_modifie = os.path.join(DOSSIER_SORTIE, fichier)

    print(f"📄 Analyse du fichier : {fichier}")

    try:
        # Ouvrir le PDF
        doc = fitz.open(chemin_pdf)
        modifie = False  # Indicateur de modification

        for page in doc:
            # Obtenir tous les blocs de texte
            blocs = page.get_text("blocks")

            for bloc in blocs:
                x0, y0, x1, y1, texte, *_ = bloc  # Récupérer coordonnées et texte

                # Ajustement des coordonnées pour déplacer la suppression
                new_x0 = x0 - DECALAGE_X
                new_y0 = y0 + DECALAGE_Y
                new_x1 = x1 - DECALAGE_X
                new_y1 = y1 + DECALAGE_Y

                if TEXTE_A_SUPPRIMER in texte:
                    modifie = True
                    print(f"   - Suppression de la mention sur la page {page.number+1}")
                    # Supprimer uniquement le bloc ajusté
                    page.add_redact_annot((new_x0, new_y0, new_x1, new_y1), fill=None)
                    page.apply_redactions()

        if modifie:
            # Sauvegarde du fichier modifié
            doc.save(chemin_pdf_modifie)
            fichiers_modifies.append(fichier)
            print(f"✔️ {fichier} a été modifié avec succès.")
            print(f"--------------------------------------------")
        else:
            fichiers_erreurs.append(fichier)
            print(f"❌ {fichier} n'a pas été modifié (mention non trouvée).")
            print(f"--------------------------------------------")

        doc.close()

    except Exception as e:
        fichiers_erreurs.append(f"{fichier} (Erreur : {str(e)})")
        print(f"❌ Erreur lors du traitement de {fichier} : {str(e)}")
        print(f"--------------------------------------------")

print("\n✅ Tous les fichiers ont été analysés.\n")

# Générer le message final avec les icônes
message = ""
for fichier in fichiers_modifies:
    message += f"✔️ {fichier} a été modifié avec succès.\n"
for fichier in fichiers_erreurs:
    message += f"❌ {fichier} n'a pas pu être modifié.\n"

# Fonction pour fermer la console après la boîte de dialogue
def fermer_console():
    root.quit()
    root.destroy()
    os._exit(0)  # Force la fermeture immédiate de la console

# Création de la fenêtre Tkinter
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale

# Afficher une boîte de dialogue avec les résultats
messagebox.showinfo("Modification des PDFs", message)

# Fermer proprement Tkinter et la console après le clic sur OK
fermer_console()
