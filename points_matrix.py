import pandas as pd
import numpy as np


#################### EXCEL ######################        

#     A     B     C
# 1   x     y     z    ->  A1 = x, B1 = y, C1 = z
# 2   12    20    17   ->  Generic example
# 3   ... 

# Utilizar . para separar a parte decimal

##################################################

def points_matrix():
    matrix = pd.read_excel('matrix.xlsx')
    return(matrix.to_numpy())
