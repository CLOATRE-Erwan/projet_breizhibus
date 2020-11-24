import mysql.connector
from bus import bus
from lignes import lignes
from arrets import arrets

class data_base:
    #user = "root"
    #"password": "root",
    #"host": "localhost",
    #"port": "8081",
    #"database": "microsoftIA"}

    @classmethod
    def connexion(cls):
        cls.cnx = mysql.connector.connect(user = "root", password= "root", host="localhost", port="8081", database="bus")
        cls.cursor = cls.cnx.cursor()
        
    @classmethod
    def fermer(cls):
        cls.cursor.close()
        cls.cnx.close()

    @classmethod
    def read_dt_bus(cls):
        lst_bus =[]
        cls.connexion()
        query = "SELECT id_bus, numero, immatriculation, nombre_place, id_ligne FROM bus"
        cls.cursor.execute(query)
        for id_bus, numero, immatriculation, nombre_place, id_ligne in cls.cursor :
            nouveau = bus(id_bus, numero, immatriculation, nombre_place, id_ligne)
            lst_bus.append(nouveau)
        cls.fermer()
        return lst_bus

    @classmethod
    def read_dt_lignes(cls):
        lst_lignes =[]
        cls.connexion()
        query = "SELECT id_ligne, nom FROM lignes"
        cls.cursor.execute(query)
        for id_ligne, nom in cls.cursor :
            nouveau = lignes(id_ligne, nom, id_bus = None)
            lst_lignes.append(nouveau)
        cls.fermer()
        return lst_lignes
        
    @classmethod
    def read_dt_arrets(cls):
        lst_arrets =[]
        cls.connexion()
        query = "SELECT id_arret, nom, adresse FROM arrets"
        cls.cursor.execute(query)
        for id_arret, nom, adresse in cls.cursor :
            nouveau = arrets(id_arret, nom, adresse)
            lst_arrets.append(nouveau)
        cls.fermer()
        return lst_arrets

    #def create(self):
        #self.cursor.execute("ALTER TABLE apprenants ADD mail VARCHAR(50) NOT NULL AFTER photo")
    
    #def envoie(self, data, id):
        #ref = (data, id)
        #self.cursor.execute('''UPDATE apprenants SET mail=(%s) WHERE id_apprenants = (%s)''', ref)
        #self.cnx.commit()

