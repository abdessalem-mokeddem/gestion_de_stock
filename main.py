import mysql.connector
from tkinter import *
from tkinter import ttk,messagebox
from produit import *
from categorie import *

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="boutique"
)

# Récupérer les produits et les catégories depuis la base de données
obj_produit = Produit (mydb)

# Créaction graphique
fenetre = Tk()
fenetre.title("Gestion de stock")
fenetre.geometry("800x600")
fenetre.config (bg="#3fb111")
fenetre.resizable(width=False, height=False)
def formulaire():
   
  # Zone de texte de bienvenue
  haut = Label (fenetre,text = "PRODUITS")
  haut.place(x=20,y=70)
  zone_texte = Label (fenetre,text = "Alimentation Abdess", bg= "Green", font=("Times New Roman" , 15)) 
  # zone_texte.config(state = DISABLED)
  zone_texte.place(x =300,y=40)
  
  global nom_produit,entre_description, entre_quantite, entre_categorie, prix_produit
  
  # Créaction du mot nom
  nom = Label(fenetre,text="Nom")
  nom.place(x=40, y=100)
  # Champs pour mettre l'écriture
  nom_produit = Entry(fenetre)
  nom_produit.place(x=80,y=100)


  # Créaction de description
  description = Label(fenetre,text="Description")
  description.place(x=250, y=100)

  # Champs pour mettre la description
  entre_description = ttk.Entry(fenetre)
  entre_description.place(x=330, y=100)

  # Créaction du mot prix
  prix = Label(fenetre,text="Prix  HT")
  prix.place(x=25, y=150)

  #  Champs pour mettre le prix
  prix_produit = Entry(fenetre)
  prix_produit.place(x=80, y=150)

  # Créaction du mot quantité
  quantite = Label(fenetre, text="Quantité")
  quantite.place(x=250, y=150)

  # Créaction de la quantité a choisir
  nombre =["1","2","3","4","5","6","7","8","9","10",
  "11","12","13","14","15","16",
  "17","18","19","20"] 

  # Champs pour mettre quantité
  entre_quantite = ttk.Combobox(fenetre,values=nombre)
  entre_quantite.place(x=320, y=150)

  # Créaction du mot id_catégorie
  categorie = Label(fenetre,text="id_catégorie")
  categorie.place(x=150, y=200)

  # Champ pour mettre id_catégorie
  entre_categorie = Entry(fenetre)
  entre_categorie.place(x=230, y=200)

def liste_produits():
  global listes

  listes=ttk.Treeview(fenetre, columns=(0,1,2,3,4, 5), show="headings" )
  listes.place(x=30 , y=270, width= 700)
  
  listes.heading(0,text="id") 
  listes.heading(1,text="nom")
  listes.heading(2,text="prix") 
  listes.heading(3,text="quantité") 
  listes.heading(4,text="description") 
  listes.heading(5,text="id_categorie")

  listes.column(0,width=5) 
  listes.column(1,width=5)
  listes.column(2,width=5) 
  listes.column(3,width=5) 
  listes.column(4,width=5) 
  listes.column(5,width=5)

  produits=obj_produit.get_produit()
  for row in produits:
     listes.insert("","end", iid=row[0], values=row)
formulaire()
liste_produits()
# Créaction d'un bouton ajouter

def ajout():
    nom = nom_produit.get()
    prix=prix_produit.get()
    quantite=entre_quantite.get()
    id_categorie=entre_categorie.get()
    description=entre_description.get()
    
    obj_produit.set_produit(nom, description,prix, quantite, id_categorie)
    messagebox.showinfo("succes","operation reussi")
    nom_produit.destroy()
    prix_produit.destroy()
    entre_quantite.destroy()
    entre_categorie.destroy()
    entre_description.destroy()
    formulaire()

def supprimer():
    
    id_produits= listes.focus()

    if str (id_produits) != "":
       id_produits = int(id_produits)
       if(messagebox.askyesno("Question","Voulez-vous vraiment supprimer ce produit ?") ):
          listes.delete(id_produits)

          obj_produit.supprimer(id_produits)
          

ajout_bouton = Button(text="Ajouter", command=ajout)
ajout_bouton.place(x=80, y=230)

# Créaction d'un bouton pour supprimer
bouton_supr = Button(text="Suprimer", command=supprimer)
bouton_supr.place(x=160, y=230)

# Créaction du bouton modifier
bouton_modif = Button(text="Modifier")
bouton_modif.place(x=240, y=230)

# Maintenir fenêtre ouverte
fenetre.mainloop()

