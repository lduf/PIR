# Article 3 : Algorithmes pour identifer les champignons comestibles

> [Lien vers l'article](3_Compare_Prosiding-ICOIACT-Yogja.pdf)

## Résumé et résultats :

**But :** Identifier le meilleur algorithme pour la reconnaissance de champignons comestibles

La comparaison des **3 algos** se base sur :

- La fiabilité des résultats
- La vitesse d'exécution

Les algos comparés sont : 

- C4.5
- Naive Bayes 
- Support Vector Machine (SVM)

**Résultats :** 

L'algorithme **C4.5** est le plus fiable et le plus rapide.

|                      | C4.5 | Naive Bayes | SVM  |
| :------------------: | :--: | :---------: | :--: |
|      Fiabilité       | 100% |  95.8887 %  | 100% |
| Temps éxécution (ms) | 180  |     340     | 320  |

## Étude plus détaillée

### C4.5 :

#### Vu par l'article :

L'article nous apprend que le C4.5 est l'algorithme le plus efficace. Il fonctionne sous forme d'arbre de décision, on peut donc récupérer les catégories de triage les plus importantes selon l'algorithme :

- Odor
- Sport-print-color
- Gill-size
- Gill-spacing
- Population

#### Recherches complémentaires :

Cet algorithme est basé sur [l'algorithme ID3](ID3.md)

### Naive Bayes :



### Support Vector Machine (SVM) :

