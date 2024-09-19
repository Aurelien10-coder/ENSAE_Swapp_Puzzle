import pygame
import time
from solver import Solver
import numpy as np


#fonction pour difficulté de la matrice:
def difficulte(m,n,dif):
    bool=True
    nombres=np.arange(1,n*m+1)
    while bool:
        np.random.shuffle(nombres)
        liste=[]
        compte=0
        for k in range(m):
            liste_bis=[]
            for i in range(n):
                liste_bis+=[nombres.tolist()[compte+i]] #totliste pour transformer en liste classique 
            liste+=[liste_bis]
            compte+=n
        liste_bis_bis=Solver(m,n,initial_state=liste)
        print(liste_bis_bis)
        if len(liste_bis_bis.bfs_2()[1])>dif:
            bool=False
    return liste_bis_bis

#Fonction pour deux swaps interdits, de manière aléatoire : 
def fct_interdiction(m,n):
    liste_interd=[]
    for k in range(m):
        for i in range(n):
            liste_interd+=[[k,i]]
    arange=np.arange(len(liste_interd))
    inter_1=liste_interd[np.random.choice(arange)]
    liste_voisin=[(1,0),(-1,0),(0,-1),(0,1)]
    arange_bis=np.arange(4)
    bool=True
    while bool:
        inter_1_2=liste_voisin[np.random.choice(arange_bis)]
        if 0<=inter_1[0]+inter_1_2[0]<=m-1 and  0<=inter_1[1]+inter_1_2[1]<=n-1:  
            swap_inter_1=[inter_1,[inter_1[0]+inter_1_2[0],inter_1[1]+inter_1_2[1]]]
            bool=False
    bool=True
    while bool:
        inter_2=liste_interd[np.random.choice(arange)]
        if inter_2!=inter_1 and inter_2!=inter_1_2:
            bool=False
    bool=True
    while bool:
        inter_2_2=liste_voisin[np.random.choice(arange_bis)]
        if 0<=inter_2[0]+inter_2_2[0]<=m-1 and  0<=inter_2[1]+inter_2_2[1]<=n-1 and inter_2_2!=inter_1 and inter_2_2!=inter_1_2:
            swap_inter_2=[inter_2,[inter_2[0]+inter_2_2[0],inter_2[1]+inter_2_2[1]]]
            bool=False
    return [swap_inter_1,swap_inter_2]


#taille de la matrice
hor=900
ver=900

# Variable 
Run=True
compte_bis=0
run_bis_bis=True
nouveau_swap=False

