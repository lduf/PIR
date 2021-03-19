# Techniques pour analyser les textures
## Sur matlab:
L'analyse de texture fait référence à la caractérisation des régions d'une image par leur contenu en texture. L'analyse de texture tente de quantifier les qualités intuitives décrites par des termes tels que rugueux, lisse, soyeux ou bosselé en fonction de la variation spatiale des intensités des pixels. En ce sens, la rugosité ou le caractère bosselé fait référence aux variations des valeurs d'intensité, ou niveaux de gris.

### Fonctions matlab:
| Fonction     | Description                                       |
|--------------|---------------------------------------------------|
| entropy      | Entropy of grayscale image                        |
| entropyfilt  | Local entropy of grayscale image                  |
| rangefilt    | Local range of image                              |
| stdfilt      | Local standard deviation of image                 |
| graycomatrix | Create gray-level co-occurrence matrix from image |
| graycoprops  | Properties of gray-level co-occurrence matrix     |


https://fr.mathworks.com/help/images/texture-analysis-1.html#:~:text=Texture%20analysis%20refers%20to%20the,spatial%20variation%20in%20pixel%20intensities.

## Avec python:
On utilise en général LBP: le Local Binary Pattern. C'est un opérateur de texture simple mais très efficace qui étiquette les pixels d'une image en seuillant le voisinage de chaque pixel et considère le résultat comme un nombre binaire.
![alt text](http://www.scholarpedia.org/w/images/thumb/7/77/LBP.jpg/400px-LBP.jpg)
### Principe du LBP:
L'idée de base pour le développement de l'opérateur LBP était que les textures de surface bidimensionnelles peuvent être décrites par deux mesures complémentaires : les motifs spatiaux locaux et le contraste d'échelle de gris. L'opérateur LBP original (Ojala et al. 1996) forme des étiquettes pour les pixels de l'image en seuillant le voisinage 3 x 3 de chaque pixel avec la valeur centrale et en considérant le résultat comme un nombre binaire. L'histogramme de ces 2^8 = 256 étiquettes différentes peut alors être utilisé comme descripteur de texture. 

Traduit avec www.DeepL.com/Translator (version gratuite)

https://www.youtube.com/watch?v=_5ktOnEZ3O4
https://github.com/maponti/imageprocessing_course_icmc/blob/master/07b_texture_descriptors.ipynb
http://www.scholarpedia.org/article/Local_Binary_Patterns#:~:text=Local%20Binary%20Pattern%20(LBP)%20is,result%20as%20a%20binary%20number.
