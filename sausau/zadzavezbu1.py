def podela(niz, donjaGranica, gornjaGranica):
    pivot = niz[gornjaGranica]
    i = donjaGranica - 1
    for j in range(donjaGranica, gornjaGranica):
        if niz[j] <= pivot:
            i+=1
            niz[i], niz[j] = niz[j], niz[i]
    niz[i+1], niz[gornjaGranica] = niz[gornjaGranica], niz[i+1]

    return i+1

def quickSort(niz, donjaGranica, gornjaGranica):
    if donjaGranica < gornjaGranica:
        index = podela(niz, donjaGranica, gornjaGranica)
        quickSort(niz, donjaGranica, index-1)
        quickSort(niz, index+1, gornjaGranica)
    return niz

def prviZadatak(niz):
    donjaGranica = 0
    gornjaGranica = len(niz)-1
    while donjaGranica <= gornjaGranica:
        sredina = (donjaGranica+gornjaGranica) // 2
        if niz[sredina] == sredina:
            donjaGranica=sredina+1
        else:
            gornjaGranica=sredina-1
    return donjaGranica

def prvi(niz):
    trenutni = niz[0]
    if trenutni !=0:
        return 0
    
    for elem in niz[1:]:
        if elem == trenutni + 1:
            trenutni = elem
        else:
            return trenutni + 1
    
    return trenutni+1
        
niz1 = [ 1, 2, 3, 4]
# print(prvi(niz1))
# print(prvi([0, 1, 2, 3, 4, 5, 7]))

print(prviZadatak(niz1))
print(prviZadatak([0, 1, 2, 3, 4, 5, 7]))

def drugiZadatak(niz):
    donjaGranica = 0
    gornjaGranica = len(niz)-1
    while donjaGranica <= gornjaGranica:
        sredina = (donjaGranica+gornjaGranica) // 2
        if niz[sredina] == sredina:
            return sredina
        elif niz[sredina] < sredina:
            donjaGranica=sredina+1
        else:
            gornjaGranica=sredina-1
    return -1

def treciZadatak(niz):
    niz = quickSort(niz, 0, len(niz) - 1)
    proizvod1 = niz[0]*niz[1]
    print(niz[0], niz[1], niz[len(niz)-1], niz[len(niz)-2])
    proizvod2 = niz[len(niz)-1]*niz[len(niz)-2]
    if proizvod1 > proizvod2:
        return proizvod1
    else:
        return proizvod2

def treciZadatak2(niz):
    max1 = max2 = float('-inf') 
    for broj in niz:
        if broj > max1:
            max2 = max1
            max1 = broj
        elif broj > max2:
            max2 = broj
    return max1 * max2


#print(treciZadatak2([3, 7, 1, 0, 67, 32, 45, 12, 4]))

def cetvrti(niz):
    trojke=[]
    niz = quickSort(niz, 0, len(niz) - 1)
    for i in range(len(niz)-2):
        j = i+1
        k = len(niz)-1
        while j<k :
            if niz[i] + niz[j] + niz[k] <= 100 :
                trojke.append((niz[i], niz[j], niz[k]))
                j+=1
            else:
                k-=1
        
    return trojke

def peti(niz):
    niz = quickSort(niz, 0, len(niz) - 1)
    nedostajuci = 1
    for elem in niz:
        if elem <= nedostajuci:
            nedostajuci += elem
            print(nedostajuci)
        else:
            break
    return nedostajuci

# Rekurzivna binarna pretraga
def drugi(niz, l, r):
    if r >= l:
        sred = (l + r) // 2
        if niz[sred] == sred:
            return sred
 
        elif niz[sred] > sred:
            return drugi(niz, l, sred-1)
 
        else:
            return drugi(niz, sred + 1, r)
 
    else:
        return -1


#print(peti([1, 2, 5, 20, 40]))
#print(cetvrti([3, 2, 5, 12, 4, 78, 55, 90, 32, 123, 63, 78, 24, 1, -8]))
