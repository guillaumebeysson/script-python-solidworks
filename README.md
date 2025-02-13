# Suppression de la mention SOLIDWORKS dans un PDF

Ce projet permet de **supprimer automatiquement la mention "Produit d'éducation SOLIDWORKS – A titre éducatif uniquement."** dans un fichier PDF, tout en conservant les autres éléments du document.

---

## 🛠️ **Installation**

### 📌 **1. Installer Python (si ce n'est pas encore fait)**

Avant d'exécuter ce script, assurez-vous que Python est installé sur votre PC.

- 📥 **Téléchargez Python** depuis le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)
- 📌 **Pendant l'installation**, cochez la case **"Add Python to PATH"**.
- 📌 **Redémarrer** votre PC.
- Vérifiez que Python est bien installé en exécutant la commande suivante dans l'invite de commande (CMD) :
  ```sh
  python --version
  ```
  Vous devriez voir quelque chose comme : `Python x.x.x`

---

### 📌 **2. Installer PyMuPDF (bibliothèque pour manipuler les PDF)**

Ouvrez l'invite de commande **(CMD)** et exécutez la commande suivante :
```sh
pip install pymupdf
```
Cette commande installe **PyMuPDF**, une bibliothèque permettant de lire et modifier des fichiers PDF.


## 🚀 **Utilisation du script**

1️⃣ **Placez votre script Python (`supprimer_mention.py`), votre fichier Bat (`supprimer_mention.bat`) et vos fichiers PDF dans le même dossier.**

2️⃣ **Créez un dossier `DOSSIER_PDF` où seront stockés les PDF à modifier.**

3️⃣ **Double cliquez sur le fichier (`supprimer_mention.py`) ou sur le fichier (`supprimer_mention.bat`) si le premier ne lance pas l'exécution**

4️⃣ **Les fichiers PDF modifiés seront enregistrés dans un dossier `MODIFIES`.**

---

## 📝 **Explication du fonctionnement**

- Le script **scanne tous les blocs de texte** du PDF.
- Il **trouve le bloc contenant "Produit d'éducation SOLIDWORKS – A titre éducatif uniquement."**
- Il **abaisse légèrement la suppression** pour éviter de supprimer d'autres éléments du document.
- Il **enregistre les fichiers PDF modifiés dans un dossier `MODIFIES`** sans toucher aux fichiers originaux.
- N'hésitez pas à **modifier le script** et ajuster les paramètres **DECALAGE_X et DECALAGE_Y** selon vos besoins.

🚀 **Bonne utilisation !**

