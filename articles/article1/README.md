# Article 1 : 

> [Lien vers l'article](1_NN_Sulc_Fungi_Recognition_A_Practical_Use_Case_WACV_2020_paper.pdf)


# Réseau de neurones convolutifs CNN :
  Réseau inspiré par les animaux
  Pour la reconnaissance d'image on l'a "pave", chq tuile est traité par un neurone (un pixel=> un poids). 
  On a la tuile et une zone " champ récepteur ", les zones se chevauchent pour permettre une cohérence.
  
  On fait des couches pour traiter différentes caractéristiques de l'image, une caractéristique => un noyau de convolution
  
  Nombre de couche => profondeur de la couche de convolution
  
  Profondeur d'un réseau de neurones => nombre de couche de convolution
  
  Volume d'entrée=> Couche de convolution => volume de sortie(image intermédiaire)
  
  AVANTAGES: empreinte mémoire moins importante et on a un poids unique associé aux signaux en entrée
  
  -Couche de convolution:
      Profondeur de la couche= nbt de neurones associés à un même champ recepteur.
      Le pas = contrôle le chevauchement des chmps récepteurs. Plus il est petit, plus il y a chevauchement et plus le volume de sortie est grd
      la marge (zero padding) = mettre des 0 à la frontière du volume d'entrée
                          
  -Couche de pooling(mise en commun): On met un filtre entre deux couches pour réduire la taille spatiale de l'image
  
  -Couche de correction 
