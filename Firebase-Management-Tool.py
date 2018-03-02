import pyrebase

# Configuration l'application avec les donnees d'authentifications de la firebase
config = {
    "apiKey": "AIzaSyCaDaM7-l6h8WPId0oqusaQKsq2OuO5aJ4",
    "authDomain": "ionic-firebase-6b62c.firebaseapp.com",
    "databaseURL": "https://ionic-firebase-6b62c.firebaseio.com",
    "projectId": "ionic-firebase-6b62c",
    "storageBucket": "ionic-firebase-6b62c.appspot.com",
    "messagingSenderId": "846006637866"
};

# On recupere les services de firebase a l'aide des donnees d'authentification
firebase = pyrebase.initialize_app(config)

# On utilise 2 services firebase = storage et database
database = firebase.database();
storage = firebase.storage();

# On recupere toute les colonnes de la table "images"
all_images = database.child('images').get();

# Pour chaque colonnes de la table "images", on utilise le chemin du fichier contenu dans une colonne de la table
# Puis on telecharge les fichiers grace au service "storage" dans le repertoire "images_backup/"
for img in all_images.each():
    path = 'images/' + img.key() + '.png';
    storage.child(path).download('images_backup/' + img.key() + '.png');
