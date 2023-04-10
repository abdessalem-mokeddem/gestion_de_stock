class categorie:
    def __init__ (self, connexion):

        self.connexion=connexion
        self.cursor=self.connexion.cursor()

    def get_categorie(self):

        demande = "Select * FROM categorie"

        self.cursor.execute (demande)
        result=self.cursor.fetchall() 

        return result