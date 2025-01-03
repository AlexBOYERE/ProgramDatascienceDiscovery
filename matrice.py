import numpy as np

# --- Création d'une matrice

M = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Matrice :\n", M)

# --- Opérations sur les matrices

# -- Transposition d'une matrice (consiste à permuter ses lignes et colonnes) - Prends les premiers de chaque colonnes et les mes en lignes
transpose = M.T

print("Transposée :\n", transpose)

# -- Multiplication matricielle (leurs dimensions doivent être compatible

# (A & B sont combinées pour une nouvelle matrice C)
# Pour que la multiplication A×B soit définie, le nombre de colonnes de A doit être égal au nombre de lignes de B.

# A 2 colonnes, 3 lignes
A = np.array([[1,2],[4, 5], [6, 7]])
# B 1 colonne, 2 lignes
B = np.array([[5],[6]])

produit_matriciel = np.dot(A,B)
# Résultat
# [17] - C[0][0]=   (1×5)+(2×6)    =5+12   =17
# [50] - C[1][0]=   (4×5)+(5×6)    =20+30  =50
# [72] - C[2][0]=   (6×5)+(7×6)    =30+42  =72

print ("Produit matriciel :\n", produit_matriciel)