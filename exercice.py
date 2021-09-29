#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:

    if values is None:
        # TODO: demander les valeurs ici
        list = input('entrez 10 valejrs séparés par des espaces:').split()
        print(list)
        return list

def anagrams(words: list = None) -> bool:
    if words is None:
        list1 = input("entrer le premier mot:")
        list2 = input("entrer le deuxieme mot:")
        if sorted (list1) == sorted(list2):
            print("oui")
            return True
        else:
            print("non")
            return False

        # TODO: demander les mots ici

def contains_doubles(items: list) -> bool:
    set1 = set(items)
    if len(set1) == len(items):
        print("Liste contient tous des éléments uniques")
    else:
        print("Liste ne contient pas uniquement des éléments uniques")

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        average = sum(value)/len(value)

        if len(best_student) == 0 or (best_student.values())[0] < average:
            best_student = {key: average}



    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequency = dict()

    frequency = {letter: sentence.count(letter) for letter in sentence}

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse = True)
    for key in sorted_keys:
        if frequency [key] > 5:
            print("le caractère {key} contient {frequency [key]}")
    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Quel est le nom de votre recette").split()
    ingredients = input("entrez la liste d'ingredients, Inserer les ingredients par une virgule").split()

    return{name:ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Quel est le nom de la recette:").split()
    if name in ingredients:
        print(ingredients[name])

    else:
        print("Je ne connais pas la recette")
        print_recipe()



def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
