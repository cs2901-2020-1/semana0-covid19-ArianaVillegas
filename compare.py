def compareADN(adn1, adn2):
    a1 = open(adn1, "r")
    a2 = open(adn2, "r")
    if a1.mode=="r" and a2.mode=="r":
        adn_1 = a1.readlines()
        adn_2 = a2.readlines()
        c1 = ""
        s1 = ""
        sim = 0
    
        for x in range(len(adn_1)):
            c1 += adn_1[x][:-2]
        for x in range(len(adn_2)):
            s1 += adn_2[x][:-2]

        for x in range(min(len(c1),len(s1))):
            if c1[x]==s1[x]:
                sim+=1
    a1.close()
    a2.close()
    return sim


virus = ["Tor2","sars BJ01","Wuhan-Hu-1","WHU01","WHU02"]
dir_virus = ["AY274119.txt",
            "AY278488.2.txt",
            "MN908947.txt",
            "MN988668.txt",
            "MN988669.txt"]

print("\nCOMPARACION DE LAS CADENAS DE ADN")
for i in range(len(virus)-1):
    for j in range(i+1,len(virus)):
        print("\nNumero de coincidencias entre {} y {}: {}".format
        (virus[i],virus[j],compareADN(dir_virus[i],dir_virus[j])))

