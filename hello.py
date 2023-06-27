# Calcul de moyenne
# n = int(input("Combien de nombres voulez-vous entrer ? "))
# total = 0

# for i in range(n):
#     nombre = float(input(f"Entrez le nombre {i+1} : "))
#     total += nombre

# moyenne = total / n
# print("La moyenne est :", moyenne)

# Vérification de palindrome
mot = input("Veuillez saisir un mot : ")
if (mot == mot[::-1]):
    print ("C'est une phrase palindromique")
else:
    print ("Ce n'est pas une phrase palindromique.")