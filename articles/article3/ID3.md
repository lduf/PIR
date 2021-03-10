# L'algorithme ID3 :

L'algorithme ID3 est un algorithme de classification supervisé. Il se base donc sur un ensemble classé pour déterminer un modèle de classification ; ce modèle est un **arbre de décision**

### L'algorithme :

​		Les ensembles d'entrées sont constitués d'attributs, l'un d'entre eux est ***la cible*** les autres sont ***non cible***. On prédit la valeur de la cible par rapport aux autres valeurs. ID3 construit l'arbre récursivement.

```
fonction ID3(exemples, attributCible, attributsNonCibles)
   si exemples est vide alors /* Nœud terminal */
       retourner un nœud Erreur
   sinon si attributsNonCibles est vide alors /* Nœud terminal */
       retourner un nœud ayant la valeur la plus représentée pour attributCible
   sinon si tous les exemples ont la même valeur pour attributCible alors /* Nœud terminal */
       retourner un nœud ayant cette valeur
   sinon /* Nœud intermédiaire */
       attributSélectionné = attribut maximisant le gain d'information parmi attributsNonCibles
       attributsNonCiblesRestants = suppressionListe(attributsNonCibles, attributSélectionné)
       nouveauNœud = nœud étiqueté avec attributSélectionné
       
       pour chaque valeur de attributSélectionné faire
           exemplesFiltrés = filtreExemplesAyantValeurPourAttribut(exemples, attributSélectionné, valeur)
           nouveauNœud->fils(valeur) = ID3(exemplesFiltrés, attributCible, attributsNonCiblesRestants)
       finpour
       
       retourner nouveauNœud
```

> Source : [Wikipédia](https://fr.wikipedia.org/wiki/Algorithme_ID3)