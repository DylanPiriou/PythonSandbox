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
# voyelles = ["a", "e", "i", "o", "u"]
# phrase = input("Veuillez entrer une phrase : ")
# nb_voyelles = 0
# for lettre in phrase.lower():
#     if lettre in voyelles:
#         nb_voyelles += 1
# print(f"Il y a {nb_voyelles} voyelles dans la phrase.")

# Calculette
# first = input("Veuillez entre un premier nombre : ")
# second = input("Veuillez entre un deuxième nombre : ")

# print(f"Le résultat de l'addition du nombre {first} avec le nombre {second} est égale à {int(first) + int(second)}")

# Random
# import random

# tableau = ["hello", "apple", "banana", "hey", "cool"]
# random.shuffle(tableau)
# print(tableau)

# print(random.randint(0, 10))

# tableau = ["hello", "a", "b"]
# tableau.remove("hello")
# print(tableau)

# Générateur nom de dossier
# phrase = input("Entrez un nom de dossier : ")

# caracteres_indesirables = ['?', '!', '.', ',', ';', ':', ' ']
# for caractere in caracteres_indesirables:
#     phrase = phrase.replace(caractere, '_')

# phrase = phrase.lower()

# print(f"Le dossier {phrase} a été créé avec succès !")

# mdp = input("Entrez un mot de passe (min 8 caractères) : ")
# mdp_trop_court = "votre mot de passe est trop court."

# if not mdp:
#     print(mdp_trop_court.upper())
# elif len(mdp)<8:
#     print(mdp_trop_court.capitalize())
# elif mdp.isdigit():
#     print("Votre mot de passe ne contient que des nombres.")
# else:
#     print("Inscription terminée.")

# for i in range(10):
#     print(f"utilisateur {i+1}")

# mot = "Python"
# for lettre in mot[::-1]:
#     print(lettre)

from random import randint

number_to_find = randint(0, 50)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    user_choice = int(user_choice)    

    if number_to_find > user_choice:  # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice:  # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:  # Égal (succès)
        break

    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
    print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

print("Fin du jeu.")