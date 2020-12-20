import mysql.connector
from bus import Bus
from lignes import lignes

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
            nouveau = Bus(id_bus, numero, immatriculation, nombre_place, id_ligne)
            lst_bus.append(nouveau)
        cls.fermer()
        return lst_bus

    @classmethod
    def add_bus(cls, num, imm, nb_pl, id_ligne):
        data = (num, imm, nb_pl, id_ligne)
        cls.connexion()
        cls.cursor.execute("INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_place`, `id_ligne`) VALUES (NULL, %s, %s, %s, %s);",data)
        cls.cnx.commit()
        cls.fermer()

    @classmethod
    def suppr_bus(cls, num, imm):
        data = (num, imm)
        cls.connexion()
        cls.cursor.execute('DELETE FROM bus WHERE bus.numero=%s AND bus.immatriculation=%s',data)
        cls.cnx.commit()
        cls.fermer()

    @classmethod
    def modif_bus(cls, num, imm, nb_pl, id_ligne, id_bus):
        data = (num, imm, nb_pl, id_ligne, id_bus)
        cls.connexion()
        cls.cursor.execute('UPDATE bus SET numero=%s, immatriculation=%s, nombre_place=%s, id_ligne=%s WHERE id_bus=%s',data)
        cls.cnx.commit()
        cls.fermer()

    @classmethod
    def read_dt_lignes(cls):
        lst_lignes =[]
        lst_inter = []
        cls.connexion()
        cls.cursor.execute("SELECT id_ligne, nom_ligne FROM lignes")
        cursor_ligne = cls.cursor.fetchall()
        for id_ligne, nom in cursor_ligne :
            nouveau = lignes(id_ligne, nom, None)
            lst_lignes.append(nouveau)
        cls.fermer()
        return lst_lignes
        
    @classmethod
    def add_arrets(cls, lst):
        cls.connexion()
        for ligne in lst:
            cls.cursor.execute(f"SELECT arrets.id_arret, arrets.nom_arret, arrets.adresse FROM arrets JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret JOIN lignes ON arrets_lignes.id_ligne = lignes.id_ligne WHERE lignes.id_ligne = {ligne.id_ligne}")
            ligne.arrets = cls.cursor.fetchall()
        cls.fermer()