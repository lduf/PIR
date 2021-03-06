# Article 2 : Mushroom Images Identification Using Orde 1 Statistics Feature Extraction with Artificial Neural Network Classification Technique

> [Lien vers l'article](2_NN_Mushroom_Images_Identification_Using_Orde_1_Statis.pdf)

**But:** Identifier l'espece d'un champignon. La reconnaissance de pattern est facile pour les humains mais peu pour les ordinateurs, on utilise donc un réseau de neurones artificiels (permet d'apprendre par l'entrainement).

**Méthode:**
- Images converties en teinte de gris pour la reconnaissance de pattern 
- Database divisée en deux: une partie pour apprendre, une partie pour tester
- Méthode de feature extraction utilisant des stats d'odre 1
- Backpropagration training: base du deep learning, permet d'apprendre

**Conclusion:** La précision du système de reconnaissance d'image est fortement influencée par les parametres internes du réseau de neurones comme le nombre d'hidden layer, dez neurones etc.   
Le plus haut taux de précision atteint ici est de 93% ce qui est tres satisfaisant.  
Pour aller plus loin dans les recherches on pourrait essayer en couleur par exemple.

**11/03/2021: Réseau de neurones** voir réseau de neurones : https://github.com/lduf/PIR/tree/main/reseau_de_neurone  

**19/03/2021: Feature Extraction**  
Feature extraction (extraction de caractéristiques)  
Caractéristiques : but = donner des informations non redondantes pour faciliter l’apprentissage du réseau de neurones.  
Utilisé quand la taille des datas d’entrée est trop grande pour être efficace (cf. pattern la semaine dernière) ou trop redondante (par ex : pixel d'une image)  
Suppositions caractéristiques champignons : pied, chapeau, lamelles/pores, silhouette ?   
Pour étudier ces caractéristiques, Article : stats d’ordre, utilise probabilité de la présence de certaines valeurs de degré de gris dans une zone de l’image. L’histogramme de l’image. Ensuite de ces valeurs, calcul de stats d’ordre 1 : moyenne, skewness (l’asymétrie), variance, kurtosis (aplatissement), entropie  