# initialisation 
pygame.init()
screen=pygame.display.set_mode((hor,ver))
player = pygame.Rect((350, 250, 50, 50))
font=pygame.font.Font(None,size=80)
font2=pygame.font.Font(None,size=60)
while Run:
   
    screen.fill((255, 255, 255))
    
    """
    On créé la difficulté du jeu
    """
    while run_bis_bis:
        screen.fill((255, 255, 255))
        difficulté=["Facile","Moyen","Difficile"]
        for k in range(3):
            pygame.draw.line(screen,"BLACK",(0,ver/3*k),(hor,ver/3*k),2)
            texte=font.render(difficulté[k],True,"BLACK")
            texte_rect=texte.get_rect(center=(hor/2,hor/3*k + ver/(3*2)))
            screen.blit(texte, texte_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.quit:
                Run=False
                run_bis_bis=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                
                if y>ver/3*2:                 
                    array=np.array([4,5])
                    m=np.random.choice(array)
                    n=np.random.choice(array)
                    grille=difficulte(m,n,20)
                    run_bis_bis=False
                    #créer deux swaps interdit,ça de manières aléatoire
                    interdiction=True
                    swap_inter=fct_interdiction(m,n)
                    inter_1=swap_inter[0]
                    inter_2=swap_inter[1]
                    print(inter_1,inter_2)

                elif y>ver/3:
                    array=np.array([3,4])
                    m=np.random.choice(array)
                    n=np.random.choice(array)
                    grille=difficulte(m,n,10)
                    run_bis_bis=False
                    interdiction=False
                else: 
                    array=np.array([3])
                    n=np.random.choice(array)
                    m=np.random.choice(array)
                    grille=difficulte(m,n,5)
                    run_bis_bis=False
                    interdiction=False
                nb_swap=len(grille.bfs_2()[1])-1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            compte=0
            x1,y1 = pygame.mouse.get_pos()
            compte+=1
            while compte != 2:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x2,y2) = pygame.mouse.get_pos()                            
                        compte+=1
            carre1=[0,0]
            carre2=[0,0]
            for k in range(n):
                if x1>ver/n*k:
                    carre1[1]=k
                if x2>ver/n*k:
                    carre2[1]=k
            for k in range(m):
                if y1>hor/m*k:
                    carre1[0]=k
                if y2>hor/m*k:
                    carre2[0]=k
            print([carre1,carre2])
            grille_avant_swap=[sous_liste.copy() for sous_liste in grille.state]
            if interdiction:
                if inter_1!=[carre1,carre2] and inter_1!=[carre2,carre1] and inter_2!=[carre1,carre2] and inter_2!=[carre2,carre1]:
                    grille.swap(tuple(carre1),tuple(carre2))
                    compte_bis+=1
            else:
                grille.swap(tuple(carre1),tuple(carre2))
                compte_bis+=1
            nouveau_swap=True
            Col="GREEN"
            if grille.state==grille_avant_swap:
                Col="RED"


    run_bis=grille.is_sorted()    
    while run_bis:
        screen.fill((255, 255, 255))
        text=font2.render("Vous avez gagné en "+str(compte_bis)+" swaps.",True,"BLACK")
        text_rect=text.get_rect(center=(hor//2,ver//2-50))
        if not interdiction:
            text2=font2.render("Vous auriez pu gagner en "+str(nb_swap)+" swaps.",True,"BLACK")
            text_rect2=text.get_rect(center=(hor//2-50,ver//2+50))
            screen.blit(text2,text_rect2)
        screen.blit(text,text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_bis=False
                Run=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Run=False
                run_bis=False


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
    for k in range(m):
        for i in range(n):
            text=font.render(str(grille.state[k][i]),True,"BLACK")
            text_rect=text.get_rect(center=(i*ver/n+ver/(n*2),k*hor/m+hor/(m*2)))
            screen.blit(text, text_rect)
    
    if interdiction: 
        if inter_1[0][0]==inter_1[1][0]: # signifie que c'est une ligne verticale
            pygame.draw.line(screen,"RED",(hor/n*max(inter_1[0][1],inter_1[1][1]),ver/m*(inter_1[0][0])),(hor/n*max(inter_1[0][1],inter_1[1][1]),ver/m*(inter_1[0][0]+1)),width=5)
        else: 
            pygame.draw.line(screen,"RED",(hor/n*inter_1[0][1],ver/m*max(inter_1[0][0],inter_1[1][0])),(hor/n*(inter_1[1][1]+1),ver/m*max(inter_1[0][0],inter_1[1][0])),width=5)
        if inter_2[0][0]==inter_2[1][0]: # ligne verticale
            pygame.draw.line(screen,"RED",(hor/n*max(inter_2[0][1],inter_2[1][1]),ver/m*(inter_2[0][0])),(hor/n*max(inter_2[0][1],inter_2[1][1]),ver/m*(inter_2[0][0]+1)),width=5)
        else:
            pygame.draw.line(screen,"RED",(hor/n*inter_2[0][1],ver/m*max(inter_2[0][0],inter_2[1][0])),(hor/n*(inter_2[1][1]+1),ver/m*max(inter_2[0][0],inter_2[1][0])),width=5)

    if nouveau_swap:
        pygame.draw.line(screen,Col,(0,0),(0,ver),width=15)
        pygame.draw.line(screen,Col,(0,0),(hor,0),width=15)
        pygame.draw.line(screen,Col,(hor,0),(hor,ver),width=15)
        pygame.draw.line(screen,Col,(0,ver),(hor,ver),width=15)
        pygame.display.flip()
        time.sleep(0.25)
        nouveau_swap=False
    else:
        pygame.display.flip()

pygame.quit()