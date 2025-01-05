def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    liste_mots = file_contents.split()
    counter = 0
    for i in range(0,len(liste_mots)):
       counter +=1
        
    liste_minuscule = file_contents.lower()
    listing_lettres = {}
    for mots in liste_minuscule:
        for character in mots:
            if character in listing_lettres:
                listing_lettres[character] +=1
            else:
                listing_lettres[character]=1
    
    dict_final = {}
    for clés in listing_lettres.keys():
        if clés.isalpha() == True:
            dict_final[clés]=listing_lettres[clés] 

    liste_finale = []
    for clés in dict_final:        
        liste_finale.append({"lettre":clés,"occurences":dict_final[clés]})
    
    def sort_on(dict):
     return dict["occurences"] 
    
    liste_finale.sort(reverse=True, key=sort_on)
    print(liste_finale)



main()

