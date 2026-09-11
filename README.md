# Swap Puzzle - Résolution de Grilles et Mode Jeu

Projet de résolution d'un jeu de grille où l'objectif est de remettre des nombres mélangés dans le bon ordre en échangeant des cases adjacentes. Ce projet compare plusieurs méthodes de résolution algorithmique et propose des interfaces graphiques pour visualiser les solutions ou jouer directement.

---

## Les Algorithmes de Résolution

### 1. La méthode naïve
Elle replace chaque numéro un par un de façon séquentielle. 
* **Résultat** : C'est très rapide à calculer, mais cela génère un nombre de mouvements beaucoup trop élevé.

### 2. Le parcours en largeur (BFS)
Cette méthode explore toutes les combinaisons possibles sous forme de graphe pour trouver le chemin optimal.
* **Résultat** : Elle garantit le nombre minimal de coups pour résoudre la grille, avec une recherche construite au fur et à mesure pour éviter de saturer la mémoire.

### 3. L'algorithme optimisé (A*)
Il s'agit d'une amélioration du parcours en largeur, guidée par une estimation des distances (la distance de Manhattan) pour savoir si l'on se rapproche de la solution.
* **Résultat** : Il trouve le chemin optimal **beaucoup plus rapidement** en évitant d'explorer des configurations inutiles.

---

## Visualisation et Mode de Jeu

### Visualisation de la résolution (`esssaie.py`)
Ce script permet de voir les algorithmes en action. Vous pouvez y observer et comparer la complexité et le nombre d'étapes de la méthode naïve face à la méthode optimale, avec un affichage graphique pas à pas.

### Mode de Jeu Interactif (`Representation.py`)
Un jeu complet pour tester vos compétences sur la grille :
* **Niveaux de difficulté** : Tailles de grilles variables et mélanges plus ou moins complexes.
* **Pièges** : Présence de barrières aléatoires qui bloquent certains échanges.
* **Score final** : Votre nombre de coups est comparé à celui de l'algorithme optimal à la fin de la partie.

---

## Utilisation

* Pour voir la complexité et la visualisation graphique, exécutez le script **`esssaie.py`**.
* Pour lancer le mode de jeu interactif, exécutez le script **`Representation.py`**.
