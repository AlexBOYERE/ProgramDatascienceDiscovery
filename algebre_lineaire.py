import numpy as np

# Définition d'un vecteur
v1 = np.array([2, 4])
print("Vecteur :", v1)

# Addition de deux vecteurs
v2 = np.array([7, 3])

somme = v1 + v2 # Addition de deux vecteurs
print("Somme :", somme)

# Multiplication de deux vecteurs par un scalaire
scalaire = 3

produit = scalaire * v2
print("Vecteur de :", v2, "; Avec un scalaire de :", scalaire, "; Produit :", produit)

# Produit scalaire
# produit scalaire = v1,1 * v2,1 + v1,2 * v2.2 ....
produit_scalaire = np.dot(v1, v2)

print("Le produit scalaire de V1 :", v1, '; Avec V2 :', v2, "; Produit scalaire :", produit_scalaire)

# Norme d'un vecteur (ou magnitude)
norme = np.linalg.norm(v1)

print("Le norme de V1 :", norme)
