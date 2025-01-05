def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    liste_mots = file_contents.split()
    counter = 0
    for i in range(0,len(liste_mots)):
       counter +=1
    print(counter)
    
    liste_minuscule = file_contents.lower()
    listing_lettres = {}
    for mots in liste_minuscule:
        for character in mots:
            if character in listing_lettres:
                listing_lettres[character] +=1
            else:
                listing_lettres[character]=1
    print(listing_lettres)
main()

