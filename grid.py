"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import math
from graph import Graph


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
        
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        m=self.m
        n=self.n
        liste_rangée=[list(range(i*n+1, (i+1)*n+1)) for i in range(m)] 
        a=0
        for k in range(m):
            for i in range(n):
                if self.state[k][i]!=liste_rangée[k][i]:
                    a=1
        return a==0

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if (cell1[0]==cell2[0] and abs(cell1[1]-cell2[1])==1) or (cell1[1]==cell2[1] and abs(cell1[0]-cell2[0])==1):
            a=self.state[cell1[0]][cell1[1]]
            self.state[cell1[0]][cell1[1]]=self.state[cell2[0]][cell2[1]]
            self.state[cell2[0]][cell2[1]]=a
        """
        else:
            raise ValueError("L'échange n'est pas autorisé")
        """
    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for k in range(int(len(cell_pair_list))):
            self.swap(cell_pair_list[k][0],cell_pair_list[k][1])
    
    def transfo_liste_en_tuple(self,liste_de_liste):
        """
        Je transforme une liste de liste en tuple de tuple pour implementer la grille dans graph
        """
        tupl=()
        for k in liste_de_liste:
            tuplbis=()
            for i in k:
                tuplbis=tuplbis+(i,)
            tupl=tupl+(tuplbis,)
        return tupl

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


