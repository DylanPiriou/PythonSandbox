# Calcul de moyenne
# n = int(input("Combien de nombres voulez-vous entrer ? "))
# total = 0

# for i in range(n):
#     nombre = float(input(f"Entrez le nombre {i+1} : "))
#     total += nombre

# moyenne = total / n
# print("La moyenne est :", moyenne)

# Vérification de palindrome
# mot = input("Veuillez saisir un mot : ")
# if (mot == mot[::-1]):
#     print ("C'est une phrase palindromique")
# else:
#     print ("Ce n'est pas une phrase palindromique.")

# Compter le nombre de voyelles
voyelles = ["a", "e", "i", "o", "u"]
phrase = input("Veuillez entrer une phrase : ")
nb_voyelles = 0
for lettre in phrase.lower():
    if lettre in voyelles:
        nb_voyelles += 1
print(f"Il y a {nb_voyelles} voyelles dans la phrase.")