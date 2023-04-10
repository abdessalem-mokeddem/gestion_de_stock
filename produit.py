
class Produit:
    def __init__ (self, connexion):

        self.connexion=connexion
        self.cursor=self.connexion.cursor()

    def get_produit(self):

        demande = "Select * FROM produit"

        self.cursor.execute (demande)
        result=self.cursor.fetchall() 

        return result
    
    def set_produit(self, nom, description, prix, quantite, id_categorie):        

        demande =  "insert into produit (nom , description,prix, quantite,id_categorie) VALUES(%s, %s, %s, %s, %s )"

        donnees=(nom, description, prix, quantite, id_categorie)

        self.cursor.execute (demande, donnees)

        self.connexion.commit()

    def supprimer (self, id_produits):

        demande = "DELETE FROM PRODUIT WHERE id=%s"

        donnees = (id_produits,) 

        self.cursor.execute (demande, donnees)

        self.connexion.commit()


