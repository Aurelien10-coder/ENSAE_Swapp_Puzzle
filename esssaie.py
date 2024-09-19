from grid import Grid
from solver import Solver 
from graph import Graph


#Réponse à la question 3
print("question 3")
grille=Solver(3,2,[])
grille.swap_seq([((0,0),(1,0)),((1,0),(2,0)),((1,1),(2,1)),((2,1),(2,0))])
print(grille.get_solution())
print("Nombre de swap avec la solution naive : ",len(grille.get_solution()),"\n")


#Réponse à la question 4
print("question 4")
graph = Graph.graph_from_file("input/graph1.in")
print("test fonction bfs : ",graph.bfs(7,14),"\n")

#Réponse à la question 7
print("question 7")

grille=Solver(3,2,[])
grille.swap_seq([((0,0),(1,0)),((1,0),(2,0)),((1,1),(2,1)),((2,1),(2,0))])
#grille.repres()
solution=grille.resolution()
print(solution)
print("Nombre de swap avec bfs : ",len(solution),"\n")

"""
Nous observons que au lieu d'avoir 14 swaps comme dans la version naive nous en avons seuelement 4
"""

#Réponse à la question 8
print("question 8")
grille=Solver(3,2,[])
grille.swap_seq([((0,0),(1,0)),((1,0),(2,0)),((1,1),(2,1)),((2,1),(2,0))])


print(grille.resolution_2(),"\n")

grille=Solver(3,3,[])
grille.swap_seq([((0,0),(1,0)),((1,0),(2,0)),((1,1),(2,1)),((2,1),(2,0))])

print(grille.resolution_2(),"\n")

"""
Nous observons que au lieu d'avoir 720 élement dans le dictionnaire nous en avons que 117
"""

#Réponse à la question 9
print("question 9")

grille=Solver(3,3,[])
grille.swap_seq([((0,0),(1,0)),((1,0),(2,0)),((1,1),(2,1)),((2,1),(2,0))])


print(grille.bfs_2(),"\n")



m=5
n=5

import numpy as np
nombres = np.arange(1, n*m+1)
np.random.shuffle(nombres)

liste=[]
compteur=0
for k in range(m):
    liste_bis=[]
    for i in range(n):
        liste_bis+=[nombres.tolist()[compteur+i]]
    liste+=[liste_bis]
    compteur+=n


grille=Solver(m,n,initial_state=liste)
bfs2=grille.bfs_2()
print(bfs2)



#Plus , création d'une interface de la grille pour voir l'évolution de la résultion selon méthode naive ou BFS
"""
voir l'évolution de la grille
"""
import pygame
def représentation_graphique(grille):
    hor=900
    ver=900
    
    # Variable 
    Run=True
    run_bis=True
    compte=0
    n=grille.n
    m=grille.m
    nouveau_swap=False
    gauche=False
    droite=False

    # initialisation 
    pygame.init()
    screen=pygame.display.set_mode((hor,ver))
    player = pygame.Rect((350, 250, 50, 50))
    font=pygame.font.Font(None,size=80)
        
    while Run:


        screen.fill((255, 255, 255))
        while run_bis:
            pygame.draw.line(screen,"BLACK",(0,ver/2),(hor,ver/2),3)
            
            text=font.render("Méthode naive",True,"BLACK")
            text_rect=text.get_rect(center=(hor/2,ver/4))
            screen.blit(text, text_rect)
            
            text=font.render("Méthode BFS",True,"BLACK")
            text_rect=text.get_rect(center=(hor/2,3*ver/4))
            screen.blit(text, text_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run=False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x2,y2) = pygame.mouse.get_pos() 
                    if y2>ver/2:
                        bfs=True
                        toutes_les_étapes=grille.bfs_2()[1] 
                        run_bis=False
                        compte=0
                    else:
                        grille_bis=[sous_liste.copy() for sous_liste in grille.state]
                        tous_les_swaps=grille.get_solution()
                        bfs=False
                        print(tous_les_swaps)
                        run_bis=False
                        compte=-1
            pygame.display.flip()

                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run=False
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    compte_bis=compte
                    droite=True
                    if bfs:
                       compte=compte+1
                       if compte==len(toutes_les_étapes):
                            compte=compte-1
                    else:
                        if gauche==True:
                            nouveau_swap=True
                            gauche=False
                        else:
                            compte+=1
                            nouveau_swap=True
                            if compte==len(tous_les_swaps):
                                nouveau_swap=False
                                compte=compte-1
                elif event.key==pygame.K_LEFT:
                    gauche=True
                    if bfs:
                        compte=compte-1
                        if compte==-1:
                            compte=0
                    else:
                        if droite:
                            nouveau_swap=True
                            droite=False
                        else:
                            compte=compte-1
                            nouveau_swap=True
                            if compte==-1:
                                nouveau_swap=False
                                compte=compte+1                          


        vecteur_x=[]
        vecteur_y=[]
        for k in range(n):
            vecteur_x=[hor/n + hor/n*k]+vecteur_x
        for k in range(m):
            vecteur_y=[ver/m + ver/m*k]+vecteur_y
        for k in vecteur_x:
            pygame.draw.line(screen,"BLACK",(k,0),(k,ver),2)
        for k in vecteur_y:
            pygame.draw.line(screen,"BLACK",(0,k),(hor,k),2)
        
        
        if bfs:
            grille_bis=toutes_les_étapes[compte]
            for k in range(m):
                for i in range(n):
                    text=font.render(str(grille_bis[k][i]),True,"BLACK")
                    text_rect=text.get_rect(center=(i*ver/n+ver/(n*2),k*hor/m+hor/(m*2)))
                    screen.blit(text, text_rect)
            pygame.display.flip()
        else:
            if nouveau_swap:
                cell1=tous_les_swaps[compte][0]
                cell2=tous_les_swaps[compte][1]
                cell=grille_bis[cell1[0]][cell1[1]]
                grille_bis[cell1[0]][cell1[1]]=grille_bis[cell2[0]][cell2[1]]
                grille_bis[cell2[0]][cell2[1]]=cell
                for k in range(m):
                    for i in range(n):
                        text=font.render(str(grille_bis[k][i]),True,"BLACK")
                        text_rect=text.get_rect(center=(i*ver/n+ver/(n*2),k*hor/m+hor/(m*2)))
                        screen.blit(text, text_rect)
                nouveau_swap=False
            else:
                for k in range(m):
                    for i in range(n):
                        text=font.render(str(grille_bis[k][i]),True,"BLACK")
                        text_rect=text.get_rect(center=(i*ver/n+ver/(n*2),k*hor/m+hor/(m*2)))
                        screen.blit(text, text_rect)
                pygame.display.flip()
        pygame.display.flip()
    pygame.quit()


grille=Solver(m,n,initial_state=liste)
représentation_graphique(grille)