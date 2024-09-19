from grid import Grid
from graph import Graph
import matplotlib.pyplot as plt
import numpy as np
import heapq

class Solver(Grid): 
    """
    A solver class, to be implemented.
    """
    def __init__(self,m, n, initial_state = []):
        super().__init__(m, n, initial_state)

    def ancien_placement(self,num):
        """
        Cette fonction nous permettera de connaitre l'ancien placement
        """
        for k in range(self.n): 
            for l in range(self.m):
                if num==self.state[l][k]:
                   i=l
                   j=k
        return [i,j]  

    def nouveau_placement(self,num):
        """
        cette fonction nous permettera de trouver où un numéro doit être placer dans la grille
        """
        trie=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)]
        for k in range(self.n): 
            for l in range(self.m):
                if num==trie[l][k]:
                    i=l
                    j=k
        return [i,j]
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        liste=[]
        for i in range(1,(self.m)*(self.n)+1): # on parcours l'ensemble des nombres de la grille
            m=self.ancien_placement(i)[0]
            n=self.ancien_placement(i)[1]
            for k in range(m,self.m-1): # on déplace le nombre tout en bas, de manière vertical
                self.swap((k,n),(k+1,n))
                liste=liste+[((k,n),(k+1,n))]
            for k in range(n,self.n-1): # on déplace le nombre tout à droite, de manière horizontale
                self.swap((self.m-1,k),(self.m-1,k+1))
                liste=liste+[((self.m-1,k),(self.m-1,k+1))]
            m1=self.nouveau_placement(i)[0]
            n1=self.nouveau_placement(i)[1]
            for k in range(self.m-1,m1,-1): # on déplace le nombre en haut jusqu'à atteindre la ligne du bon placement j=
                self.swap((k,self.n-1),(k-1,self.n-1))
                liste=liste+[((k,self.n-1),(k-1,self.n-1))]
            for k in range(self.n-1,n1,-1): # on déplace le nombre à gauche j=> atteindre la colonne du bon placement
                self.swap((m1,k),(m1,k-1))
                liste=liste+[((m1,k),(m1,k-1))]
        return liste

    def repres(self):
        """
        Fait une représentation grpahique de la matrice avec matplotlib
        """
        plt.imshow(self.state)  
        for i in range(len(self.state)):  
            for j in range(len(self.state[0])):
                plt.text(j, i, str(self.state[i][j]), ha='center', va='center', color='white')
        plt.xticks([]) #permet de supprimer la graduation des x
        plt.yticks([]) #permet de supprimer la graduation des y
        plt.show()


    """
    Question 7
    """
    def toutes_listes(self):
        """
        Je définis une fonction qui me donne tous les rangements possible des nombres entre 1 et m*n. Les rangement sont contenus dans des listes
        """ 
        toutes_les_listes = []
        def fct(liste): 
            if len(liste)==self.n*self.m:
                toutes_les_listes.append(liste.copy())
                return
            for k in range(1,self.n*self.m + 1):
                if k not in liste:
                    liste+=[k]
                    fct(liste)
                    liste.pop() 
        fct([])
        return toutes_les_listes
        
    def transfo_grille(self):
        """
        On transforme TOUTES les listes en liste de liste pour que l'on puisse représenter sous forme de grille
        """
        liste=self.toutes_listes()
        nv_liste=[]
        for k in liste:  
            sous_liste=[]
            sous_sous_liste=[]
            compte=0
            for j in range(self.m): 
                sous_sous_liste=[]
                for i in range(self.n):
                    sous_sous_liste+=[k[compte]]
                    compte+=1
                sous_liste+=[sous_sous_liste]
            nv_liste+=[sous_liste]
        return nv_liste


    def swap_bis(self,grille,cell1,cell2):
        """
        Je définis une nouvelle fonction swap pour que je puisse swap n'importe quelle grille
        """
        grillebis=[sublist[:] for sublist in grille] #Pour ne pas changer la liste original
        try:
            if ((cell1[0]==cell2[0] and abs(cell1[1]-cell2[1])==1) or (cell1[1]==cell2[1] and abs(cell1[0]-cell2[0])==1)) and cell1[0]>=0 and cell1[1]>=0 and cell2[0]>=0 and cell2[1]>=0:
                a=grillebis[cell1[0]][cell1[1]]
                grillebis[cell1[0]][cell1[1]]=grillebis[cell2[0]][cell2[1]]
                grillebis[cell2[0]][cell2[1]]=a
            return grillebis
        except:
            return grillebis #permet de tratier les swaps dans les foncitons suivantes, impossible de mettre un booléen ou un None
        
    def transfo_liste_en_tuple(self,liste_de_liste):
        """
        Je transforme une liste de liste en tuple de tuple
        """
        tupl=()
        for k in liste_de_liste:
            tuplbis=()
            for i in k:
                tuplbis=tuplbis+(i,)
            tupl=tupl+(tuplbis,)
        return tupl
    

    def dictio(self):
        """
        Je créer un dico avec comme key tous les état possible d'une grille et comme valeurs associés toutes les grilles suite à un swap
        """
        toutes_les_grilles=self.transfo_grille()
        dico={}
        for k in toutes_les_grilles:
            liste=k
            nv_tupl=self.transfo_liste_en_tuple(k)
            dico.update({nv_tupl:[]})
            for i in range(self.m):
                for j in range(self.n):
                    if nv_tupl!=self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i-1,j))) : #regarde si on peut swap les deux ( cf fct swap bis )
                        dico[nv_tupl].append(self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i-1,j)))) 
                    if nv_tupl!=self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i+1,j))):
                        dico[nv_tupl].append(self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i+1,j))))
                    if nv_tupl!=self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i,j-1))):
                        dico[nv_tupl].append(self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i,j-1))))
                    if nv_tupl!=self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i,j+1))):                        
                        dico[nv_tupl].append(self.transfo_liste_en_tuple(self.swap_bis(liste,(i,j),(i,j+1))))
        return dico
    
    def resolution(self):
        """
        Fonction qui premet de résoudre le graph de la manière la plus rapide possible et qui renvoie les différentes étapes 
        """
        dico=self.dictio()
        liste_nodes=[]
        for k in dico:
            liste_nodes+=[k]
        graph=Graph(liste_nodes)
        for k in dico:
            for i in dico[k]:
                graph.add_edge(k,i)
        print("nombre d'élement dans le dictionnaire :",graph.nb_nodes)
        return graph.bfs(self.transfo_liste_en_tuple(self.state),self.transfo_liste_en_tuple([list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)]))
        
    """"
    Question 8
    """

    def transfo_tu_en_li(self,tuple_de_tuples):
        """
        fonction qui transforme un tuple de tuples en liste de listes
        """
        liste_de_listes = []
        for k in tuple_de_tuples:
            liste_de_listes=liste_de_listes+[list(k)]
        return liste_de_listes
    
    

    def resolution_2(self):
        """
        Fonction qui premet de résoudre le graph de la manière la plus rapide possible et qui renvoie les différentes étapes 
        et en créant le graph au fur et à mesure 
        """
        from collections import deque
        dst=self.transfo_liste_en_tuple([list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)])
        src=self.transfo_liste_en_tuple(self.state)
        liste = deque()
        liste.append([src,[src]])
        nombre_vu=[src]
        graphe=Graph([src])
        compte=0
        while liste!=[]:
            compte+=1
            nombre=liste[0][0]
            for i in range(self.m):
                for j in range(self.n):
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))))
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i+1,j))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i+1,j))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(src,(i,j),(i+1,j))))
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j+1))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j+1))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(src,(i,j),(i,j+1))))                       
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))))
            for k in graphe.graph[nombre]:
                if k==dst:
                    print("nombre de sommet :",compte)
                    print("nombre d'élement dans le dictionnaire :",graphe.nb_nodes)
                    return liste[0][1]+[k]
                elif k not in nombre_vu:
                    nombre_vu+=[k]
                    liste.append([(k),liste[0][1]+[k]])
            liste.popleft() 
    
    """
    Question 9
    """
    def ancien_placement_bis(self,grille,num):
        """
        Cette fonction nous permettera de connaitre l'ancien placement pour  n'importe quelle grille
        """
        for k in range(self.n):
            for l in range(self.m):
                if num==grille[l][k]:
                   i=l
                   j=k
        return [i,j]  


    def calcule_de_cout(self,grille):
        """
        Création de la fonction heuristique
        on calcule somme de la distance entre un point et se point bien ordonnée, lequelle on divise par 2
        """
        self.m
        self.n
        compte=0
        liste_rangée=[list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)] 
        for k in range(1,self.n*self.m):
            compte+=np.abs(self.ancien_placement_bis(grille,k)[0]-self.nouveau_placement(k)[0])
            compte+=np.abs(self.ancien_placement_bis(grille,k)[1]-self.nouveau_placement(k)[1])
        return compte

    def calcule_cout_total(self,tuple):
        """
        Calcule la somme distance par rapport à l'origine + heuristique
        """
        return tuple[2]+tuple[3]

    def bfs_2(self):
        """
        Fonction qui premet de résoudre le graph de la manière la plus rapide possible et qui renvoie les différentes étapes 
        et en créant le graph au fur et à mesure 
        """
        dst=self.transfo_liste_en_tuple([list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)])
        src=self.transfo_liste_en_tuple(self.state)
        nombre_vu=[src]
        graphe=Graph([src])
        tas=[]
        compte=0
        heapq.heappush(tas,(self.calcule_cout_total([src,[src],0,self.calcule_de_cout(src)]),[src,[src],0,self.calcule_de_cout(src)]))
        while tas!=[]:
            compte+=1
            historique=tas[0][1][1]
            cout_jusquà_maintenant=tas[0][1][2]
            nombre=(heapq.heappop(tas))[1][0]
            for i in range(self.m):
                for j in range(self.n):
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i-1,j))))
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i+1,j))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i+1,j))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(src,(i,j),(i+1,j))))
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j+1))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j+1))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(src,(i,j),(i,j+1))))                       
                    if nombre!=self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))) and self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))) not in nombre_vu:
                        graphe.add_edge(nombre,self.transfo_liste_en_tuple(self.swap_bis(self.transfo_tu_en_li(nombre),(i,j),(i,j-1))))
            for k in graphe.graph[nombre]:
                if k==dst:         
                    return (("nombre de sommet traversé :"+str(compte)),(historique+[k]))
                elif k not in nombre_vu:
                    nombre_vu+=[k]
                    nouvelle_liste=[k,historique+[k],cout_jusquà_maintenant+1,self.calcule_de_cout(k)]
                    heapq.heappush(tas,(self.calcule_cout_total(nouvelle_liste),nouvelle_liste))
    