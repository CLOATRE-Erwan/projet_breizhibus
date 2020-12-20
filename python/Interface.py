from tkinter import *
from tkinter.messagebox import *
from data_base import data_base

class Interface():
    
    def __init__(self):
        self.fenetre = Tk()
        self.ligne = data_base.read_dt_lignes()
        self.lst = StringVar()
        self.bus = data_base.read_dt_bus()
        self.lst_info_bus = []

        data_base.add_arrets(self.ligne)



        self.fenetre.geometry('840x560')       
        
        
        
        # Création de nos widgets  
        # Menu "fichier"  
        self.menubar = Menu(self.fenetre)
        #Menu Fichier
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="coming soon", command=self.alert)
        self.menu1.add_command(label="coming soon", command=self.alert)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quitter", command=self.callback_fun)
        self.menubar.add_cascade(label="Fichier", menu=self.menu1)
        #Menu Editer
        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="coming soon", command=self.alert)
        self.menu2.add_command(label="coming soon", command=self.alert)
        self.menu2.add_command(label="coming soon", command=self.alert)
        self.menubar.add_cascade(label="Editer", menu=self.menu2)
        #Menu Aide
        self.menu3 = Menu(self.menubar, tearoff=0)
        self.menu3.add_command(label="Tips", command=self.alert_tips)
        self.menubar.add_cascade(label="Aide", menu=self.menu3)

        self.fenetre.config(menu=self.menubar)

        #Frame du tiere
        self.frame_titre = Frame(self.fenetre)
        self.frame_titre.pack(fill=BOTH,pady=50)
        #Titre
        self.titre = Label(self.frame_titre, text="BREIZHIBUS", font = ("Arial", 50))
        self.titre.pack(fill=BOTH)

        #Frame du menu choix
        self.frame_choix_option = Frame(self.fenetre, bg='red')
        self.frame_choix_option.pack()
        #Bouton list des arret
        self.bouton_choix_option = Button(self.frame_choix_option, text="Liste des Arrets ou des bus par lignes",padx=60, command=self.ui_lst_arret)
        self.bouton_choix_option.grid(row=1, column=0)
        #bouton modif bus
        self.bouton_choix_option = Button(self.frame_choix_option, text="Modifier un bus", padx=60, command=self.ui_bus)
        self.bouton_choix_option.grid(row=1, column=1)
        #bouton quitter
        self.bouton_quitter = Button(self.frame_choix_option, text="Quitter", command=self.callback_fun)
        self.bouton_quitter.grid(row=1, column=2)

        #frame du "corp" de l'app partie liste arret/bus
        self.frame_choix = Frame(self.fenetre)
        #choix des lignes
        self.var_choix = StringVar()
        self.choix_rouge = Radiobutton(self.frame_choix, text="Rouge", variable=self.var_choix, value="Rouge")
        self.choix_vert = Radiobutton(self.frame_choix, text="Vert", variable=self.var_choix, value="Vert")
        self.choix_bleu = Radiobutton(self.frame_choix, text="Bleu", variable=self.var_choix, value="Bleu")
        self.choix_noir = Radiobutton(self.frame_choix, text="Noir", variable=self.var_choix, value="Noir")
        #bouton validation
        self.bouton_choix_arret = Button(self.frame_choix, text="Afficher les arrets", command=self.affichage_arrets)
        self.bouton_choix_bus = Button(self.frame_choix, text="Afficher les bus", command=self.affichage_bus)

        #frame de l'affichage
        self.frame_rep = Frame(self.fenetre)
        #label pour afficher
        self.rep = Label(self.frame_rep, textvariable=self.lst, font = ("Arial", 12))
        
        #frame du "corp" de l'app partie modif bus
        self.frame_bus = Frame(self.fenetre)
        #nom du bus a entrer
        self.var_name_bus = StringVar()
        self.name_bus_b = Label(self.frame_bus, text="Numero :   BB")
        self.name_bus_a = Entry(self.frame_bus, bd =5, textvariable=self.var_name_bus)
        #immatriculation du bus a entrer
        self.var_imm_bus = StringVar()
        self.imm_bus_b = Label(self.frame_bus, text="Immatriculation : ")
        self.imm_bus_a = Entry(self.frame_bus, bd =5, textvariable=self.var_imm_bus)
        #nombre de place du bus a entrer
        self.var_nb_pl_bus = IntVar()
        self.nb_pl_bus_b = Label(self.frame_bus, text="Nombre de place : ")
        self.nb_pl_bus_a = Entry(self.frame_bus, bd =5, textvariable=self.var_nb_pl_bus)
        #choix de la ligne du bus
        self.ligne_bus_b = Label(self.frame_bus, text="Ligne : ")
        self.var_choix_id_ligne = IntVar()
        self.choix_1 = Radiobutton(self.frame_bus, text="Rouge", variable=self.var_choix_id_ligne, value=1)
        self.choix_2 = Radiobutton(self.frame_bus, text="Vert", variable=self.var_choix_id_ligne, value=2)
        self.choix_3 = Radiobutton(self.frame_bus, text="Bleu", variable=self.var_choix_id_ligne, value=3)
        self.choix_4 = Radiobutton(self.frame_bus, text="Noir", variable=self.var_choix_id_ligne, value=4)
        #bouton de validation
        self.bouton_aj_bus = Button(self.frame_bus, text="Ajouter le bus", command=self.ajout_bus)
        self.bouton_mod_bus = Button(self.frame_bus, text="Modifier le bus", command=self.modif_bus)
        self.bouton_sup_bus = Button(self.frame_bus, text="Supprimer le bus", command=self.suppr_bus)


        self.fenetre.mainloop()
        
    def alert(self):
        showinfo("alerte", "Bravo!")

    def alert_tips(self):
        showinfo("Petit tips :)", "place_forget() / grid_forget() / pack_forget() c'est mieux de .destroy()")

    def callback_fun(self):
        if askyesno('Comfirmation', 'Êtes-vous sûr de vouloir faire ça?'):
            showwarning(' :( ', 'Tant pis...')
            showerror("Erreur 418", "Oups, une erreur est survenu\n code ereure : 418")
            self.fenetre.quit()
        else:
            showinfo(':) ', 'Tant mieux :)')

    #fonction pour afficher la liste des arret en fonction de la ligne choisit
    def affichage_arrets(self):
        for ligne in self.ligne:
            if ligne.nom == self.var_choix.get():
                self.lst.set(ligne.arrets)

    #fonction pour afficher les liste des bus en fonction de la ligne choisit
    def affichage_bus(self):
        self.bus = data_base.read_dt_bus()
        lst_bus = []
        for ligne in self.ligne:
            if ligne.nom == self.var_choix.get():
                for bus in self.bus:
                    if bus.id_ligne == ligne.id_ligne:
                        lst_bus.append(bus.numero)
                        self.lst.set(lst_bus)

    #methode pour ajouter un bus a la base de donnée
    def ajout_bus(self):
        self.bus = data_base.read_dt_bus()
        bus_name = 'BB' + self.var_name_bus.get()
        lst = []
        if askyesno('Comfirmation', 'Êtes-vous sûr de vouloir faire ça?'):
            for bus in self.bus:
                lst.append(bus.numero)
            if bus_name not in lst:                  
                data_base.add_bus(bus_name, self.var_imm_bus.get(), self.var_nb_pl_bus.get(), self.var_choix_id_ligne.get())
                showinfo('Ajout', 'Le bus a été ajouté :)')
                return
            else:
                showwarning('Attention !', 'Un bus porte deja ce nom')


    def suppr_bus(self):
        self.bus = data_base.read_dt_bus()
        bus_name = 'BB' + self.var_name_bus.get()
        verif = True
        if askyesno('Comfirmation', 'Êtes-vous sûr de vouloir faire ça?'):
            for bus in self.bus:
                if bus_name in bus.numero and self.var_imm_bus.get() in bus.immatriculation:
                    data_base.suppr_bus(bus_name, self.var_imm_bus.get())
                    showinfo('Suppression', 'Le bus a été supprimé :)')
                    return
                else:
                    verif = False
            if verif == False:
                showwarning(' Attention !', "Le bus n'existe pas")

    def modif_bus(self):
        self.bus = data_base.read_dt_bus()
        bus_name = 'BB' + self.var_name_bus.get()
        verif = True
        if askyesno('Comfirmation', 'Êtes-vous sûr de vouloir faire ça?'):
            for bus in self.bus:
                if bus_name in bus.numero and self.var_imm_bus.get() in bus.immatriculation:
                    data_base.modif_bus(bus_name, self.var_imm_bus.get(), self.var_nb_pl_bus.get(), self.var_choix_id_ligne.get(), bus.id_bus)
                    showinfo('Modification', 'Le bus a été modifié :)')
                    return
                else:
                    verif = False
            if verif == False:
                showwarning(' Attention !', "Le bus n'existe pas")


    

    #fonction pour afficher l'onglet liste arrets/bus
    def ui_lst_arret_pack(self):
        self.frame_choix.pack(pady=30)
        self.choix_rouge.grid(row=1, column=0)
        self.choix_vert.grid(row=1, column=1)
        self.choix_bleu.grid(row=1, column=2)
        self.choix_noir.grid(row=1, column=3)
        self.bouton_choix_arret.grid(row=2, column=0, pady=10)
        self.bouton_choix_bus.grid(row=2, column=1, pady=10)
        self.frame_rep.pack(pady=30)
        self.rep.pack()
    #fonction pour cacher l'onglet liste arrets/bus
    def ui_lst_arret_destroy(self):        
        self.frame_choix.pack_forget()
        self.choix_rouge.grid_forget()
        self.choix_vert.grid_forget()
        self.choix_bleu.grid_forget()
        self.choix_noir.grid_forget()
        self.bouton_choix_arret.grid_forget()
        self.bouton_choix_bus.grid_forget()
        self.frame_rep.pack_forget()
        self.rep.pack_forget()

    #fonction pour afficher l'onglet modification de bus
    def ui_bus_pack(self):
        self.frame_bus.pack(pady=30)
        self.name_bus_b.grid(row=1, column=0)
        self.name_bus_a.grid(row=1, column=1)
        self.imm_bus_b.grid(row=2, column=0)
        self.imm_bus_a.grid(row=2, column=1)
        self.nb_pl_bus_b.grid(row=3, column=0)
        self.nb_pl_bus_a.grid(row=3, column=1)
        self.ligne_bus_b.grid(row=4, column=0)
        self.choix_1.grid(row=4, column=1)
        self.choix_2.grid(row=5, column=1)
        self.choix_3.grid(row=6, column=1)
        self.choix_4.grid(row=7, column=1)
        self.bouton_aj_bus.grid(row=8, column=0)
        self.bouton_mod_bus.grid(row=8, column=1)
        self.bouton_sup_bus.grid(row=8, column=2)
    #fonction pour cacher l'onglet modification de bus
    def ui_bus_pack_forget(self):
        self.frame_bus.pack_forget()
        self.name_bus_b.pack_forget()
        self.name_bus_a.pack_forget()
        self.imm_bus_b.grid_forget()
        self.imm_bus_a.grid_forget()
        self.nb_pl_bus_b.grid_forget()
        self.nb_pl_bus_a.grid_forget()
        self.ligne_bus_b.grid_forget()
        self.choix_1.grid_forget()
        self.choix_2.grid_forget()
        self.choix_3.grid_forget()
        self.choix_4.grid_forget()
        self.bouton_aj_bus.grid_forget()
        self.bouton_mod_bus.grid_forget()
        self.bouton_sup_bus.grid_forget()

    #fonction de bouton_choix_arret pour afficher l'onglet liste arrets/bus et cacher l'onglet modif bus
    def ui_lst_arret(self):
        self.ui_lst_arret_pack()
        self.ui_bus_pack_forget()
    #fonction de bouton_choix_bus pour afficher l'onglet modif bus et cacher l'onglet liste arrets/bus
    def ui_bus(self):
        self.ui_lst_arret_destroy()
        self.ui_bus_pack()