# Swap Puzzle - Algorithmes de Recherche et Résolution de Graphes d'États

Projet d'exploration algorithmique appliqué à un problème de réorganisation de grille par permutations d'éléments adjacents. Le travail met en œuvre différentes stratégies de résolution dans un espace combinatoire, allant de heuristiques constructives à des algorithmes de parcours de graphes optimisés, complété par une interface graphique interactive et un mode de jeu.

---

## Modélisation et Approches Algorithmiques

### 1. Approche Constructive (Méthode Naïve)
Cette approche consiste à replacer séquentiellement chaque élément à sa position cible définitive par une suite prédéfinie de mouvements verticaux et horizontaux. 
* **Complexité et Comportement** : L'exécution est immédiate en termes de temps de calcul, mais la trajectoire générée est largement sous-optimale et produit un nombre élevé de permutations superflues.

### 2. Exploration en Largeur (BFS sur Graphe d'États)
Le problème est formalisé comme la recherche d'un chemin dans un graphe implicite où chaque nœud représente une configuration globale de la grille et chaque arête un échange valide entre cases adjacentes.
* **Génération dynamique (On-the-fly)** : Afin de s'affranchir de la combinatoire de l'espace des états, le graphe n'est pas instancié en amont mais exploré progressivement à partir de l'état source.
* **Optimisation** : Cette méthode garantit l'optimalité de la solution en trouvant systématiquement le plus court chemin (nombre minimal de swaps).

### 3. Recherche Heuristique (Algorithme A*)
Pour pallier le coût d'exploration de l'algorithme précédent, le parcours en largeur est couplé à une fonction d'évaluation basée sur la **distance de Manhattan** (somme des écarts absolus entre les coordonnées actuelles et cibles de chaque chiffre).
* **Hiérarchisation par file de priorité** : Chaque état est évalué via une fonction de coût combinant la profondeur réelle et l'estimation heuristique restante.
* **Gain de performance** : En guidant l'exploration vers les configurations les plus proches de la solution, l'algorithme réduit drastiquement le nombre de sommets visités et s'avère **sensiblement plus rapide** que le BFS standard.

---

## Visualisation Graphique et Interface Interactive

### Visualisation de Résolution Séquentielle
Une interface permet de charger une grille initiale et d'observer pas à pas la résolution selon l'algorithme choisi. Le parcours de la séquence de swaps permet d'analyser visuellement la trajectoire des états intermédiaires.

### Mode de Jeu Interactif
Une application interactive permet de manipuler directement la grille sous forme de jeu :
* **Graduation de la complexité** : Paramétrage dynamique de la taille des matrices et du degré de mélange initial.
* **Contraintes topologiques** : Intégration de barrières d'interdiction bloquant aléatoirement certaines paires d'échanges adjacents.
* **Analyse comparative** : À l'état final, une métrique compare directement les performances empiriques du joueur avec le seuil optimal calculé par les algorithmes.

---

## Utilisation des Scripts

* Pour voir la complexité et la visualisation graphique, exécutez le script **`esssaie.py`**.
* Pour lancer le mode de jeu interactif, exécutez le script **`Representation.py`**.
