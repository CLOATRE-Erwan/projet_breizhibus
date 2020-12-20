# Breizhibus, gestion de lignes de bus


## Conteneu
 * [*bus.sql*](/bdd/bus.sql) : La base de donnée
 * [*main.py*](/python/main.py) : programme principal
 * [*data_base.py*](/python/data_base.py) : classe pour connexion et le traitement de la base de donnée
 * [*bus.py*](/python/bus.py) : classe des bus
 * [*ligne.py*](/python/ligne.py) : classe des ligne de bus
 * [*interface*](/python/interface.py) : classe pour l'interface tkinter
 
## description
Breizhibus souhaite informatiser la gestion de ses lignes de bus. Pour le moment, l'appli n'est prévue que pour une utilisation interne.
La DSI a décidé d'utiliser MySQL et Python pour ce projet. MySQL, car Breizhibus gère les transports de Ploukusanagi, une petit ville. Il n'y a donc pas beaucoup de données à stocker.

## Foncionnement de l'application
### Lancement
Pour lancer l'application il suffit d'executer le fichier [*main.py*](/python/main.py) qui se trouve dans le dossier [*python*](/python)

### Utilisation
#### Interface principale
Une fois l'application ouvert vous tomberais sur l'interface principale
![page principale](/images/page_prin.jpg)

Sur cette interface il y a trois choix : 
* Le bouton *List des Arrets ou des bus par ligne* en rouge
* Le bouton *Modifier un bus* en bleu
* Le bouton *Quitter* en vert
![page prin ann](/images/page_prin_annotations.jpg)

#### Interface d'affichage
Après avoir clické sur le bouton *List des Arrets ou des bus par ligne*, cette interface devrait apparaitre
![page affichage](/images/page_affi_annotations.jpg)

Une fois sur cette interface il vous est possible de choisir parmit les quatre ligne disponible : Rouge, Vert, Bleu et noir (Carré rouge sur l'image ci dessus)
Puis ensuite faire le choix de soit : 
* afficher la list des arrets de cette ligne, bouton *Afficher les arrets* en bleu
* Afficher la list des bus de cette ligne, bouton *Afficher les bus* en vert

Une fois le choix fait la list devrait s'afficher en dessous des boutons

#### Interface de modification
Après avoir clické sur le bouton *Modifier un bus*, cette interface devrait apparaitre
![page modification](/images/page_mod_annotations.jpg)

Une fois sur cette interface il vous est possible d'ajouter, modifier ou supprimer un bus dans la liste

Pour ce faire, il faut remplir les champs suivant (en rouge sur l'image ci dessus) :
* Numero : BB : Numero du bus -> Renter un chiffre allant de 00 a 99
* Immatriculation : Immatriculation du bus -> Renter une suite de caratère d'ont la longeur maximum est 7 (exemple : TE123ST)
* Nombre de place : Nombre de place dans le bus -> Renter un chiffre entier egale au nombre de place dans le bus
* Ligne: La ligne sur la quelle le bus se trouve -> choisir en Rouge, Vert, Bleu ou Noir

Pour ajouter ou modifier un bus il est imperatif de remplire tout les champs, et pour supprimer un bus il suffit de renter le numero du bus et son immatriculation

Une fois les champs remplit il suffit juste de clické sur le bouton crrespondant a l'action voulant être effectué :
* Bouton *Ajouter le bus* en bleu pour ajouter un bus
* Bouton *Modifier le bus* en vert pour modifier le bus
* Bouton *Supprimer le bus* en rose pour suprimer le bus

#### Quitter
Une fois fini avec l'application, il ne rest plus qua la fermer soit en utilisant la croix en haut a droite soit en clckant sur le bouton *Quitter* en vert sur l'image ci dessous
![page modification](/images/page_prin_annotations.jpg)


## Choix technique
### Mysql Connector
*Rappel : La DSI a décidé d'utiliser MySQL et Python pour ce projet.*
Pour ce projet Mysql a été choist par le client pour la base de donnée, de ce faite il fallait trouver un moyen de pouvoit s'y connecter.
Mysql a developé Mysql connector pour remplir cette tache, de par ce fait il a été choisit dans ce projet.

### Python
*Rappel : La DSI a décidé d'utiliser MySQL et Python pour ce projet.*
Python a été choisit par le client pour ce projet.

### tkinter
Pour ce projet le client a demander a ce que l'application possède une interface graphique, il existe plusieur "framework" pour la réaliser comme par exemple gjango, flask et d'autre.

*Rappel : Pour le moment, l'appli n'est prévue que pour une utilisation interne.*

Du faite que le cilent n'a besion que d'une appli en interne et que tkinter demande moins de temps pour pouvoir être utiliser de manière ok, deuxièmement il est aussi plus simple a mattre en place puisque qu'il n'y a que a installer puis importé tkinter dans le code puthon la ou flask ou django par exemple, qui permet de faire des application web, demmande l'instalation d'un serveur web.
Pour ces raison tkinter a été choisit


## Dificulters techniques et solutions
Dans ce projet très peu de difficulter technique ont été renconté.
Il y a quand meme eu quel que petit dificulter avec tkinter pour ne plus afficher une interface et afficher une autre a la place, cette dificulter a été resolut en remplacant la methode ````.destroy()```` par les methodes ````.grid_forget() | .pack_forget()````

lien qui aider a résoudre le problème : https://stackoverflow.com/
