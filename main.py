from data_base import data_base
from bus import bus

def main():
    dt_bus = data_base.read_dt_bus()
    dt_lignes = data_base.read_dt_lignes()
    dt_arrets = data_base.read_dt_arrets()
    #for bus in dt_bus:
        #print(bus.id_bus,bus.numero, bus.immatriculation, bus.nombre_place, bus.id_ligne)
    
    for ligne in dt_lignes:
        print(ligne.id_ligne, ligne.nom) 

    for arret in dt_arrets:
        print(arret.id_arret, arret.nom, arret.adresse)   



main()